import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import remarkParse from 'remark-parse';
import { unified } from 'unified';
import publicMarkdown from '../../src/lib/markdown';

describe('public Markdown', () => {
  it('rejects raw HTML but leaves code containing HTML alone', async () => {
    const root=await mkdtemp(path.join(os.tmpdir(),'algorithm-md-')); const source=path.join(root,'note.md'); await writeFile(source,'source');
    const transform=(body:string)=>{const processor=unified().use(remarkParse).use(publicMarkdown,{repoRoot:root,base:'/lab'});return processor.run(processor.parse(body),{path:source});};
    try { await expect(transform('<a href="secret">bad</a>')).rejects.toThrow(/Raw HTML/); await expect(transform('`<a href="safe">text</a>`\n\n```html\n<a>code</a>\n```')).resolves.toBeDefined(); }
    finally { await rm(root,{recursive:true,force:true}); }
  });
});
