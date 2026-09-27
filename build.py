#!/usr/bin/env python3
"""Genera il sito statico delle lezioni.

    python3 build.py

Produce:
  index.html            -> pagina completa per GitHub Pages (o da aprire con doppio clic)
  dist/fragment.html    -> stessa pagina senza <html>/<head>, per la pubblicazione come artifact
"""
import html
import importlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "content"))

CHAPTERS = [
    dict(id="c0", label="Capitolo 0", color="p0", title="Si parte da qui",
         desc="Com'è fatto l'esame, come viene valutato e la strategia per il terzo tentativo."),
    dict(id="p1", label="Capitolo 1 · Part 1", color="p1", title="Domande personali",
         desc="Rispondere subito e bene su temi di vita quotidiana: risposta + motivo + esempio."),
    dict(id="p2", label="Capitolo 2 · Part 2", color="p2", title="Role-play sociali",
         desc="Frasi funzionali e situazioni: quando inizi tu e quando reagisci all'esaminatore."),
    dict(id="p3", label="Capitolo 3 · Part 3", color="p3", title="Discussione e negoziazione",
         desc="Confrontare idee diverse, trovare un compromesso e arrivare a una decisione."),
    dict(id="p4", label="Capitolo 4 · Part 4", color="p4", title="Monologo di 2 minuti",
         desc="Appunti in 30 secondi, una storia semplice e ben strutturata, poi le domande."),
    dict(id="gr", label="Capitolo 5", color="p5", title="Grammatica per parlare",
         desc="Solo gli errori che ti sono costati l'esame: tempi, articoli, preposizioni, calchi, connettori."),
    dict(id="mk", label="Capitolo 6", color="p6", title="Simulazioni complete",
         desc="Tre prove d'esame intere da 13 minuti, con autovalutazione finale."),
]
MODULES = {"c0": "c0_start", "p1": "p1_personal", "p2": "p2_roleplay", "p3": "p3_negotiation",
           "p4": "p4_longturn", "gr": "gr_grammar", "mk": "mk_mock"}

TAGS = {
    # temi
    "phone": "Telefono e comunicazione", "manners": "Buone maniere", "food": "Cibo e bevande",
    "education": "Scuola e studio", "travel": "Viaggi e trasporti", "work": "Lavoro",
    "freetime": "Tempo libero", "sport": "Sport", "home": "Casa e quartiere", "tech": "Tecnologia",
    "shopping": "Acquisti e soldi", "weather": "Tempo atmosferico e stagioni",
    "family": "Famiglia e amici", "health": "Salute e stile di vita", "festivals": "Feste e celebrazioni",
    "media": "Media e notizie", "environment": "Ambiente", "town": "Città e servizi",
    "events": "Eventi e organizzazione",
    # abilità
    "format": "Formato e valutazione", "strategy": "Strategia d'esame", "fluency": "Fluidità e prendere tempo",
    "functions": "Funzioni comunicative (Part 2)", "negotiation": "Accordo, disaccordo, compromesso",
    "storytelling": "Raccontare una storia", "tense": "Tempi verbali", "articles": "Articoli",
    "prepositions": "Preposizioni", "calques": "Calchi dall'italiano", "connectors": "Connettori",
    "mock": "Simulazione d'esame",
}
TAG_GROUPS = [
    dict(title="Temi di conversazione", tags=["phone", "manners", "food", "education", "travel", "work",
                                              "freetime", "sport", "home", "tech", "shopping", "weather",
                                              "family", "health", "festivals", "media", "environment",
                                              "town", "events"]),
    dict(title="Abilità e grammatica", tags=["format", "strategy", "fluency", "functions", "negotiation",
                                             "storytelling", "tense", "articles", "prepositions", "calques",
                                             "connectors", "mock"]),
]
DAYS = [
    (1, "Orientamento", "Capire l'esame e partire con la formula della Part 1."),
    (2, "Part 1: primi temi", "Risposte brevi ma sviluppate, con un esempio personale."),
    (3, "Part 1 + passato", "Il nodo past simple / present perfect e tre temi nuovi."),
    (4, "Part 2: le frasi", "Il kit di frasi funzionali e i primi role-play."),
    (5, "Part 2 + articoli", "Altri role-play, articoli e domande."),
    (6, "Part 3: negoziare", "Come si discute una scelta e si arriva a un accordo."),
    (7, "Ripasso attivo", "Una negoziazione, due temi di Part 1, un role-play."),
    (8, "Part 4: la struttura", "Lo schema del monologo, gli appunti, la prima storia."),
    (9, "Part 4 + connettori", "Due monologhi e i connettori che restano nel parlato."),
    (10, "Part 3 + preposizioni", "Nuove negoziazioni e le preposizioni che sbagli."),
    (11, "Calchi e condizionali", "Le frasi “tradotte dall'italiano” e le ipotesi."),
    (12, "Simulazione A", "Prima prova completa, poi un monologo e una negoziazione."),
    (13, "Simulazione B", "Seconda prova e due monologhi nuovi."),
    (14, "Simulazione C e vigilia", "Ultima prova e checklist del giorno dell'esame."),
]


# Percorso a giorni: decide in quale giorno cade ogni lezione (sovrascrive il valore nei file di contenuto).
PLAN = {
    1: ["c0-format", "c0-strategy", "p1-intro", "p1-phone", "p1-manners"],
    2: ["c0-fluency", "p1-food", "p1-education", "p1-travel", "p1-work"],
    3: ["gr-tenses", "p1-media", "p1-freetime", "p1-home"],
    4: ["p2-howto", "p2-phrases", "p2-apologise", "p2-invite"],
    5: ["gr-articles", "gr-questions", "p2-complain", "p2-request", "p1-weather"],
    6: ["p3-howto", "p3-phrases", "p3-schoolday", "p2-advice", "p1-environment"],
    7: ["p3-teambuilding", "p1-festivals", "p1-family", "p2-feelings"],
    8: ["p4-structure", "p4-notes", "p4-person", "p1-health", "p3-club"],
    9: ["gr-connectors", "p4-achievement", "p4-difficult", "p1-shopping"],
    10: ["gr-prepositions", "p3-charity", "p3-town", "p2-plans"],
    11: ["gr-calques", "gr-conditionals", "p1-tech", "p2-info"],
    12: ["mk-a", "p4-place", "p3-exchange"],
    13: ["mk-b", "p4-skill", "p4-journey"],
    14: ["mk-c", "p4-change", "mk-day"],
}


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def text_of(obj):
    if isinstance(obj, str):
        return strip_tags(obj)
    if isinstance(obj, dict):
        return " ".join(text_of(v) for k, v in obj.items() if k not in ("t",))
    if isinstance(obj, (list, tuple)):
        return " ".join(text_of(v) for v in obj)
    return ""


def load():
    lessons = []
    for ch in CHAPTERS:
        mod = importlib.import_module(MODULES[ch["id"]])
        for l in mod.LESSONS:
            l["ch"] = ch["id"]
            l["_text"] = html.unescape(re.sub(r"\s+", " ", text_of(l["blocks"]) + " " + text_of(l["goal"])))[:4000]
            lessons.append(l)
    ids = [l["id"] for l in lessons]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"id duplicati: {dup}"
    day_of = {i: d for d, lst in PLAN.items() for i in lst}
    missing = set(ids) - set(day_of)
    unknown = set(day_of) - set(ids)
    assert not missing and not unknown, f"PLAN: mancano {missing}, sconosciuti {unknown}"
    for l in lessons:
        l["day"] = day_of[l["id"]]
    for l in lessons:
        for t in l["tags"]:
            assert t in TAGS, f"tag sconosciuto {t} in {l['id']}"
        assert 1 <= l["day"] <= len(DAYS), l["id"]
        assert re.fullmatch(r"[a-z0-9-]+", l["id"]), l["id"]
    return lessons


def main():
    lessons = load()
    data = dict(chapters=CHAPTERS, lessons=lessons, tags=TAGS, tagGroups=TAG_GROUPS,
                days=[dict(n=n, title=t, desc=d) for n, t, d in DAYS])
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    frag = tpl.replace("/*DATA*/", blob)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "fragment.html").write_text(frag, encoding="utf-8")
    head, body = frag.split('<header class="top">', 1)
    full = ('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n<header class="top">' + body + '\n</body>\n</html>\n')
    (ROOT / "index.html").write_text(full, encoding="utf-8")
    # riepilogo
    by_ch = {}
    for l in lessons:
        by_ch.setdefault(l["ch"], []).append(l)
    for ch in CHAPTERS:
        ls = by_ch.get(ch["id"], [])
        print(f"{ch['id']}: {len(ls):2d} lezioni, {sum(l['min'] for l in ls):4d} min")
    for n, t, _ in DAYS:
        ls = [l for l in lessons if l["day"] == n]
        print(f"  giorno {n:2d}: {sum(l['min'] for l in ls):3d} min  ({len(ls)} lezioni)")
    print(f"Totale: {len(lessons)} lezioni, {len(full)//1024} KB")


if __name__ == "__main__":
    main()
