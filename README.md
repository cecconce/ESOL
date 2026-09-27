# ESOL — B2 Speaking Lab

Lezioni per l'esame **LanguageCert / EISOL Communicator B2 – Speaking**, organizzate in un sito web che funziona anche fuori da GitHub.

- **58 lezioni** in 7 capitoli: orientamento, Part 1, Part 2, Part 3, Part 4, grammatica per parlare, simulazioni complete
- **Tre modi di navigare**: per *capitolo*, per *argomento* (temi e abilità) e per *tempo* (percorso di 14 giorni oppure lezioni da 10/15/20/30 minuti)
- In ogni lezione: risposte modello da aprire dopo aver provato, frasi pronte con pulsante *ascolta*, errori tipici (corretto/sbagliato), esercizi con **timer** (anche 30″ + 2′ per la Part 4)
- I progressi (“segna come completata”) restano salvati nel browser

## Come usarlo

| Dove | Come |
|---|---|
| Sul computer, senza internet | Scarica `index.html` e aprilo con doppio clic. È un unico file. |
| Online con GitHub Pages | *Settings → Pages → Source: Deploy from a branch → `main` / root*. Il sito sarà su `https://cecconce.github.io/ESOL/` |
| Su telefono | Apri il link di GitHub Pages e aggiungilo alla schermata Home. |

## Struttura

```
index.html          il sito (generato, non modificare a mano)
build.py            genera index.html dai contenuti; contiene capitoli, argomenti e percorso a giorni (PLAN)
src/template.html   grafica e funzionamento della pagina
content/*.py        le lezioni, un file per capitolo
  c0_start.py       Capitolo 0 – Si parte da qui
  p1_personal.py    Capitolo 1 – Part 1, domande personali
  p2_roleplay.py    Capitolo 2 – Part 2, role-play
  p3_negotiation.py Capitolo 3 – Part 3, negoziazione
  p4_longturn.py    Capitolo 4 – Part 4, monologo
  gr_grammar.py     Capitolo 5 – Grammatica per parlare
  mk_mock.py        Capitolo 6 – Simulazioni complete
```

## Aggiungere o modificare una lezione

1. Apri il file del capitolo in `content/` e copia una lezione esistente (`L(...)` oppure `topic(...)`, `rp(...)`, `task(...)`, `mono(...)`).
2. Cambia `id`, numero, titolo, argomenti e contenuto.
3. Aggiungi l'`id` al giorno giusto in `PLAN` dentro `build.py`.
4. Esegui `python3 build.py` e ricarica `index.html`.
