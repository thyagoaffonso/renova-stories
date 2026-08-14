# -*- coding: utf-8 -*-
"""Renderiza um mes de conteudo Renova para dentro do repo e gera o JSON de publicacao."""
import os, sys, json
import renova_render as R

REPO = os.path.join(os.path.dirname(__file__), "renova_repo")
RAWBASE = "https://raw.githubusercontent.com/thyagoaffonso/renova-stories/main"

def render_month(pasta, dados_dict, out_json):
    """pasta: subpasta no repo (ex 'agosto'); dados_dict: {date: {stories, carrossel}}"""
    root = os.path.join(REPO, pasta)
    os.makedirs(root, exist_ok=True)
    pub = {}
    for date in sorted(dados_dict):
        blk = dados_dict[date]
        ddir = os.path.join(root, date)
        os.makedirs(ddir, exist_ok=True)
        entry = {"stories": [], "carrossel": None}
        # stories
        for i, fr in enumerate(blk["stories"]):
            img = R.story_frame(fr["role"], fr, i, len(blk["stories"]))
            fn = f"story_{i+1}.png"
            img.save(os.path.join(ddir, fn), "PNG")
            entry["stories"].append(f"{RAWBASE}/{pasta}/{date}/{fn}?v=1")
        # carrossel
        car = blk.get("carrossel")
        if car:
            urls = []
            for i, sl in enumerate(car["slides"]):
                img = R.carousel_slide(sl["role"], sl, i, len(car["slides"]))
                fn = f"slide_{i+1}.png"
                img.save(os.path.join(ddir, fn), "PNG")
                urls.append(f"{RAWBASE}/{pasta}/{date}/{fn}?v=1")
            entry["carrossel"] = {"children": urls, "legenda": car["legenda"]}
        pub[date] = entry
    with open(os.path.join(REPO, out_json), "w", encoding="utf-8") as f:
        json.dump(pub, f, ensure_ascii=False, indent=2)
    ns = sum(len(v["stories"]) for v in pub.values())
    nc = sum(1 for v in pub.values() if v["carrossel"])
    print(f"{pasta}: {len(pub)} dias | {ns} stories | {nc} carrosseis -> {out_json}")
    return pub

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "agosto"
    if which == "agosto":
        from conteudo_agosto import AGOSTO
        render_month("agosto", AGOSTO, "dados_agosto.json")
    elif which == "setembro":
        from conteudo_setembro import SETEMBRO
        render_month("setembro", SETEMBRO, "dados_setembro.json")
