import { expect, test } from '@playwright/test';
import { readFileSync, readdirSync } from 'node:fs';
const origin='http://127.0.0.1:4321';
const base=`/${(process.env.SITE_BASE||'/algorithm-solutions/').split('/').filter(Boolean).join('/')}/`;
const url=(pathname:string)=>`${origin}${base}${pathname.replace(/^\/+/, '')}`;

test('desktop and mobile navigation expose all libraries and preserve theme', async ({page}) => {
  await page.goto(url('/')); await expect(page.getByRole('heading',{level:1})).toContainText('한 문제의 풀이에서');
  if((page.viewportSize()?.width??1000)<760){await page.locator('.mobile-nav summary').click();await expect(page.locator('.mobile-nav[open] a')).toHaveCount(5);}else await expect(page.locator('.desktop-nav a')).toHaveCount(5);
  await page.evaluate(()=>localStorage.clear()); await page.getByRole('button',{name:'색상 테마 변경'}).click(); const theme=await page.locator('html').getAttribute('data-theme'); await page.reload(); await expect(page.locator('html')).toHaveAttribute('data-theme',theme!);
});

test('renders all seeded records, dotted problem routes, source code and graceful empty contests', async ({page}) => {
  await page.goto(url('/knowledge/')); expect(await page.locator('.record-card').count()).toBeGreaterThanOrEqual(5);
  await page.goto(url('/problems/')); expect(await page.locator('.record-card').count()).toBeGreaterThanOrEqual(3);
  const href=await page.locator('.record-card h3 a[href*="1422.maximum-score-after-splitting-a-string"]').getAttribute('href'); expect(href).toMatch(/\/problems\/leetcode\/easy\/1422\.[^/]+\/$/u); await page.goto(`${origin}${href}`); await expect(page.locator('.solution-code pre code')).toBeVisible(); await expect(page.locator('a',{hasText:'문제 원문'})).toHaveAttribute('href',/^https:\/\//u);
  await page.goto(url('/problems/leetcode/easy/1422.maximum-score-after-splitting-a-string/')); expect(await page.locator('.solution-code code').textContent()).toBe(readFileSync('../leetcode/easy/1422.maximum-score-after-splitting-a-string.py','utf8'));
  const contestCount=readdirSync('../contests').filter((name)=>name.endsWith('.md')&&!['README.md','template.md'].includes(name)).length;
  await page.goto(url('/contests/'));
  if(contestCount===0) await expect(page.getByText('아직 공개한 대회 복기가 없습니다.')).toBeVisible();
  else await expect(page.locator('.record-card')).toHaveCount(contestCount);
});

test('combined search and URL-persisted filters work', async ({page}) => {
  await page.goto(url('/search/')); await page.getByLabel('종류').selectOption('concept'); await page.getByLabel('분야').selectOption('graphs'); await expect(page).toHaveURL(/type=concept.*area=graphs|area=graphs.*type=concept/u);
  const visibleCards=page.locator('#record-results>[data-record-key]:not([hidden])');
  expect(await visibleCards.count()).toBeGreaterThanOrEqual(2);
  for(const key of await visibleCards.evaluateAll((items)=>items.map((item)=>item.getAttribute('data-record-key')))) expect(key).toMatch(/^concept:graphs\//u);
  await expect(page.locator('#record-results>[data-record-key="concept:search/binary-search"]')).toBeHidden();
  await page.getByLabel('검색어').fill('BFS'); await page.getByRole('button',{name:/검색/}).click(); await expect(page.locator('.search-result').first()).toBeVisible({timeout:15000}); await expect(page.getByLabel('정렬', { exact: true })).toBeDisabled();
  await page.goto(url('/search/?type=problem&platform=leetcode&sort=title')); await expect(page.getByLabel('플랫폼')).toHaveValue('leetcode'); const titles=await page.locator('#record-results>[data-record-key]:not([hidden]) h3').allTextContents(); expect(titles).toEqual([...titles].sort((a,b)=>a.localeCompare(b,'ko')));
});

test('math, fenced code, internal links and JavaScript-free reading remain available', async ({page,browser}) => {
  await page.goto(url('/knowledge/graphs/bfs/')); await expect(page.locator('.prose pre code').first()).toBeVisible(); await expect(page.locator('.public-article a[href*="/problems/"]').first()).toBeVisible();
  const katexCount=await page.locator('.katex').count(); expect(katexCount).toBeGreaterThan(0);
  const context=await browser.newContext({javaScriptEnabled:false}); const noJs=await context.newPage(); await noJs.goto(url('/search/')); expect(await noJs.locator('.record-card').count()).toBeGreaterThanOrEqual(8); const first= noJs.locator('.record-card h3 a').first(); await first.click(); await expect(noJs.getByRole('heading',{level:1})).toHaveCount(1); await context.close();
});
