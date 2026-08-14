// RENOVA - publicacao diaria de Stories + Carrossel (feed) no Instagram.
// Facebook vem por CROSSPOST automatico do IG (fbPageToken vazio = so IG).
// Le a config do no Config e o conteudo do dia de dados_renova.json (GitHub raw).
// Polling status_code ate FINISHED antes de cada media_publish (evita o 400 de race condition).

const cfg = $('Config').first().json;
const token   = cfg.metaToken;
const ig      = cfg.igUserId;
const GV      = cfg.graphVersion || 'v21.0';
const dataUrl = cfg.dataUrl;
const fbToken = (cfg.fbPageToken || '').trim();   // vazio = crosspost
const fbPage  = (cfg.fbPageId || '').trim();

const http = this.helpers.httpRequest;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const asObj = (x) => (typeof x === 'string' ? JSON.parse(x) : x);

// data de hoje em America/Sao_Paulo (YYYY-MM-DD)
const today = new Intl.DateTimeFormat('en-CA', {
  timeZone: 'America/Sao_Paulo', year: 'numeric', month: '2-digit', day: '2-digit',
}).format(new Date());

const data = asObj(await http({ method: 'GET', url: dataUrl + '?t=' + Date.now() }));
const day = data[today];
if (!day) {
  return [{ json: { status: 'sem conteudo para hoje', today } }];
}

async function createContainer(params) {
  const res = await http({
    method: 'POST',
    url: `https://graph.facebook.com/${GV}/${ig}/media`,
    qs: { ...params, access_token: token }, json: true,
  });
  return asObj(res);
}
async function pollFinished(cid, label) {
  for (let i = 0; i < 30; i++) {
    const st = asObj(await http({
      method: 'GET', url: `https://graph.facebook.com/${GV}/${cid}`,
      qs: { fields: 'status_code', access_token: token }, json: true,
    }));
    if (st.status_code === 'FINISHED') return true;
    if (st.status_code === 'ERROR' || st.status_code === 'EXPIRED') {
      throw new Error(`${label} container ${cid} -> ${st.status_code}`);
    }
    await sleep(4000);
  }
  throw new Error(`${label} container ${cid} -> TIMEOUT`);
}
async function publish(cid) {
  const res = await http({
    method: 'POST', url: `https://graph.facebook.com/${GV}/${ig}/media_publish`,
    qs: { creation_id: cid, access_token: token }, json: true,
  });
  return asObj(res);
}

const out = { today, stories: [], carrossel: null };

// ---- STORIES (um container por quadro) ----
for (const url of (day.stories || [])) {
  const c = await createContainer({ media_type: 'STORIES', image_url: url });
  if (!c.id) throw new Error('story container falhou: ' + JSON.stringify(c));
  await pollFinished(c.id, 'story');
  const p = await publish(c.id);
  out.stories.push(p.id || p);
  await sleep(2000);
}

// ---- CARROSSEL de feed (nos dias com carrossel) ----
if (day.carrossel) {
  const kids = [];
  for (const url of day.carrossel.children) {
    const c = await createContainer({ is_carousel_item: 'true', image_url: url });
    if (!c.id) throw new Error('carrossel filho falhou: ' + JSON.stringify(c));
    await pollFinished(c.id, 'carrossel-filho');
    kids.push(c.id);
  }
  const parent = await createContainer({
    media_type: 'CAROUSEL', children: kids.join(','), caption: day.carrossel.legenda,
  });
  if (!parent.id) throw new Error('carrossel pai falhou: ' + JSON.stringify(parent));
  await pollFinished(parent.id, 'carrossel');
  const p = await publish(parent.id);
  out.carrossel = p.id || p;
}

// ---- FACEBOOK ----
// fbToken vazio de proposito: o Facebook (Pagina Renova) recebe por CROSSPOST automatico do IG,
// ativado em IG > Compartilhamento em outros apps > Facebook. Se um dia houver token de Pagina,
// da para publicar no feed do FB aqui, guardado por if (fbPage && fbToken).
out.facebook = (fbPage && fbToken) ? 'via-token' : 'via-crosspost';

return [{ json: out }];
