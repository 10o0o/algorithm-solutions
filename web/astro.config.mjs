import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import { fileURLToPath } from 'node:url';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import publicMarkdown from './src/lib/markdown';

export default defineConfig({
  output: 'static',
  site: 'https://10o0o.github.io',
  base: process.env.SITE_BASE || '/algorithm-solutions/',
  trailingSlash: 'always',
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath, [publicMarkdown, {
        repoRoot: fileURLToPath(new URL('../', import.meta.url)),
        base: process.env.SITE_BASE || '/algorithm-solutions/',
      }]],
      rehypePlugins: [rehypeKatex],
      shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' } },
    }),
  },
});
