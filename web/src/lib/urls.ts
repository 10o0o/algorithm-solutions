import { execFileSync } from 'node:child_process';
import { existsSync, lstatSync, realpathSync } from 'node:fs';
import path from 'node:path';

export const REPOSITORY_URL = 'https://github.com/10o0o/algorithm-solutions';
const PROHIBITED = new Set(['.git', '.local', '.venv', '.venv-pypy', '.cph', 'private']);
const ROOT_SCRATCH = new Set(['main.py', 'ex.in']);

export function normalizedBase(base: string): string {
  const parts = base.split('/').filter(Boolean);
  return parts.length ? `/${parts.join('/')}/` : '/';
}
export function withBase(pathname: string, base = import.meta.env.BASE_URL): string {
  const suffix = pathname.replace(/^\/+/, '');
  return `${normalizedBase(base)}${suffix}`;
}
function safeSegments(id: string, label: string): string[] {
  const parts = id.split('/');
  if (parts.some((part) => !part || part === '.' || part === '..' || part.includes('\\') || part.includes('\0'))) {
    throw new Error(`Invalid ${label} id: ${id}`);
  }
  return parts;
}
export function conceptUrl(id: string, base = import.meta.env.BASE_URL): string {
  const parts = safeSegments(id, 'knowledge');
  if (parts.length !== 2) throw new Error(`Invalid knowledge id: ${id}`);
  return withBase(`knowledge/${parts.map(encodeURIComponent).join('/')}/`, base);
}
export function problemUrl(id: string, base = import.meta.env.BASE_URL): string {
  const parts = safeSegments(id, 'problem');
  if (parts.length < 2 || !['atcoder', 'codeforces', 'leetcode'].includes(parts[0])) throw new Error(`Invalid problem id: ${id}`);
  return withBase(`problems/${parts.map(encodeURIComponent).join('/')}/`, base);
}
export function contestUrl(id: string, base = import.meta.env.BASE_URL): string {
  if (safeSegments(id, 'contest').length !== 1) throw new Error(`Invalid contest id: ${id}`);
  return withBase(`contests/${encodeURIComponent(id)}/`, base);
}
export function recordUrl(kind: 'concept' | 'problem' | 'contest', id: string, base = import.meta.env.BASE_URL): string {
  return kind === 'concept' ? conceptUrl(id, base) : kind === 'problem' ? problemUrl(id, base) : contestUrl(id, base);
}
function inside(candidate: string, root: string): boolean {
  const rel = path.relative(root, candidate);
  return rel === '' || (!rel.startsWith('..') && !path.isAbsolute(rel));
}
function assertNoSymlink(candidate: string, root: string): void {
  const relative = path.relative(root, candidate);
  if (!inside(candidate, root)) throw new Error(`Content link escapes the repository: ${relative}`);
  let cursor = root;
  for (const segment of relative.split(path.sep).filter(Boolean)) {
    cursor = path.join(cursor, segment);
    if (lstatSync(cursor).isSymbolicLink()) throw new Error(`Content links may not traverse symlinks: ${relative}`);
  }
}
function repoPathToRecord(relative: string, base: string): string | undefined {
  const slash = relative.split(path.sep).join('/');
  if (/(?:^|\/)(?:README|template)\.md$/iu.test(slash)) return undefined;
  if (/^knowledge\/[^/]+\/[^/]+\.md$/u.test(slash)) return conceptUrl(slash.slice(10, -3), base);
  if (/^(atcoder|codeforces|leetcode)\/.+\.md$/u.test(slash)) return problemUrl(slash.slice(0, -3), base);
  if (/^contests\/[^/]+\.md$/u.test(slash) && !/(?:README|template)\.md$/u.test(slash)) return contestUrl(slash.slice(9, -3), base);
  return undefined;
}
function isIgnored(root: string, relative: string): boolean {
  if (!existsSync(path.join(root, '.git'))) return false;
  try { execFileSync('git', ['check-ignore', '--quiet', '--', relative], { cwd: root, stdio: 'ignore' }); return true; }
  catch (error) { return (error as { status?: number }).status !== 1; }
}
export function resolveContentLink(target: string, sourceFile: string, repoRoot: string, base = import.meta.env.BASE_URL): string {
  if (!target || target.startsWith('#') || target.startsWith('//')) return target;
  const scheme = target.match(/^([a-z][a-z0-9+.-]*):/iu)?.[1]?.toLowerCase();
  if (scheme) {
    if (['http', 'https', 'mailto', 'tel', 'data'].includes(scheme)) return target;
    throw new Error(`Unsupported content link scheme: ${scheme}`);
  }
  if (target.startsWith('/')) throw new Error(`Root-absolute content links are not allowed: ${target}`);
  const match = target.match(/^([^?#]*)([?#].*)?$/u);
  if (!match?.[1]) return target;
  let decoded: string;
  try { decoded = decodeURIComponent(match[1]); } catch { throw new Error(`Content link has invalid percent encoding: ${target}`); }
  if (decoded.includes('\\') || decoded.includes('\0')) throw new Error(`Content link contains an invalid path: ${target}`);
  const root = realpathSync(repoRoot);
  const source = path.isAbsolute(sourceFile) ? path.normalize(sourceFile) : path.resolve(root, sourceFile);
  if (!existsSync(source) || !lstatSync(source).isFile()) throw new Error(`Content source file does not exist: ${sourceFile}`);
  assertNoSymlink(source, root);
  const resolved = path.resolve(path.dirname(source), decoded);
  if (!inside(resolved, root)) throw new Error(`Content link escapes the repository: ${target}`);
  const relative = path.relative(root, resolved);
  const parts = relative.split(path.sep);
  if (parts.some((part) => PROHIBITED.has(part)) || ROOT_SCRATCH.has(relative)) throw new Error(`Content link targets a prohibited path: ${target}`);
  if (!existsSync(resolved)) throw new Error(`Content link target does not exist: ${target}`);
  assertNoSymlink(resolved, root);
  if (!lstatSync(resolved).isFile() || !inside(realpathSync(resolved), root)) throw new Error(`Content link target is not a public file: ${target}`);
  if (isIgnored(root, relative)) throw new Error(`Content link targets an ignored path: ${target}`);
  const suffix = match[2] ?? '';
  const internal = repoPathToRecord(relative, base);
  if (internal) return `${internal}${suffix}`;
  const encoded = relative.split(path.sep).map(encodeURIComponent).join('/');
  return `${REPOSITORY_URL}/blob/main/${encoded}${suffix}`;
}

export function repositoryFileUrl(relative: string): string {
  return `${REPOSITORY_URL}/blob/main/${relative.split('/').map(encodeURIComponent).join('/')}`;
}

export function assertPublicRepositoryFile(relative: string, repoRoot: string): string {
  const root = realpathSync(repoRoot);
  const candidate = path.resolve(root, relative);
  if (!inside(candidate, root)) throw new Error(`Public file escapes the repository: ${relative}`);
  const lexical = path.relative(root, candidate);
  const parts = lexical.split(path.sep);
  if (parts.some((part) => PROHIBITED.has(part)) || ROOT_SCRATCH.has(lexical)) throw new Error(`Public file targets a prohibited path: ${relative}`);
  if (!existsSync(candidate)) throw new Error(`Public file does not exist: ${relative}`);
  assertNoSymlink(candidate, root);
  if (!lstatSync(candidate).isFile() || !inside(realpathSync(candidate), root)) throw new Error(`Public path is not a repository file: ${relative}`);
  if (isIgnored(root, lexical)) throw new Error(`Public file is ignored: ${relative}`);
  return realpathSync(candidate);
}
