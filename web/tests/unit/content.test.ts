import { describe, expect, it } from 'vitest';
import { setMockCollections } from './astro-content.mock';
import { extractSummary, getRecords, normalizeDate } from '../../src/lib/content';

const common = { updated:'2026-09-20', tags:['test'] };
describe('record registry', () => {
  it('extracts summaries, validates dates, and derives cross-kind links and backlinks', async () => {
    expect(extractSummary('## 핵심 요약\n\n첫 요약.\n\n## 개념 정리\n\n본문')).toBe('첫 요약.');
    expect(extractSummary('## 핵심 요약\n\n시간은 $O(n)$이다.')).toBe('시간은 O(n)이다.');
    expect(normalizeDate('2026-09-20')).toBe('2026-09-20');
    expect(() => normalizeDate('2026-02-30')).toThrow(/Invalid updated/);
    setMockCollections({
      knowledge:[{ id:'new-area/topic', collection:'knowledge', data:{...common,title:'새 분야'}, body:'## 핵심 요약\n\n새 분야도 허용한다.' },{ id:'graphs/bfs', collection:'knowledge', data:{...common,title:'BFS'}, body:'## 핵심 요약\n\n너비 우선 탐색.\n\n[문제][p]\n\n[p]: ../../leetcode/easy/1422.maximum-score-after-splitting-a-string.md' }],
      problems:[{ id:'leetcode/easy/1422.maximum-score-after-splitting-a-string', collection:'problems', data:{...common,title:'점수',url:'https://leetcode.com/problems/example/',solution:'1422.maximum-score-after-splitting-a-string.py'}, body:'자유 형식 문제 요약.\n\n[개념](../../knowledge/graphs/bfs.md)' }],
      contests:[],
    });
    const records=await getRecords();
    const concept=records.find((record)=>record.id==='graphs/bfs')!;
    const problem=records.find((record)=>record.kind==='problem')!;
    expect(concept.relatedKeys).toEqual([problem.key]);
    expect(concept.backlinkKeys).toEqual([problem.key]);
    expect(problem.relatedKeys).toEqual([concept.key]);
    expect(problem.backlinkKeys).toEqual([concept.key]);
    expect(problem.summary).toBe('자유 형식 문제 요약.');
    expect(records.find((record)=>record.id==='new-area/topic')?.area).toBe('new-area');
  });
});
