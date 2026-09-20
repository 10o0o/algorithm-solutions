import { getCollection, type CollectionEntry } from 'astro:content';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import type { Definition, Link, LinkReference, Root, RootContent } from 'mdast';
import { toString } from 'mdast-util-to-string';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import remarkParse from 'remark-parse';
import { unified } from 'unified';
import { visit } from 'unist-util-visit';
import { assertPublicRepositoryFile } from './urls';

export const AREAS = [
  { id: 'basics', label: '기초', description: '배열과 포인터, 누적해서 생각하는 법', symbol: '∑' },
  { id: 'search', label: '탐색', description: '정답의 범위와 상태 공간을 줄이는 법', symbol: '⌕' },
  { id: 'graphs', label: '그래프', description: '연결된 상태를 빠짐없이 방문하는 법', symbol: '⌘' },
] as const;
export const PLATFORMS = [
  { id: 'atcoder', label: 'AtCoder' },
  { id: 'codeforces', label: 'Codeforces' },
  { id: 'leetcode', label: 'LeetCode' },
] as const;
export interface AreaInfo { id:string; label:string; description:string; symbol:string }
export function areaInfo(id: string): AreaInfo {
  const known = AREAS.find((area) => area.id === id);
  return known ?? { id, label: id, description: '새로 연결한 알고리즘 개념', symbol: '·' };
}

export type RecordKind = 'concept' | 'problem' | 'contest';
type AnyEntry = CollectionEntry<'knowledge'> | CollectionEntry<'problems'> | CollectionEntry<'contests'>;
export interface PublicRecord {
  key: string;
  kind: RecordKind;
  id: string;
  title: string;
  updated: string;
  tags: string[];
  summary: string;
  area?: string;
  platform?: string;
  sourcePath: string;
  url?: string;
  solution?: string;
  relatedKeys: string[];
  backlinkKeys: string[];
  entry: AnyEntry;
}

function tree(body: string): Root { return unified().use(remarkParse).use(remarkGfm).use(remarkMath).parse(body) as Root; }
function sectionNodes(root: Root, heading: string): RootContent[] {
  const start = root.children.findIndex((node) => node.type === 'heading' && node.depth === 2 && toString(node).trim() === heading);
  if (start < 0) return [];
  const nodes: RootContent[] = [];
  for (const node of root.children.slice(start + 1)) {
    if (node.type === 'heading' && node.depth === 2) break;
    nodes.push(node);
  }
  return nodes;
}
export function extractSummary(body: string): string {
  return sectionNodes(tree(body), '핵심 요약').map((node) => toString(node).trim()).filter(Boolean).join(' ').replace(/\s+/gu, ' ').trim();
}
function extractLead(body: string): string {
  const root = tree(body);
  const paragraph = root.children.find((node) => node.type === 'paragraph');
  return paragraph ? toString(paragraph).replace(/\s+/gu, ' ').trim() : '';
}
export function normalizeDate(value: string | Date): string {
  const result = value instanceof Date ? value.toISOString().slice(0, 10) : value.trim();
  const parsed = new Date(`${result}T00:00:00.000Z`);
  if (!/^\d{4}-\d{2}-\d{2}$/u.test(result) || Number.isNaN(parsed.getTime()) || parsed.toISOString().slice(0, 10) !== result) {
    throw new Error(`Invalid updated date: ${String(value)}`);
  }
  return result;
}
function recordSource(kind: RecordKind, id: string): string {
  return kind === 'concept' ? `knowledge/${id}.md` : kind === 'contest' ? `contests/${id}.md` : `${id}.md`;
}
function keyFromSource(relative: string): string | undefined {
  const slash = relative.split(path.sep).join('/');
  if (/(?:^|\/)(?:README|template)\.md$/iu.test(slash)) return undefined;
  if (/^knowledge\/[^/]+\/[^/]+\.md$/u.test(slash)) return `concept:${slash.slice(10, -3)}`;
  if (/^(atcoder|codeforces|leetcode)\/.+\.md$/u.test(slash)) return `problem:${slash.slice(0, -3)}`;
  if (/^contests\/[^/]+\.md$/u.test(slash) && !/(?:README|template)\.md$/u.test(slash)) return `contest:${slash.slice(9, -3)}`;
  return undefined;
}
function linkedKeys(body: string, sourcePath: string): string[] {
  const result = new Set<string>();
  const root = tree(body);
  const definitions = new Map<string, string>();
  visit(root, 'definition', (node: Definition) => { definitions.set(node.identifier.toLowerCase(), node.url); });
  const add = (url: string) => {
    if (!url || url.startsWith('/') || url.startsWith('//') || /^[a-z][a-z0-9+.-]*:/iu.test(url)) return;
    const raw = url.split(/[?#]/u, 1)[0];
    if (!raw.endsWith('.md')) return;
    let decoded: string;
    try { decoded = decodeURIComponent(raw); } catch { throw new Error(`Related link has invalid encoding in ${sourcePath}: ${url}`); }
    if (decoded.includes('\\') || decoded.includes('\0')) throw new Error(`Related link has an invalid path in ${sourcePath}: ${url}`);
    const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(sourcePath), decoded));
    if (resolved.startsWith('../') || resolved === '..') throw new Error(`Related link escapes the repository in ${sourcePath}: ${url}`);
    const key = keyFromSource(resolved);
    if (key) result.add(key);
  };
  visit(root, 'link', (node: Link) => add(node.url));
  visit(root, 'linkReference', (node: LinkReference) => { const url = definitions.get(node.identifier.toLowerCase()); if (url) add(url); });
  return [...result];
}
function makeRecord(kind: RecordKind, entry: AnyEntry): PublicRecord {
  const id = entry.id;
  const data = entry.data as { title: string; updated: string | Date; tags: string[]; url?: string; solution?: string };
  const sourcePath = recordSource(kind, id);
  const summary = extractSummary(entry.body ?? '') || (kind === 'concept' ? '' : extractLead(entry.body ?? ''));
  if (!summary && kind === 'concept') throw new Error(`${sourcePath} has no 핵심 요약 section`);
  const record: PublicRecord = {
    key: `${kind}:${id}`, kind, id, title: data.title, updated: normalizeDate(data.updated), tags: [...data.tags], summary,
    sourcePath, url: data.url, solution: data.solution, relatedKeys: linkedKeys(entry.body ?? '', sourcePath), backlinkKeys: [], entry,
  };
  if (kind === 'concept') {
    record.area = id.split('/')[0];
  } else if (kind === 'problem') {
    record.platform = id.split('/')[0];
    if (!PLATFORMS.some((platform) => platform.id === record.platform)) throw new Error(`Unknown problem platform: ${record.platform}`);
  }
  return record;
}
export async function getRecords(): Promise<PublicRecord[]> {
  const [knowledge, problems, contests] = await Promise.all([getCollection('knowledge'), getCollection('problems'), getCollection('contests')]);
  const records = [
    ...knowledge.map((entry) => makeRecord('concept', entry)),
    ...problems.map((entry) => makeRecord('problem', entry)),
    ...contests.map((entry) => makeRecord('contest', entry)),
  ];
  if (!process.env.VITEST) {
    const repoRoot = path.resolve(process.cwd(), '..');
    for (const record of records) assertPublicRepositoryFile(record.sourcePath, repoRoot);
  }
  const byKey = new Map(records.map((record) => [record.key, record]));
  for (const record of records) {
    for (const key of record.relatedKeys) {
      const target = byKey.get(key);
      if (!target) throw new Error(`${record.sourcePath} links to unknown public note ${key}`);
      target.backlinkKeys.push(record.key);
    }
  }
  for (const record of records) record.backlinkKeys.sort();
  return records.sort((a, b) => b.updated.localeCompare(a.updated) || a.title.localeCompare(b.title, 'ko'));
}
export async function getConcepts(): Promise<PublicRecord[]> { return (await getRecords()).filter((record) => record.kind === 'concept'); }
export async function getProblems(): Promise<PublicRecord[]> { return (await getRecords()).filter((record) => record.kind === 'problem'); }
export async function getContests(): Promise<PublicRecord[]> { return (await getRecords()).filter((record) => record.kind === 'contest'); }
export function areasFor(records: PublicRecord[]): AreaInfo[] { return [...new Set(records.filter((record) => record.kind === 'concept').map((record) => record.area!))].map(areaInfo); }

export function relatedRecords(record: PublicRecord, records: PublicRecord[]): PublicRecord[] {
  const keys = new Set([...record.relatedKeys, ...record.backlinkKeys]);
  return records.filter((candidate) => keys.has(candidate.key));
}

export async function readProblemSolution(record: PublicRecord, repoRoot = path.resolve(process.cwd(), '..')): Promise<{ source: string; relative: string }> {
  if (record.kind !== 'problem' || !record.solution) throw new Error(`${record.sourcePath} has no solution`);
  const note = assertPublicRepositoryFile(record.sourcePath, repoRoot);
  const candidate = path.resolve(path.dirname(note), decodeURIComponent(record.solution));
  const relative = path.relative(path.resolve(repoRoot), candidate);
  const [platform] = relative.split(path.sep);
  if (path.isAbsolute(relative) || relative.startsWith('..') || !PLATFORMS.some((item) => item.id === platform) || path.extname(candidate).toLowerCase() !== '.py') {
    throw new Error(`Invalid solution path for ${record.sourcePath}: ${record.solution}`);
  }
  const safe = assertPublicRepositoryFile(relative, repoRoot);
  return { source: await readFile(safe, 'utf8'), relative: relative.split(path.sep).join('/') };
}
