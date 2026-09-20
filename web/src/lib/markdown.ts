import type { Definition, Image, ImageReference, Link, Root, RootContent } from 'mdast';
import { toString } from 'mdast-util-to-string';
import type { Plugin } from 'unified';
import { visit } from 'unist-util-visit';
import { resolveContentLink } from './urls';

export interface PublicMarkdownOptions { repoRoot: string; base?: string }
function ignore(node: RootContent): void {
  const data = node.data as { hProperties?: Record<string, unknown> } | undefined;
  node.data = { ...node.data, hProperties: { ...data?.hProperties, 'data-pagefind-ignore': '' } };
}
const publicMarkdown: Plugin<[PublicMarkdownOptions], Root> = ({ repoRoot, base }) => (root, file) => {
  const firstH1 = root.children.findIndex((node) => node.type === 'heading' && node.depth === 1);
  if (firstH1 >= 0) root.children.splice(firstH1, 1);
  for (let index = 0; index < root.children.length; index += 1) {
    const node = root.children[index];
    if (node.type === 'heading' && node.depth === 2 && ['출처', '출처와 연결', '문제별 링크'].includes(toString(node).trim())) {
      for (const item of root.children.slice(index)) {
        if (item !== node && item.type === 'heading' && item.depth === 2) break;
        ignore(item);
      }
    }
  }
  visit(root, 'html', () => { throw new Error('Raw HTML is unsupported in public Markdown'); });
  const definitions = new Set<string>();
  visit(root, (node) => {
    if (node.type === 'imageReference' || !['link', 'image', 'definition'].includes(node.type)) return;
    if (!file.path) throw new Error('Cannot resolve a relative content link without a source file');
    if (node.type === 'definition') definitions.add(node.identifier.toLowerCase());
    (node as Link | Image | Definition).url = resolveContentLink((node as Link | Image | Definition).url, file.path, repoRoot, base);
  });
  visit(root, 'imageReference', (node: ImageReference) => {
    if (!definitions.has(node.identifier.toLowerCase())) throw new Error(`Image reference has no definition: ${node.identifier}`);
  });
};
export default publicMarkdown;
