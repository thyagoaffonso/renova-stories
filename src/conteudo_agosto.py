# -*- coding: utf-8 -*-
"""
Conteudo RENOVA - AGOSTO 2026 (14 a 31). Texto final COM acentuacao.
Stories diarios + 4 carrosseis de feed (18, 20, 25, 27).
Rotacao dos 5 pilares, rosto misto (foto no institucional e prova social),
CTA WhatsApp + diagnostico gratuito. Sem travessao no texto final.
"""

WPP = "Chamar no WhatsApp"
NOTE = "diagnóstico gratuito da sua gestão"

def gancho(t, sub=None, kicker="SÍNDICO, UMA PERGUNTA", photo=None, focus=0.30):
    d = {"role": "gancho", "title": t}
    if sub: d["sub"] = sub
    if kicker: d["kicker"] = kicker
    if photo: d["photo"] = photo; d["focus"] = focus
    return d

def ponto(num, t, body):
    return {"role": "ponto", "num": num, "title": t, "body": body}

def cta(t, sub=None, photo=None, focus=0.24):
    d = {"role": "cta", "title": t, "cta": WPP, "note": NOTE, "kicker": "RENOVA DO BRASIL"}
    if sub: d["sub"] = sub
    if photo: d["photo"] = photo; d["focus"] = focus
    return d

AGOSTO = {}

# 14 sex - Dor
AGOSTO["2026-08-14"] = {"stories": [
    gancho("Ser síndico virou um segundo emprego que ninguém te ensinou a fazer.",
           "E a responsabilidade toda no seu nome."),
    ponto(1, "Assembleia que vira briga", "Reunião tensa, decisão sem registro e o desgaste sobrando para você no dia seguinte."),
    ponto(2, "Inadimplência que não para", "Cobrança sem método, caixa apertado e prestação de contas que tira o seu sono."),
    cta("O problema não é você. É a falta de estrutura.",
        "A Renova assume a gestão do lado do síndico."),
]}

# 15 sab - Educacao
AGOSTO["2026-08-15"] = {"stories": [
    gancho("Você sabe pelo que o síndico responde pessoalmente?", kicker="EDUCAÇÃO CONDOMINIAL"),
    ponto(1, "Prestação de contas irregular", "Número que não fecha vira responsabilidade sua, não do condomínio."),
    ponto(2, "Decisão fora da convenção", "O que passa por cima da assembleia pode ser anulado, e a conta sobra para quem assinou."),
    cta("Síndico bem assessorado decide amparado, não no escuro.",
        "A Renova mantém a gestão dentro da técnica e da lei."),
]}

# 16 dom - Dor
AGOSTO["2026-08-16"] = {"stories": [
    gancho("Domingo à noite e você já pensando no condomínio."),
    ponto(1, "A semana começa e o telefone não para", "Morador, fornecedor, boleto, chamado. Tudo chega em você ao mesmo tempo."),
    cta("Existe um jeito de o condomínio rodar sem depender só de você.",
        "A Renova organiza a rotina para o síndico respirar."),
]}

# 17 seg - Institucional (foto)
AGOSTO["2026-08-17"] = {"stories": [
    gancho("Por trás de uma boa gestão existe gente, não só sistema.",
           kicker="QUEM É A RENOVA", photo="EDF_8963.jpg", focus=0.22),
    ponto(1, "Time próprio à disposição do síndico", "Assessoria, financeiro, jurídico e mediação trabalhando lado a lado com você."),
    cta("Aqui você fala com gente de verdade, não com um gerador de boleto.",
        photo="EDF_8969.jpg", focus=0.20),
]}

# 18 ter - Dor (carrossel)
AGOSTO["2026-08-18"] = {"stories": [
    gancho("Seu condomínio ainda é tocado no improviso?"),
    ponto(1, "Cada mês uma correria diferente", "Sem processo e sem registro, o problema de ontem volta amanhã com outra roupa."),
    cta("Improviso cansa. Estrutura tranquiliza.",
        "Veja no post de hoje os 5 sinais do improviso."),
], "carrossel": {
    "legenda": ("5 sinais de que a gestão do seu condomínio está no improviso. Marque quantos você "
                "reconhece. Se marcou dois ou mais, a Renova do Brasil organiza isso com você. "
                "Chame no WhatsApp e peça o diagnóstico gratuito da sua gestão.\n\n"
                "#sindico #condominio #assessoriacondominial #florianopolis"),
    "slides": [
        {"role":"capa","kicker":"PARA SÍNDICOS","title":"5 sinais de que seu condomínio está no improviso","sub":"Marque quantos você reconhece."},
        {"role":"slide","num":1,"title":"Ninguém acha o documento quando precisa","body":"Contrato, ata, convenção. Tudo espalhado, nada organizado num lugar só."},
        {"role":"slide","num":2,"title":"Decisão importante fica só na conversa","body":"Sem registro e sem ata, quando dá problema é a palavra do morador contra a sua."},
        {"role":"slide","num":3,"title":"A inadimplência cresce e ninguém cobra com método","body":"Sem régua de cobrança, o caixa aperta e o rateio pesa em quem paga em dia."},
        {"role":"slide","num":4,"title":"Toda assembleia é uma surpresa","body":"Convocação em cima da hora, pauta improvisada e decisão no susto."},
        {"role":"slide","num":5,"title":"Se o síndico sai, o condomínio para","body":"Tudo depende da sua cabeça. Nada está em processo, nada está registrado."},
        {"role":"fecho","kicker":"RENOVA DO BRASIL","title":"Marcou dois ou mais? A gente organiza isso com você.","sub":"Peça o diagnóstico gratuito da sua gestão.","cta":WPP},
    ]}}

# 19 qua - Educacao
AGOSTO["2026-08-19"] = {"stories": [
    gancho("Toda despesa do condomínio precisa passar pela assembleia?", kicker="EDUCAÇÃO CONDOMINIAL"),
    ponto(1, "Depende da natureza do gasto", "Despesa ordinária segue o orçamento aprovado. A extraordinária é que exige aprovação."),
    ponto(2, "O risco está em confundir os dois", "Gastar como ordinário o que era extraordinário abre brecha para impugnação."),
    cta("Saber onde termina a sua alçada protege o seu nome.",
        "A Renova orienta cada decisão dentro da convenção."),
]}

# 20 qui - Metodo (carrossel)
AGOSTO["2026-08-20"] = {"stories": [
    gancho("Tem coisa que o síndico faz por não saber que não precisava.", kicker="RESPALDO"),
    ponto(1, "Pagar do próprio bolso despesa do condomínio", "Sem respaldo, vira favor. Com método, vira processo com prazo e responsável."),
    cta("Síndico bem assessorado sabe exatamente onde termina a sua obrigação.",
        "Veja no post de hoje o que você não é obrigado a fazer."),
], "carrossel": {
    "legenda": ("O que o síndico não é obrigado a fazer, e faz por não saber. Salve este post e "
                "compartilhe com quem está à frente do seu condomínio. Quer esse respaldo na prática? "
                "Chame a Renova no WhatsApp e peça o diagnóstico gratuito.\n\n"
                "#sindico #condominio #gestaocondominial #florianopolis"),
    "slides": [
        {"role":"capa","kicker":"PARA SÍNDICOS","title":"O que o síndico NÃO é obrigado a fazer","sub":"E faz por não saber."},
        {"role":"slide","num":1,"title":"Bancar do próprio bolso o que é do condomínio","body":"Adiantar despesa sem processo vira prejuízo seu e dor de cabeça na prestação de contas."},
        {"role":"slide","num":2,"title":"Decidir sozinho o que deveria ir à assembleia","body":"Carregar sozinho uma decisão coletiva é assumir sozinho o risco dela."},
        {"role":"slide","num":3,"title":"Aguentar cobrança de morador sem respaldo","body":"Sem técnica e sem registro, você vira alvo. Com respaldo, a resposta é da estrutura."},
        {"role":"slide","num":4,"title":"Ser o jurídico, o financeiro e o RH ao mesmo tempo","body":"Cada frente pede especialista. Acumular tudo em uma pessoa é onde o erro mora."},
        {"role":"fecho","kicker":"RENOVA DO BRASIL","title":"A Renova mostra onde termina a sua obrigação.","sub":"Peça o diagnóstico gratuito da sua gestão.","cta":WPP},
    ]}}

# 21 sex - Dor
AGOSTO["2026-08-21"] = {"stories": [
    gancho("O grupo do condomínio não para de apitar e todo mundo cobra você."),
    ponto(1, "Você virou o pronto socorro do prédio", "Cano, portão, barulho, boleto. Tudo cai no seu colo, a qualquer hora."),
    cta("Existe estrutura para receber, organizar e resolver o que chega.",
        "A Renova tira o síndico da linha de frente do caos."),
]}

# 22 sab - Prova social (foto)
AGOSTO["2026-08-22"] = {"stories": [
    gancho("Antes, tudo passava pela cabeça de uma pessoa só.",
           kicker="ANTES E DEPOIS", photo="EDF_8889.jpg", focus=0.22),
    ponto(1, "Depois, virou rotina com registro", "Solicitação protocolada, prazo definido e responsável claro. O síndico deixa de ser o gargalo."),
    cta("Organização também é resultado. E o morador sente.",
        photo="EDF_8815.jpg", focus=0.18),
]}

# 23 dom - Dor
AGOSTO["2026-08-23"] = {"stories": [
    gancho("Quanto do seu fim de semana o condomínio já levou este mês?"),
    ponto(1, "Tempo do síndico também é patrimônio", "Cada hora apagando incêndio é uma hora que some da sua vida e do seu trabalho."),
    cta("Dá para delegar o operacional e ficar só com a decisão.",
        "A Renova assume a rotina para devolver o seu tempo."),
]}

# 24 seg - Educacao
AGOSTO["2026-08-24"] = {"stories": [
    gancho("Prestação de contas não é só mostrar número.", kicker="EDUCAÇÃO CONDOMINIAL"),
    ponto(1, "É o morador entender para onde foi o dinheiro", "Receita, despesa, saldo e decisão. Explicados, não só listados."),
    ponto(2, "Conta clara reduz conflito", "Quando o morador entende, ele confia. E a assembleia deixa de virar tribunal."),
    cta("A Renova organiza a conta e traduz para quem paga o boleto.",
        "Transparência que o síndico apresenta de cabeça erguida."),
]}

# 25 ter - Dor (carrossel)
AGOSTO["2026-08-25"] = {"stories": [
    gancho("Você assumiu o cargo de gestor sem nunca ter sido treinado para isso."),
    ponto(1, "E ninguém avisou o tamanho da conta", "Jurídico, financeiro, obra, gente. Tudo virou responsabilidade sua de uma vez."),
    cta("Não precisa dar conta de tudo sozinho.",
        "Veja no post de hoje como a Renova assume a estrutura."),
], "carrossel": {
    "legenda": ("Como a Renova do Brasil assume a estrutura do seu condomínio, na prática. "
                "Diagnóstico, estruturação e acompanhamento, do lado do síndico. "
                "Chame no WhatsApp e peça o diagnóstico gratuito da sua gestão.\n\n"
                "#assessoriacondominial #sindico #condominio #florianopolis"),
    "slides": [
        {"role":"capa","kicker":"MÉTODO RENOVA","title":"Como a Renova assume a estrutura do seu condomínio","sub":"Do lado do síndico, na prática."},
        {"role":"slide","num":1,"title":"Diagnóstico","body":"A gente escuta, olha os números e mapeia onde o condomínio está no improviso."},
        {"role":"slide","num":2,"title":"Estruturação","body":"Processo de cobrança, organização de documentos, rotina de pagamentos e de assembleia."},
        {"role":"slide","num":3,"title":"Acompanhamento","body":"A Renova segue junto mês a mês. O síndico decide amparado, não no escuro."},
        {"role":"slide","num":4,"title":"Respaldo técnico e jurídico","body":"Jurídico próprio à disposição e mediação dos conflitos entre síndico e moradores."},
        {"role":"fecho","kicker":"RENOVA DO BRASIL","title":"A estrutura que tira o peso das costas do síndico.","sub":"Peça o diagnóstico gratuito da sua gestão.","cta":WPP},
    ]}}

# 26 qua - Educacao
AGOSTO["2026-08-26"] = {"stories": [
    gancho("Inadimplência no condomínio: dá para cobrar de qualquer jeito?", kicker="EDUCAÇÃO CONDOMINIAL"),
    ponto(1, "Não. Exposição de devedor gera risco", "Lista no mural ou no grupo pode virar ação por dano moral contra o condomínio."),
    ponto(2, "Cobrança tem método e tem lei", "Notificação, régua e, se preciso, a via judicial. Tudo com registro."),
    cta("A Renova cobra com método e protege o condomínio no processo.",
        "Veja amanhã um antes e depois de gestão organizada."),
]}

# 27 qui - Prova social (foto) (carrossel)
AGOSTO["2026-08-27"] = {"stories": [
    gancho("A inadimplência estava crescendo e ninguém cobrava com método.",
           kicker="ANTES E DEPOIS", photo="EDF_8973.jpg", focus=0.24),
    ponto(1, "Entrou régua de cobrança e registro", "Notificação no prazo, acordo formalizado e caixa voltando a respirar."),
    cta("Cobrar com método protege quem paga em dia.",
        "Veja no post de hoje o que dá para cobrar, e como."),
], "carrossel": {
    "legenda": ("Inadimplência no condomínio: o que dá para cobrar com método, e o que o síndico "
                "não pode fazer sozinho. Salve para a próxima reunião do conselho. "
                "Quer uma régua de cobrança de verdade? Chame a Renova no WhatsApp.\n\n"
                "#inadimplencia #condominio #sindico #florianopolis"),
    "slides": [
        {"role":"capa","kicker":"EDUCAÇÃO CONDOMINIAL","title":"Inadimplência: o que dá para cobrar com método","sub":"E o que o síndico não pode fazer sozinho."},
        {"role":"slide","num":1,"title":"Pode: notificar formalmente","body":"Cobrança por escrito, com prazo e registro. O primeiro passo que sustenta todos os outros."},
        {"role":"slide","num":2,"title":"Pode: cobrar multa e juros da convenção","body":"Dentro do que a convenção e a lei preveem. Nem mais, nem menos."},
        {"role":"slide","num":3,"title":"Não pode: expor o devedor","body":"Nome no mural ou no grupo vira risco de dano moral para o condomínio inteiro."},
        {"role":"slide","num":4,"title":"Não pode: cortar serviço essencial","body":"Suspender água ou uso de área pode ser revertido na justiça e gerar indenização."},
        {"role":"fecho","kicker":"RENOVA DO BRASIL","title":"A Renova monta a régua de cobrança e protege o condomínio.","sub":"Peça o diagnóstico gratuito da sua gestão.","cta":WPP},
    ]}}

# 28 sex - Dor
AGOSTO["2026-08-28"] = {"stories": [
    gancho("Sexta à noite e um vazamento no prédio. Adivinha quem resolve?"),
    ponto(1, "Sem estrutura, urgência sempre sobra para você", "Sem fornecedor de plantão e sem processo, o telefone que toca é o seu."),
    cta("Com a Renova, a emergência tem para quem ligar antes de você.",
        "Estrutura para o síndico parar de apagar incêndio."),
]}

# 29 seg - Metodo
AGOSTO["2026-08-29"] = {"stories": [
    gancho("O que muda quando o condomínio passa a ter processo?", kicker="MÉTODO RENOVA"),
    ponto(1, "A demanda deixa de se perder", "Tudo entra por um canal, com protocolo, prazo e responsável. Nada some no grupo."),
    ponto(2, "A decisão passa a ter histórico", "No mês seguinte, ninguém discute o que já foi resolvido. Fica registrado."),
    cta("Processo não engessa. Processo liberta o síndico.",
        "A Renova instala a rotina e acompanha de perto."),
]}

# 30 dom - Institucional (foto)
AGOSTO["2026-08-30"] = {"stories": [
    gancho("A Renova nasceu para tirar o peso da gestão dos ombros do síndico.",
           kicker="QUEM É A RENOVA", photo="EDF_8805.jpg", focus=0.20),
    ponto(1, "Método, respaldo e acompanhamento próximo", "Em Florianópolis e região, do lado de quem toma a decisão no condomínio."),
    cta("Estrutura de gente que entende de condomínio.",
        photo="EDF_8827.jpg", focus=0.20),
]}

# 31 seg - Dor / virada de mes
AGOSTO["2026-08-31"] = {"stories": [
    gancho("Começar setembro no improviso de novo ou com estrutura?"),
    ponto(1, "O mês vira, os problemas continuam", "Enquanto não muda a estrutura, muda só a data no calendário."),
    cta("Setembro pode ser o mês em que o seu condomínio para de improvisar.",
        "Chame a Renova e peça o diagnóstico gratuito."),
]}


def check_promise(data):
    """QA: se o gancho promete N, exige N pontos; se a capa do carrossel promete N, exige N slides."""
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
            if n:
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
    dias = sorted(AGOSTO)
    ncar = sum(1 for d in dias if AGOSTO[d].get("carrossel"))
    nstory = sum(len(AGOSTO[d]["stories"]) for d in dias)
    print(f"AGOSTO: {len(dias)} dias | stories frames: {nstory} | carrosseis: {ncar}")
    a = check_promise(AGOSTO)
    print("QA:", "TUDO CASADO" if a == 0 else f"{a} alertas")
