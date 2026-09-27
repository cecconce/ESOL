from _h import *

LESSONS = [
L("c0-format", "0.1", "Com'è fatto l'esame", "Le 4 parti, i tempi e cosa guarda davvero l'esaminatore",
  ["format", "strategy"], 10, 1,
  "Sapere esattamente cosa succede in ognuno dei 13 minuti, così niente ti coglie di sorpresa.",
  P("""<p>Lo Speaking di LanguageCert Communicator B2 dura circa <strong>13 minuti</strong> ed è un colloquio a tu per tu con un esaminatore (l'interlocutore), di solito registrato. Le parti sono sempre quattro e sempre nello stesso ordine.</p>""", h="Le quattro parti"),
  UL(["<strong>Part 1 · 3 min</strong> — domande personali su 4–5 temi diversi (casa, lavoro, tempo libero, cibo…). Risposte brevi ma sviluppate: 2–4 frasi, con un motivo o un esempio.",
      "<strong>Part 2 · 3 min</strong> — due role-play sociali. In uno l'esaminatore apre e tu reagisci; nell'altro devi iniziare tu (proporre, scusarti, chiedere, lamentarti…).",
      "<strong>Part 3 · 3–4 min</strong> — tu e l'esaminatore avete due liste di idee diverse per lo stesso progetto o evento. Dovete confrontarle e <em>decidere insieme</em>.",
      "<strong>Part 4 · 4 min</strong> — ricevi un argomento, hai circa 30 secondi per prendere appunti, parli per 2 minuti, poi rispondi a qualche domanda di approfondimento."],
     h="Minuto per minuto"),
  P("""<p>In sintesi i criteri sono quattro, con lo stesso peso:</p>
<ul class="plain">
<li><strong>Svolgimento del compito e coerenza</strong> — rispondi a ciò che ti chiedono, con risposte collegate e della lunghezza giusta.</li>
<li><strong>Grammatica</strong> — correttezza e varietà. Qui ti sono costati i tempi verbali, gli articoli e le preposizioni.</li>
<li><strong>Lessico</strong> — parole adatte, non tradotte parola per parola dall'italiano.</li>
<li><strong>Pronuncia e fluidità</strong> — farsi capire senza fatica, con pause naturali, non lunghi silenzi.</li>
</ul>
<p>La soglia B2 non chiede perfezione. Chiede che gli errori <em>non ostacolino la comunicazione</em> e che non siano sistematici. Un errore isolato non boccia; lo stesso errore ripetuto 15 volte sì.</p>""", h="Cosa viene valutato"),
  FIX([("I have been bocciato two times.", "I've failed it twice.", "“Two times” si capisce, ma “twice” è la forma naturale. “Bocciato” = <em>failed</em>.", "calque"),
       ("The exam is of 13 minutes.", "The exam takes 13 minutes. / It's a 13-minute exam.", "Niente “of” per la durata; nota “13-minute” senza -s quando è aggettivo.", "prep")],
      h="Due frasi che ti servono subito"),
  TASK("<p>Spiega a voce, in inglese, com'è fatto l'esame come se lo raccontassi a un collega: <em>“The exam has four parts. In the first part…”</em>. Usa almeno tre connettori (<em>first, then, after that, finally</em>).</p>", 60),
),

L("c0-strategy", "0.2", "Strategia per il terzo tentativo", "Il contenuto c'è già: si lavora sulla precisione sotto pressione",
  ["strategy", "tense", "articles", "calques"], 15, 1,
  "Trasformare i cinque errori ricorrenti in una checklist mentale da usare durante l'esame.",
  P("""<p>Le due bocciature non sono arrivate per mancanza di idee ma per <strong>imprecisioni formali sotto pressione</strong>. Quindi il piano non è imparare frasi più difficili: è dire cose semplici, <em>corrette</em>, e completare ogni compito.</p>
<p>Regola d'oro: <strong>frase semplice e giusta &gt; frase complessa e sbagliata</strong>. Una frase corta con il tempo verbale corretto vale più di una frase lunga con tre calchi.</p>""", h="Il punto di partenza"),
  UL(["<strong>Tempo verbale</strong> — prima di raccontare, decidi: <em>è finito e ha una data?</em> → past simple. <em>Collega il passato a oggi, senza data?</em> → present perfect.",
      "<strong>Articoli</strong> — sostantivo singolare numerabile = serve <em>a/the/my</em>. Mai “I am teacher”.",
      "<strong>Preposizioni</strong> — le 15 combinazioni che sbagli sono nella lezione 5.3: ripassale la sera prima.",
      "<strong>Calchi</strong> — se una frase “suona” italiana, cambiala in una più semplice.",
      "<strong>Connettori</strong> — tieni pronti 4 connettori parlati: <em>Also… · On the other hand… · For example… · So, all in all…</em>"],
     h="La checklist dei 5 errori"),
  PH([("Autocorreggersi (è un punto a favore, non contro)",
       [("Sorry, I mean…", "mi correggo"), ("Let me rephrase that.", "lo ridico meglio"),
        ("What I'm trying to say is…", "quello che intendo è…")]),
      ("Se non capisci la domanda",
       [("Sorry, could you repeat the question, please?", ""), ("Do you mean … ?", "verifica"),
        ("Sorry, I'm not sure I understand what you mean by …", "")])],
     h="Frasi di sicurezza"),
  FIX([("I have gone to London in 2019.", "I went to London in 2019.", "C'è una data → past simple.", "tense"),
       ("I am teacher in a technical school.", "I'm a teacher at a technical school.", "Articolo con il mestiere; “at” per il luogo di lavoro.", "art"),
       ("I am agree.", "I agree.", "“Agree” è già un verbo: niente “am”.", "calque")],
      h="I tre errori più frequenti delle prove precedenti"),
  TASK("<p>Parla per un minuto di <em>“Why are you taking this exam?”</em>. Registrati con il telefono, riascolta e conta: quanti verbi al passato sono corretti? Quanti sostantivi hanno l'articolo giusto?</p>", 60),
),

L("c0-fluency", "0.3", "Prendere tempo senza bloccarsi", "Frasi per pensare, riformulare e non restare in silenzio",
  ["fluency", "strategy"], 10, 2,
  "Avere 10 frasi automatiche che riempiono i secondi di riflessione in modo naturale.",
  P("""<p>Un silenzio di 4–5 secondi pesa sulla fluidità più di un piccolo errore. Queste frasi ti comprano 2–3 secondi e suonano naturali, a patto di <strong>non usarle a ogni risposta</strong>: sceglile a rotazione.</p>"""),
  PH([("Per pensare", [("That's a good question. Let me think…", ""), ("Well, it depends, really.", ""),
                       ("I've never really thought about it, but…", ""), ("Hmm, how can I put it…", "")]),
      ("Per dare opinioni", [("Personally, I think…", ""), ("As far as I'm concerned…", ""),
                            ("If you ask me…", ""), ("I'd say that…", "")]),
      ("Se non trovi una parola", [("I can't remember the word, but it's a kind of…", "descrivi"),
                                  ("It's something you use to…", "descrivi la funzione"),
                                  ("It's like a … but smaller.", "confronta")])]),
  FIX([("How can I say…", "How can I put it…", "“How can I say” è un calco di “come posso dire”.", "calque"),
       ("Eh… eh… eh…", "Well, let me think…", "I suoni di esitazione italiani si notano: sostituiscili con “well”.", "")]),
  TASK("<p>Rispondi a queste tre domande iniziando <em>ogni volta con una frase diversa</em> per prendere tempo: <br>1. What's the best age to learn a language? <br>2. Is it better to live in a city or in the countryside? <br>3. What would you change about your job?</p>", 90),
),
]
