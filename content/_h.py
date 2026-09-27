"""Helper per scrivere le lezioni in modo compatto.

Ogni file di contenuto definisce CHAPTER (id del capitolo) e LESSONS (lista di L(...)).
I blocchi disponibili sono le funzioni qui sotto; vengono resi dal JavaScript della pagina.
"""


def L(id, n, title, sub, tags, min, day, goal, *blocks):
    return dict(id=id, n=n, title=title, sub=sub, tags=list(tags), min=min, day=day,
                goal=goal, blocks=list(blocks))


def P(html, h=None):
    return dict(t="p", html=html, h=h)


def UL(items, h=None):
    return dict(t="list", items=items, h=h)


def QA(items, h="Domande d'esame con risposta modello", note=None):
    """items: lista di (domanda, risposta[, suggerimento])"""
    out = []
    for it in items:
        d = dict(q=it[0], a=it[1])
        if len(it) > 2:
            d["tip"] = it[2]
        out.append(d)
    return dict(t="qa", items=out, h=h, note=note)


def PH(groups, h="Frasi pronte"):
    """groups: lista di (nome_gruppo, [frase | (frase, nota_it)])"""
    return dict(t="phrases", h=h, groups=[dict(name=g, items=[list(i) if isinstance(i, tuple) else i for i in items]) for g, items in groups])


def FIX(items, h="Errori da evitare"):
    """items: (sbagliato, corretto, perché, tag) — tag: tense/art/prep/calque/conn/wo/vocab"""
    return dict(t="fix", h=h, items=[list(i) + [""] * (4 - len(i)) for i in items])


def VOC(items, h="Lessico utile"):
    return dict(t="vocab", h=h, items=[list(i) for i in items])


def DLG(lines, h=None, ctx=None):
    return dict(t="dlg", h=h, ctx=ctx, lines=[list(x) for x in lines])


def TASK(html, timer=None, prep=None, h="Allenati adesso"):
    return dict(t="task", html=html, timer=timer, prep=prep, h=h)


def NEG(brief, you, exam, h="Il compito"):
    return dict(t="neg", h=h, brief=brief, you=you, exam=exam)


def MONO(topic, prompts, notes, model, follow=None, h="Il monologo"):
    return dict(t="mono", h=h, topic=topic, prompts=prompts, notes=notes, model=model,
                follow=[dict(q=q, a=a) for q, a in (follow or [])])
