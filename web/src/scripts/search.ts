type Kind = 'concept' | 'problem' | 'contest';
type RecordData = { key:string; kind:Kind; id:string; title:string; updated:string; tags:string[]; area?:string; platform?:string; summary:string; url:string };
type SearchData = { url:string; excerpt:string };
type Pagefind = { options:(options:{baseUrl:string})=>Promise<void>; search:(query:string)=>Promise<{results:{data:()=>Promise<SearchData>}[]}> };
const payload = JSON.parse(document.querySelector('#record-data')!.textContent!) as { records:RecordData[]; base:string };
const { records, base } = payload;
const form = document.querySelector<HTMLFormElement>('#library-form')!;
const field = <T extends HTMLInputElement | HTMLSelectElement>(name:string) => form.elements.namedItem(name) as T;
const query = field<HTMLInputElement>('q');
const type = field<HTMLSelectElement>('type');
const area = field<HTMLSelectElement>('area');
const platform = field<HTMLSelectElement>('platform');
const tag = field<HTMLSelectElement>('tag');
const sort = field<HTMLSelectElement>('sort');
const cards = document.querySelector<HTMLElement>('#record-results')!;
const results = document.querySelector<HTMLElement>('#search-results')!;
const status = document.querySelector<HTMLElement>('#result-status')!;
const empty = document.querySelector<HTMLElement>('#empty-results')!;
let generation = 0;
let pagefind:Promise<Pagefind>|undefined;
const matches = (record:RecordData) => (!type.value || record.kind === type.value) && (!area.value || record.area === area.value) && (!platform.value || record.platform === platform.value) && (!tag.value || record.tags.includes(tag.value));
function readState() { const params = new URLSearchParams(location.search); query.value=params.get('q')||''; type.value=params.get('type')||''; area.value=params.get('area')||''; platform.value=params.get('platform')||''; tag.value=params.get('tag')||''; sort.value=params.get('sort')==='title'?'title':'updated'; }
function writeState() { const params=new URLSearchParams(); for(const input of [query,type,area,platform,tag,sort]) if(input.value && !(input===sort&&input.value==='updated')) params.set(input.name,input.value.trim()); history.pushState(null,'',`${location.pathname}${params.size?`?${params}`:''}`); }
function safeExcerpt(html:string):DocumentFragment { const template=document.createElement('template'); template.innerHTML=html; const fragment=document.createDocumentFragment(); const append=(node:Node,parent:Node) => { if(node.nodeType===Node.TEXT_NODE) parent.appendChild(document.createTextNode(node.textContent||'')); else if(node instanceof Element&&node.tagName==='MARK'){const mark=document.createElement('mark');mark.textContent=node.textContent;parent.appendChild(mark);}else node.childNodes.forEach((child)=>append(child,parent)); }; template.content.childNodes.forEach((node)=>append(node,fragment)); return fragment; }
function meta(record:RecordData):string { const typeLabel={concept:'개념',problem:'문제',contest:'대회'}[record.kind]; return `${typeLabel} · ${record.area||record.platform||'복기'} · ${record.updated}`; }
async function update() {
  const current=++generation; const text=query.value.trim(); empty.hidden=true; results.replaceChildren(); cards.hidden=Boolean(text); results.hidden=!text; sort.disabled=Boolean(text);
  if(!text){ const sorted=[...records].sort((a,b)=>(sort.value==='title'?0:b.updated.localeCompare(a.updated))||a.title.localeCompare(b.title,'ko')); let count=0; for(const record of sorted){ const card=cards.querySelector<HTMLElement>(`[data-record-key="${CSS.escape(record.key)}"]`)!; card.hidden=!matches(record); if(!card.hidden) count++; cards.append(card); } empty.hidden=count>0; status.textContent=`${count}개의 문서`; return; }
  status.textContent='본문에서 검색하고 있습니다…';
  try { pagefind??=(import(/* @vite-ignore */ `${base}pagefind/pagefind.js`) as Promise<Pagefind>).then(async(engine)=>{await engine.options({baseUrl:base});return engine;}); const response=await(await pagefind).search(text); const found=await Promise.all(response.results.map((result)=>result.data())); if(current!==generation)return; let count=0; for(const data of found){ const pathname=new URL(data.url,location.origin).pathname; const record=records.find((item)=>decodeURI(item.url)===decodeURI(pathname)); if(!record||!matches(record))continue; count++; const article=document.createElement('article');article.className='search-result';const metadata=document.createElement('p');metadata.className='card-meta';metadata.textContent=meta(record);const h3=document.createElement('h3');const link=document.createElement('a');link.href=record.url;link.textContent=record.title;h3.append(link);const excerpt=document.createElement('p');excerpt.className='search-excerpt';excerpt.append(safeExcerpt(data.excerpt));article.append(metadata,h3,excerpt);results.append(article); } empty.hidden=count>0;status.textContent=`“${text}” 검색 결과 ${count}개 · 관련도순`; }
  catch { if(current!==generation)return;pagefind=undefined;status.textContent=import.meta.env.DEV?'본문 검색은 빌드 후 미리보기에서 사용할 수 있습니다.':'검색을 불러오지 못했습니다. 잠시 후 다시 검색해 주세요.'; }
}
form.addEventListener('submit',(event)=>{event.preventDefault();writeState();void update();});
for(const select of [type,area,platform,tag,sort]) select.addEventListener('change',()=>{writeState();void update();});
window.addEventListener('popstate',()=>{readState();void update();}); readState(); void update();
