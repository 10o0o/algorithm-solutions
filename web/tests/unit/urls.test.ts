import { mkdir, mkdtemp, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import { assertPublicRepositoryFile, conceptUrl, problemUrl, resolveContentLink, withBase } from '../../src/lib/urls';

describe('public URLs', () => {
  it('keeps the project base and dotted LeetCode slug', () => {
    expect(withBase('/search/', '/algorithm-solutions')).toBe('/algorithm-solutions/search/');
    expect(conceptUrl('graphs/bfs', '/algorithm-solutions/')).toBe('/algorithm-solutions/knowledge/graphs/bfs/');
    expect(problemUrl('leetcode/easy/1422.maximum-score-after-splitting-a-string', '/algorithm-solutions/')).toBe('/algorithm-solutions/problems/leetcode/easy/1422.maximum-score-after-splitting-a-string/');
    expect(problemUrl('codeforces/4A_Watermelon', '/algorithm-solutions/')).toBe('/algorithm-solutions/problems/codeforces/4A_Watermelon/');
    expect(problemUrl('cses/Range_Update_Queries', '/algorithm-solutions/')).toBe('/algorithm-solutions/problems/cses/Range_Update_Queries/');
  });
});

describe('publication boundary', () => {
  it('maps note links, maps public files to GitHub and rejects private, scratch, outside and symlink targets', async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), 'algorithm-web-'));
    const outside = `${root}-outside.py`;
    try {
      await mkdir(path.join(root, 'knowledge', 'basics'), { recursive:true });
      await mkdir(path.join(root, 'leetcode', 'easy'), { recursive:true });
      await mkdir(path.join(root, 'cses'), { recursive:true });
      await mkdir(path.join(root, 'private'), { recursive:true });
      const source = path.join(root, 'knowledge', 'basics', 'source.md');
      await writeFile(source, '# source\n');
      await writeFile(path.join(root, 'knowledge', 'basics', 'target.md'), '# target\n');
      await writeFile(path.join(root, 'leetcode', 'easy', 'answer.py'), 'print(1)\n');
      await writeFile(path.join(root, 'cses', 'Range_Update_Queries.md'), '# CSES test fixture\n');
      await writeFile(path.join(root, 'main.py'), 'scratch\n');
      await writeFile(path.join(root, 'private', 'secret.md'), 'secret\n');
      await writeFile(outside, 'outside\n');
      await symlink(path.join(root, 'leetcode', 'easy', 'answer.py'), path.join(root, 'knowledge', 'basics', 'answer-link.py'));
      expect(resolveContentLink('./target.md', source, root, '/lab')).toBe('/lab/knowledge/basics/target/');
      expect(resolveContentLink('../../cses/Range_Update_Queries.md', source, root, '/lab')).toBe('/lab/problems/cses/Range_Update_Queries/');
      expect(resolveContentLink('../../leetcode/easy/answer.py', source, root)).toContain('github.com/10o0o/algorithm-solutions/blob/main/leetcode/easy/answer.py');
      expect(resolveContentLink('data:image/png;base64,AAAA', source, root)).toBe('data:image/png;base64,AAAA');
      expect(() => resolveContentLink('../../private/secret.md', source, root)).toThrow(/prohibited/);
      expect(() => resolveContentLink('../../main.py', source, root)).toThrow(/prohibited/);
      expect(() => resolveContentLink(`../../../${path.basename(outside)}`, source, root)).toThrow(/escapes/);
      expect(() => resolveContentLink('./answer-link.py', source, root)).toThrow(/symlinks/);
      expect(() => assertPublicRepositoryFile('knowledge/basics/answer-link.py', root)).toThrow(/symlinks/);
    } finally { await rm(root, { recursive:true, force:true }); await rm(outside, { force:true }); }
  });
});
