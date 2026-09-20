let entries: Record<string, unknown[]> = { knowledge: [], problems: [], contests: [] };
export function setMockCollections(value: Record<string, unknown[]>): void { entries = value; }
export async function getCollection(name: string): Promise<unknown[]> { return entries[name] ?? []; }
export type CollectionEntry<T extends string> = { id:string; data:Record<string, unknown>; body?:string; collection:T };
export async function render(): Promise<never> { throw new Error('render is unavailable in unit tests'); }
