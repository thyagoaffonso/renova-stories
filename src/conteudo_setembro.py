# -*- coding: utf-8 -*-
"""
Conteudo RENOVA - SETEMBRO 2026 (01 a 30). Texto final COM acentuacao, sem travessao.
Calendario do Thyago: "Setembro da Gestao Condominial Eficiente".
Stories diarios (3 a 5 quadros) + 9 carrosseis de feed (ter/qui: 01,03,08,10,15,17,22,24,29).
Interacao = so ARTE (a API nao poe sticker nativo); CTA puxa resposta no direct/comentario.
Rosto misto: foto da lideranca no institucional, bastidores e prova social.
Feriado 07/09 (Independencia) com tema institucional proprio.
"""

WPP = "Chamar no WhatsApp"
NOTE = "diagnóstico gratuito da sua gestão"

def gancho(t, sub=None, kicker="SETEMBRO DA GESTÃO EFICIENTE", photo=None, focus=0.28):
    d = {"role": "gancho", "title": t}
    if sub: d["sub"] = sub
    if kicker: d["kicker"] = kicker
    if photo: d["photo"] = photo; d["focus"] = focus
    return d

def ponto(num, t, body):
    return {"role": "ponto", "num": num, "title": t, "body": body}

def interacao(t, options, note="responda aqui no direct ou nos comentários", kicker="RESPONDA"):
    return {"role": "interacao", "title": t, "options": options, "note": note, "kicker": kicker}

def cta(t, sub=None, photo=None, focus=0.22, label=WPP):
    d = {"role": "cta", "title": t, "cta": label, "note": NOTE, "kicker": "RENOVA DO BRASIL"}
    if sub: d["sub"] = sub
    if photo: d["photo"] = photo; d["focus"] = focus
    return d

def capa(t, sub=None, kicker="PARA SÍNDICOS"):
    d = {"role": "capa", "title": t, "kicker": kicker}
    if sub: d["sub"] = sub
    return d

def slide(num, t, body):
    return {"role": "slide", "num": num, "title": t, "body": body}

def fecho(t, sub="Peça o diagnóstico gratuito da sua gestão.", kicker="RENOVA DO BRASIL"):
    return {"role": "fecho", "title": t, "sub": sub, "cta": WPP, "kicker": kicker}

SETEMBRO = {}

# 01 ter - Abertura + enquete (carrossel 7 sinais)
SETEMBRO["2026-09-01"] = {"stories": [
    gancho("Setembro da Gestão Condominial Eficiente começa hoje.",
           "Um mês inteiro mostrando como sair do improviso."),
    interacao("Qual é hoje o maior problema do seu condomínio?",
              ["Financeiro e inadimplência", "Manutenção", "Comunicação", "Conflitos entre moradores"],
              note="responda e durante o mês mostramos como resolver cada um"),
    cta("Escolha o seu e a gente te mostra o caminho.",
        "Ou já chame no WhatsApp e peça o diagnóstico."),
], "carrossel": {
    "legenda": ("7 sinais de que o seu condomínio precisa de apoio administrativo. Marque quantos você "
                "reconhece e salve para a próxima reunião do conselho. Chame a Renova no WhatsApp e "
                "peça o diagnóstico gratuito da sua gestão.\n\n#sindico #condominio #assessoriacondominial #florianopolis"),
    "slides": [
        capa("7 sinais de que o seu condomínio precisa de apoio administrativo", "Marque quantos você reconhece."),
        slide(1, "O síndico faz tudo sozinho", "Cobrança, fornecedor, documento e morador, tudo passa por uma pessoa só."),
        slide(2, "Documento ninguém acha", "Contrato, ata e convenção espalhados, sem um lugar único e organizado."),
        slide(3, "A inadimplência só cresce", "Sem régua de cobrança, o caixa aperta e o rateio pesa em quem paga em dia."),
        slide(4, "Decisão fica só na conversa", "Nada é registrado. Quando dá problema, ninguém sabe o que foi combinado."),
        slide(5, "Toda assembleia é no susto", "Convocação em cima da hora, pauta improvisada e discussão sem preparo."),
        slide(6, "Fornecedor sem controle", "Contrato vencido, orçamento sem comparação e serviço sem acompanhamento."),
        slide(7, "Se o síndico sai, tudo para", "A gestão depende da cabeça de uma pessoa, não de um processo."),
        fecho("Marcou dois ou mais? A Renova organiza isso com você."),
    ]}}

# 02 qua - Dor: sindico nao precisa fazer tudo sozinho
SETEMBRO["2026-09-02"] = {"stories": [
    gancho("O síndico não precisa fazer tudo sozinho.", kicker="IDENTIFICAÇÃO"),
    ponto(1, "Veja o que costuma sobrecarregar", "Cobrança, fornecedor, documento, morador e prestação de contas. Tudo ao mesmo tempo."),
    cta("Seu síndico está administrando ou só apagando incêndio?",
        "A Renova assume a estrutura para ele decidir com calma."),
]}

# 03 qui - Educacao: 5 sinais desorganizacao (carrossel custo invisivel)
SETEMBRO["2026-09-03"] = {"stories": [
    gancho("A desorganização administrativa sempre dá sinais.", kicker="AUTORIDADE"),
    ponto(1, "Reconhece algum destes?", "Boleto atrasado, contrato vencido, documento espalhado, sem orçamento e sem controle de chamado."),
    cta("Quantos desses existem no seu condomínio?",
        "Veja no post de hoje o custo invisível da desorganização."),
], "carrossel": {
    "legenda": ("O custo invisível da desorganização condominial. O que não aparece na planilha, mas "
                "sai caro todo mês. Salve e compartilhe com o seu síndico. Quer organizar isso de "
                "verdade? Chame a Renova no WhatsApp.\n\n#gestaocondominial #sindico #condominio #florianopolis"),
    "slides": [
        capa("O custo invisível da desorganização condominial", "O que não aparece na planilha e sai caro."),
        slide(1, "Tempo perdido procurando documento", "Cada hora atrás de um contrato é uma hora que some da gestão."),
        slide(2, "Retrabalho que ninguém contabiliza", "A mesma demanda resolvida duas vezes porque nada ficou registrado."),
        slide(3, "Contrato renovado sem negociar", "Sem acompanhamento, o valor sobe no automático, ano após ano."),
        slide(4, "Multa e emergência evitáveis", "Manutenção que virou urgência custa muito mais do que a prevenção."),
        slide(5, "Confiança do morador desgastada", "Desorganização vira desconfiança, e desconfiança vira assembleia tensa."),
        fecho("A Renova transforma isso em rotina com registro."),
    ]}}

# 04 sex - Bastidores (foto)
SETEMBRO["2026-09-04"] = {"stories": [
    gancho("Um dia dentro da Renova.", kicker="BASTIDORES", photo="EDF_8969-2.jpg", focus=0.20),
    ponto(1, "Demanda que entra vira tarefa com dono", "Cada solicitação recebe protocolo, prazo e responsável. Nada se perde no grupo."),
    cta("É assim que a gente transforma pedido em resultado.",
        photo="EDF_8827.jpg", focus=0.20),
]}

# 05 sab - Verdadeiro ou falso (interacao)
SETEMBRO["2026-09-05"] = {"stories": [
    gancho("Verdadeiro ou falso sobre condomínio?", kicker="TESTE RÁPIDO"),
    interacao("O síndico precisa guardar todos os documentos por conta própria?",
              ["Verdadeiro", "Falso"], note="responda e amanhã a gente explica"),
    interacao("Toda despesa precisa ser aprovada em assembleia?",
              ["Verdadeiro", "Falso"], note="envie a sua dúvida para respondermos"),
    cta("Ficou em dúvida em alguma? A gente esclarece.",
        "Chame no WhatsApp e tire as suas dúvidas de gestão."),
]}

# 06 dom - Checklist preventivo (educacao)
SETEMBRO["2026-09-06"] = {"stories": [
    gancho("Checklist preventivo para a semana do seu condomínio.", kicker="AUTORIDADE"),
    ponto(1, "Antes de segunda, confira", "Contas a vencer, chamados pendentes, contratos a renovar, manutenção e comunicados."),
    cta("Salve este checklist e envie para o seu síndico.",
        "Quer esse controle todo mês? A Renova cuida disso."),
]}

# 07 seg - Independencia (institucional, feriado, foto)
SETEMBRO["2026-09-07"] = {"stories": [
    gancho("Independência também é ter uma gestão que não depende de improviso.",
           kicker="7 DE SETEMBRO", photo="EDF_8805.jpg", focus=0.18),
    ponto(1, "Planejamento, transparência e responsabilidade", "Um condomínio organizado depende menos de sorte e mais de método."),
    cta("Que o seu condomínio seja livre do improviso.",
        photo="EDF_8815.jpg", focus=0.16),
]}

# 08 ter - Planejamento financeiro (carrossel 5 despesas)
SETEMBRO["2026-09-08"] = {"stories": [
    gancho("Quanto custa a falta de planejamento no condomínio?", kicker="AUTORIDADE"),
    ponto(1, "O improviso tem preço", "Manutenção virou emergência, multa por atraso e contrato renovado sem negociar."),
    cta("A economia começa antes da despesa acontecer.",
        "Veja no post de hoje 5 despesas que sobem por falta de planejamento."),
], "carrossel": {
    "legenda": ("5 despesas que aumentam por falta de planejamento no condomínio. O que dá para "
                "evitar antes de virar conta alta. Salve e mostre na próxima reunião. Chame a Renova "
                "no WhatsApp e peça o diagnóstico gratuito.\n\n#financeirocondominial #sindico #condominio #florianopolis"),
    "slides": [
        capa("5 despesas que aumentam por falta de planejamento", "O que dá para evitar antes de virar conta alta."),
        slide(1, "Manutenção que virou emergência", "O reparo adiado custa muito mais quando quebra de vez."),
        slide(2, "Multa e juros por atraso", "Conta paga fora do prazo por falta de controle vira dinheiro jogado fora."),
        slide(3, "Contrato renovado sem comparar", "Sem cotação, o valor sobe todo ano no piloto automático."),
        slide(4, "Compra sem cotação", "Comprar no aperto, do primeiro fornecedor, sempre sai mais caro."),
        slide(5, "Inadimplência sem cobrança", "O que não é cobrado com método vira rombo que todo mundo paga."),
        fecho("A Renova planeja e acompanha para o caixa respirar."),
    ]}}

# 09 qua - Dia do Administrador (institucional/autoridade)
SETEMBRO["2026-09-09"] = {"stories": [
    gancho("Hoje é o Dia do Administrador.", kicker="INSTITUCIONAL"),
    ponto(1, "Condomínio também é gestão", "Precisa de processo, controle e planejamento, igual a qualquer empresa séria."),
    cta("Parabéns a quem transforma problema em gestão.",
        "A Renova leva administração profissional para o seu condomínio."),
]}

# 10 qui - Prestacao de contas (carrossel)
SETEMBRO["2026-09-10"] = {"stories": [
    gancho("Prestação de contas que o morador realmente entende.", kicker="AUTORIDADE"),
    ponto(1, "Mostrar número não é explicar", "O morador precisa entender receita, despesa, saldo e a decisão por trás de cada gasto."),
    cta("Você entende a prestação de contas do seu condomínio?",
        "Veja no post de hoje o que ela precisa ter."),
], "carrossel": {
    "legenda": ("Prestação de contas: o que todo morador precisa conseguir entender. Transparência que "
                "o síndico apresenta de cabeça erguida. Salve para a próxima assembleia. Chame a Renova "
                "no WhatsApp.\n\n#prestacaodecontas #condominio #sindico #florianopolis"),
    "slides": [
        capa("Prestação de contas: o que todo morador precisa entender", "Transparência que reduz conflito."),
        slide(1, "De onde veio o dinheiro", "Receita de taxa, fundo de reserva e eventuais extras, tudo claro."),
        slide(2, "Para onde foi", "Despesa por categoria, não uma lista solta de números sem contexto."),
        slide(3, "Qual o saldo", "Quanto entrou, quanto saiu e quanto sobrou, mês a mês."),
        slide(4, "Por que cada decisão", "A explicação por trás do gasto é o que gera confiança."),
        slide(5, "Com documento por trás", "Cada valor com nota e registro, pronto para qualquer conferência."),
        fecho("A Renova organiza a conta e traduz para quem paga o boleto."),
    ]}}

# 11 sex - Caixa de perguntas (interacao)
SETEMBRO["2026-09-11"] = {"stories": [
    gancho("Caixa de perguntas para síndicos.", kicker="RESPONDA"),
    interacao("Qual situação mais toma o seu tempo durante a semana?",
              ["Cobrança e inadimplência", "Fornecedor e manutenção", "Morador e conflito", "Documento e burocracia"],
              note="responda e a gente pode transformar em conteúdo"),
    cta("Manda a sua. A gente responde e ajuda.",
        "Ou chame no WhatsApp e resolva de vez."),
]}

# 12 sab - Antes e depois (prova, foto)
SETEMBRO["2026-09-12"] = {"stories": [
    gancho("Antes e depois administrativo de um condomínio.",
           kicker="PROVA REAL", photo="EDF_8889.jpg", focus=0.20),
    ponto(1, "Antes: pedido perdido no WhatsApp", "Solicitação por mensagem solta, sem prazo, sem dono e sem retorno."),
    ponto(2, "Depois: protocolo com prazo e dono", "Cada demanda registrada, acompanhada e resolvida. O morador vê o andamento."),
    cta("Organização também é resultado.",
        "A Renova instala essa rotina no seu condomínio."),
]}

# 13 dom - Planejamento da semana (educacao)
SETEMBRO["2026-09-13"] = {"stories": [
    gancho("Como planejar a semana do seu condomínio.", kicker="AUTORIDADE"),
    ponto(1, "Eleja tres prioridades", "Defina o que importa, quem é o responsável e o prazo de cada uma."),
    cta("Qual será a prioridade do seu condomínio nesta semana?",
        "A Renova ajuda a definir e a acompanhar."),
]}

# 14 seg - Inadimplencia (dor + autoridade)
SETEMBRO["2026-09-14"] = {"stories": [
    gancho("Inadimplência é problema financeiro e administrativo.", kicker="AUTORIDADE"),
    ponto(1, "Sem acompanhamento, o rombo cresce", "Falta de cobrança com método prejudica caixa, manutenção e planejamento inteiro."),
    cta("Seu condomínio acompanha a inadimplência todo mês?",
        "A Renova monta a régua de cobrança e protege quem paga em dia."),
]}

# 15 ter - Dia do Cliente (carrossel atendimento)
SETEMBRO["2026-09-15"] = {"stories": [
    gancho("Dia do Cliente: ouvir também é administrar.", kicker="IDENTIFICAÇÃO"),
    ponto(1, "Morador não é só pagador de boleto", "Ele precisa de comunicação clara e de retorno quando faz um pedido."),
    cta("O morador do seu condomínio se sente ouvido?",
        "Veja no post de hoje como o atendimento reduz conflito."),
], "carrossel": {
    "legenda": ("Atendimento eficiente reduz conflitos no condomínio. Como responder bem transforma a "
                "relação com o morador. Salve e compartilhe com quem atende o seu condomínio. Chame a "
                "Renova no WhatsApp.\n\n#atendimento #condominio #sindico #florianopolis"),
    "slides": [
        capa("Atendimento eficiente reduz conflitos no condomínio", "Ouvir bem é administrar."),
        slide(1, "Acolher o pedido", "O morador quer se sentir ouvido antes de qualquer resposta."),
        slide(2, "Registrar a demanda", "O que é registrado não se perde e pode ser cobrado depois."),
        slide(3, "Dar um prazo", "Mesmo sem solução imediata, um prazo claro acalma o morador."),
        slide(4, "Retornar e documentar", "Fechar o ciclo com resposta e registro evita a repetição do problema."),
        fecho("A Renova centraliza e organiza o atendimento do seu condomínio."),
    ]}}

# 16 qua - Reclamacoes sem conflito (autoridade)
SETEMBRO["2026-09-16"] = {"stories": [
    gancho("Como responder reclamações sem criar conflito.", kicker="AUTORIDADE"),
    ponto(1, "Acolher, registrar, verificar", "Escute, anote, apure o que aconteceu antes de responder qualquer coisa."),
    ponto(2, "Responder com prazo e documentar", "Uma resposta com prazo e registro encerra o assunto sem virar briga."),
    cta("Compartilhe com quem atende os moradores.",
        "A Renova assume esse atendimento com método."),
]}

# 17 qui - Fornecedores (carrossel menor preco)
SETEMBRO["2026-09-17"] = {"stories": [
    gancho("Contratar pelo menor preço pode sair muito caro.", kicker="AUTORIDADE"),
    ponto(1, "Preço é um item, não o critério", "Escopo, documento, garantia, prazo e responsabilidade também entram na conta."),
    cta("Preço é um item. Segurança é o conjunto.",
        "Veja no post de hoje o que analisar antes de contratar."),
], "carrossel": {
    "legenda": ("Menor preço ou melhor contratação? Veja o que analisar antes de fechar com um "
                "fornecedor no condomínio. Salve para a próxima cotação. Chame a Renova no WhatsApp.\n\n"
                "#fornecedores #condominio #sindico #florianopolis"),
    "slides": [
        capa("Menor preço ou melhor contratação?", "O que analisar antes de fechar."),
        slide(1, "Escopo do serviço", "O que exatamente está incluso. Barato sem escopo vira caro no meio do caminho."),
        slide(2, "Documento e regularidade", "Certidões, contrato e responsável técnico. Sem isso, o risco é do condomínio."),
        slide(3, "Garantia e prazo", "O que acontece se der problema e em quanto tempo a entrega acontece."),
        slide(4, "Material e responsabilidade", "Qualidade do material e quem responde por falha depois da obra."),
        slide(5, "Reputação e histórico", "Quem já contratou e como foi. Referência vale mais que promessa."),
        fecho("A Renova compara e contrata com critério pelo seu condomínio."),
    ]}}

# 18 sex - Checklist fornecedor (autoridade, isca FORNECEDOR)
SETEMBRO["2026-09-18"] = {"stories": [
    gancho("Como a Renova analisa um fornecedor antes de contratar.", kicker="BASTIDORES"),
    ponto(1, "Um checklist que protege o condomínio", "Orçamento comparado, certidões, contrato, prazo e responsável técnico definido."),
    cta("Quer receber esse checklist?",
        "Envie a palavra FORNECEDOR no direct.", label=WPP),
]}

# 19 sab - Quiz protegido (interacao)
SETEMBRO["2026-09-19"] = {"stories": [
    gancho("Quiz: o seu condomínio está protegido?", kicker="TESTE RÁPIDO"),
    interacao("Quantos destes o seu condomínio mantém em dia?",
              ["Seguro e AVCB", "Manutenção preventiva", "Contratos em dia", "Documentação dos prestadores"],
              note="conte quantos você mantém atualizados"),
    cta("Faltou algum? Isso é risco no nome do síndico.",
        "A Renova coloca tudo isso em ordem."),
]}

# 20 dom - Antes da assembleia (autoridade)
SETEMBRO["2026-09-20"] = {"stories": [
    gancho("O que preparar antes da assembleia.", kicker="AUTORIDADE"),
    ponto(1, "Uma boa assembleia começa antes", "Pauta, documentos, orçamentos, convocação correta e as prováveis dúvidas dos moradores."),
    cta("Assembleia preparada não vira briga.",
        "A Renova organiza e conduz a sua assembleia."),
]}

# 21 seg - Primavera areas comuns (identificacao/educacao)
SETEMBRO["2026-09-21"] = {"stories": [
    gancho("Chegou a primavera. E as áreas comuns, como estão?", kicker="IDENTIFICAÇÃO"),
    ponto(1, "Estação de renovar", "Jardim, limpeza, áreas externas, iluminação e manutenção preventiva pedem atenção agora."),
    cta("Qual área comum precisa ser renovada no seu condomínio?",
        "A Renova planeja e acompanha a manutenção."),
]}

# 22 ter - Manutencao para o verao (carrossel)
SETEMBRO["2026-09-22"] = {"stories": [
    gancho("Começou a primavera. A manutenção do verão começa agora.", kicker="AUTORIDADE"),
    ponto(1, "Antecipar evita emergência", "Fachada, piscina, jardim, bombas, reservatório e impermeabilização não esperam dezembro."),
    cta("O verão parece distante, mas a manutenção começa hoje.",
        "Veja no post de hoje o que preparar agora."),
], "carrossel": {
    "legenda": ("O verão começa agora para quem administra condomínios. O que preparar na primavera "
                "para não virar emergência no calor. Salve para o seu planejamento. Chame a Renova no "
                "WhatsApp.\n\n#manutencao #condominio #sindico #florianopolis"),
    "slides": [
        capa("O verão começa agora para quem administra condomínios", "O que preparar na primavera."),
        slide(1, "Piscina e reservatórios", "Tratamento, limpeza e laudo em dia antes da alta temporada de uso."),
        slide(2, "Bombas e impermeabilização", "Chuva de verão testa telhado e laje. Prevenir agora sai barato."),
        slide(3, "Jardim e áreas externas", "Poda, irrigação e iluminação para a área comum ficar apresentável."),
        slide(4, "Ar-condicionado e fachada", "Revisão e limpeza antes do pico de calor e de uso."),
        fecho("A Renova monta o calendário de manutenção do seu condomínio."),
    ]}}

# 23 qua - Tempo do sindico (interacao)
SETEMBRO["2026-09-23"] = {"stories": [
    gancho("Quanto tempo o síndico perde com tarefa operacional?", kicker="IDENTIFICAÇÃO"),
    interacao("Quantas horas por semana o seu condomínio consome de você?",
              ["Até 2h", "De 2 a 5h", "De 5 a 10h", "Mais de 10h"],
              note="responda com sinceridade e veja o que dá para delegar"),
    cta("Tempo do síndico também é patrimônio do condomínio.",
        "A Renova assume o operacional para devolver o seu tempo."),
]}

# 24 qui - O que uma assessoria faz (carrossel, foto, isca ASSESSORIA)
SETEMBRO["2026-09-24"] = {"stories": [
    gancho("O que uma assessoria condominial realmente faz?",
           kicker="QUEM É A RENOVA", photo="EDF_8815.jpg", focus=0.18),
    ponto(1, "Muito além de emitir boleto", "Organização, atendimento, acompanhamento, controle, orientação e apoio ao síndico."),
    cta("Quer conhecer a estrutura da Renova?",
        "Envie a palavra ASSESSORIA no direct."),
], "carrossel": {
    "legenda": ("O que uma assessoria condominial faz pelo síndico? Muito além de emitir boleto. Veja "
                "o que a Renova assume no dia a dia do seu condomínio. Chame no WhatsApp e peça o "
                "diagnóstico gratuito.\n\n#assessoriacondominial #sindico #condominio #florianopolis"),
    "slides": [
        capa("O que uma assessoria condominial faz pelo síndico?", "Muito além de emitir boleto."),
        slide(1, "Financeiro e cobrança", "Rateio, pagamentos, régua de inadimplência e prestação de contas clara."),
        slide(2, "Atendimento e comunicação", "Centraliza pedido de morador, com protocolo, prazo e retorno."),
        slide(3, "Assembleias e documentos", "Convoca, prepara, conduz e registra tudo com respaldo."),
        slide(4, "Jurídico e mediação", "Jurídico próprio à disposição e mediação dos conflitos do condomínio."),
        slide(5, "Acompanhamento próximo", "A Renova segue junto mês a mês, não some depois de assinar."),
        fecho("A estrutura que tira o peso das costas do síndico."),
    ]}}

# 25 sex - Comunicacao (autoridade)
SETEMBRO["2026-09-25"] = {"stories": [
    gancho("Comunicação que evita conflito no condomínio.", kicker="AUTORIDADE"),
    ponto(1, "Comunicado ruim gera boato", "Vago, seco e sem informação completa abre espaço para interpretação e briga."),
    ponto(2, "Comunicado claro resolve", "Objetivo, respeitoso e com todas as informações. Menos ruído, menos conflito."),
    cta("Clareza evita interpretação e reduz desgaste.",
        "A Renova cuida da comunicação com os moradores."),
]}

# 26 sab - Mito ou verdade (interacao)
SETEMBRO["2026-09-26"] = {"stories": [
    gancho("Mito ou verdade: a administradora substitui o síndico?", kicker="TESTE RÁPIDO"),
    interacao("O que você acha?", ["É mito", "É verdade"],
              note="responda e veja a explicação no próximo quadro"),
    ponto(1, "É mito", "A assessoria não substitui o síndico. Ela dá estrutura e respaldo para as decisões dele."),
    cta("A boa gestão nasce da parceria.",
        "A Renova trabalha do lado do síndico, não no lugar dele."),
]}

# 27 dom - Fechamento do mes (autoridade)
SETEMBRO["2026-09-27"] = {"stories": [
    gancho("Checklist de fechamento do mês do condomínio.", kicker="AUTORIDADE"),
    ponto(1, "Antes de virar o mês, confira", "Conciliação, contas pagas, inadimplência, contratos, chamados, documentos e relatório."),
    cta("Seu condomínio fecha o mês com controle ou vira a página?",
        "A Renova entrega esse fechamento pronto todo mês."),
]}

# 28 seg - Avaliar administradora (autoridade)
SETEMBRO["2026-09-28"] = {"stories": [
    gancho("Como saber se a sua administradora entrega resultado.", kicker="AUTORIDADE"),
    ponto(1, "Cobre estes critérios", "Prazo de resposta, transparência, organização, relatório, acompanhamento e resolução."),
    cta("Há quanto tempo você não avalia a própria gestão?",
        "Peça um diagnóstico gratuito e compare."),
]}

# 29 ter - Caso pratico (prova, foto) (carrossel 10 perguntas)
SETEMBRO["2026-09-29"] = {"stories": [
    gancho("Do problema ao processo: um caso prático.",
           kicker="PROVA REAL", photo="EDF_8973.jpg", focus=0.22),
    ponto(1, "Antes: tudo pelo WhatsApp do síndico", "Pedido solto, sem prazo e sem dono. O que chegava se perdia no meio da conversa."),
    ponto(2, "Depois: protocolo, prazo e responsável", "A mesma demanda, agora acompanhada até resolver. O morador vê o andamento."),
    cta("A diferença não é receber o pedido. É acompanhar até o fim.",
        "Veja no post 10 perguntas para avaliar a sua gestão."),
], "carrossel": {
    "legenda": ("10 perguntas para avaliar a gestão administrativa do seu condomínio. Responda com "
                "sinceridade e veja onde está o improviso. Se travou em alguma, chame a Renova no "
                "WhatsApp e peça o diagnóstico gratuito.\n\n#gestaocondominial #sindico #condominio #florianopolis"),
    "slides": [
        capa("10 perguntas para avaliar a gestão do seu condomínio", "Responda com sinceridade."),
        slide(1, "Você acha qualquer documento em minutos?", "Ou perde tempo procurando quando precisa?"),
        slide(2, "A inadimplência é acompanhada todo mês?", "Ou só aparece quando o caixa aperta?"),
        slide(3, "As decisões ficam registradas?", "Ou vivem apenas na memória e no grupo?"),
        slide(4, "A prestação de contas é entendível?", "Ou é uma lista de números sem contexto?"),
        slide(5, "Os contratos estão em dia?", "Ou renovam sozinhos, sem ninguém comparar?"),
        slide(6, "O morador recebe retorno?", "Ou o pedido some sem resposta?"),
        slide(7, "A manutenção é preventiva?", "Ou você só age quando quebra?"),
        slide(8, "A assembleia é preparada?", "Ou vira sempre uma surpresa tensa?"),
        slide(9, "Existe respaldo jurídico?", "Ou o risco fica todo no nome do síndico?"),
        slide(10, "Se o síndico sair, o condomínio segue?", "Ou tudo depende da cabeça de uma pessoa?"),
        fecho("Travou em alguma? A Renova organiza isso com você."),
    ]}}

# 30 qua - Encerramento + convite comercial (oferta, foto)
SETEMBRO["2026-09-30"] = {"stories": [
    gancho("Chegamos ao fim do Setembro da Gestão Eficiente.",
           kicker="RENOVA DO BRASIL", photo="EDF_8963.jpg", focus=0.20),
    ponto(1, "O mês inteiro mostrou o mesmo ponto", "Improviso cansa e cobra caro. Estrutura tranquiliza e devolve o seu tempo."),
    cta("Quer começar outubro com uma gestão mais organizada?",
        "Solicite uma apresentação da Renova no WhatsApp.", label=WPP),
]}


def check_promise(data):
    import re
    mapa = {"dois":2,"tres":3,"quatro":4,"cinco":5,"seis":6,"sete":7,"oito":8,"nove":9,"dez":10}
    alertas = 0
    for day, blk in data.items():
        frames = blk.get("stories") or []
        g = next((f for f in frames if f.get("role") == "gancho"), None)
        if g:
            t = g["title"].lower()
            m = re.search(r"\b(\d+)\b", t)
            n = int(m.group(1)) if m else next((v for k, v in mapa.items() if re.search(r"\b"+k+r"\b", t)), None)
            if n and n <= 12:
                pts = [f for f in frames if f.get("role") == "ponto"]
                if len(pts) < n:
                    print(f"  ALERTA {day}: gancho promete {n}, tem {len(pts)} pontos"); alertas += 1
        car = blk.get("carrossel")
        if car:
            m = re.search(r"\b(\d+)\b", car["slides"][0]["title"])
            if m:
                n = int(m.group(1)); nums = [s for s in car["slides"] if s.get("role") == "slide"]
                if len(nums) != n:
                    print(f"  ALERTA {day} carrossel: promete {n}, tem {len(nums)} slides"); alertas += 1
    return alertas


if __name__ == "__main__":
    dias = sorted(SETEMBRO)
    ncar = sum(1 for d in dias if SETEMBRO[d].get("carrossel"))
    nstory = sum(len(SETEMBRO[d]["stories"]) for d in dias)
    print(f"SETEMBRO: {len(dias)} dias ({dias[0]} a {dias[-1]}) | stories frames: {nstory} | carrosseis: {ncar}")
    a = check_promise(SETEMBRO)
    print("QA:", "TUDO CASADO" if a == 0 else f"{a} alertas")
