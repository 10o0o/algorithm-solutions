import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const updated = z.union([z.string(), z.date()]).transform((value) =>
  value instanceof Date ? value.toISOString().slice(0, 10) : value,
).refine((value) => /^\d{4}-\d{2}-\d{2}$/u.test(value), 'updated must use YYYY-MM-DD');
const common = { title: z.string().min(1), updated, tags: z.array(z.string().min(1)) };

const knowledge = defineCollection({
  loader: glob({ base: '../knowledge', pattern: ['*/*.md', '!**/{README,template}.md'], generateId: ({ entry }) => entry.replace(/\.md$/u, '') }),
  schema: z.object(common),
});
const problems = defineCollection({
  loader: glob({ base: '..', pattern: ['{atcoder,codeforces,leetcode}/**/*.md', '!**/{README,template}.md'], generateId: ({ entry }) => entry.replace(/\.md$/u, '') }),
  schema: z.object({ ...common, url: z.url({ protocol: /^https$/u }), solution: z.string().min(1) }),
});
const contests = defineCollection({
  loader: glob({ base: '../contests', pattern: ['*.md', '!{README,template}.md'], generateId: ({ entry }) => entry.replace(/\.md$/u, '') }),
  schema: z.object({ ...common, url: z.url({ protocol: /^https$/u }) }),
});

export const collections = { knowledge, problems, contests };
