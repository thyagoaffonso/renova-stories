# renova-stories

Assets e automacao de publicacao organica (Instagram + Facebook) da Renova do Brasil Assessoria.

- `agosto/`, `setembro/` : PNGs renderizados (stories 1080x1920 e slides de carrossel 1080x1350) por dia.
- `dados_agosto.json`, `dados_setembro.json`, `dados_renova.json` : mapa data -> URLs raw + legenda. O workflow N8N le `dados_renova.json`.
- `src/` : motores de render (Pillow) e conteudo.
  - `renova_render.py` : tema visual Renova (azul #0F5CA8 / #08325C, dourado #C08A3C, Segoe UI Black + corpo humanista), layouts de story, carrossel, foto e interacao.
  - `conteudo_agosto.py` : copy de agosto + QA promessa x quantidade.
  - `render_mes.py` : renderiza um mes para dentro do repo e gera o JSON.
  - `publish_code.js` : no de Code do N8N (polling status_code FINISHED antes de publicar; FB por crosspost).

Publicacao: workflow N8N "Renova Publicacoes (Stories + Carrossel)", schedule 09:00 America/Sao_Paulo.
IG Business Account @renovadobrasilassessoria = 17841425065973861. Facebook por crosspost do IG.
