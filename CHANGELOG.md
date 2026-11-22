# Changelog

Content changes to the commandments (`en/SKILL.md` + `pt-br/SKILL.md`).
Language revisions and formatting are out of scope, unless they change
meaning. Both languages always move together.

Mudanças de **conteúdo** dos mandamentos (`en/SKILL.md` + `pt-br/SKILL.md`).
Revisão de idioma e formato ficam de fora, salvo quando mudam o sentido.
Os dois idiomas andam sempre juntos.

---

## 2026-11-22

Revision of the list against what the author's working rules learned
between August and November. One change per commandment where a lesson
proved general; stack-specific rules stay out.

- **Commandment 1** — uncertainty splits in two: **facts get checked**
  (code, data, records), **intent gets asked**. New bullet: a claim needs
  a source that was read or measured, and a symptom the human reports is
  data, reproduced before it is explained.
- **Commandment 4** — new bullet: **finishing is the AI's duty**. Offering
  "stop or keep going?" after failing shifts the responsibility; when
  nothing converges, hand over what was ruled out and ask for the data
  only the human has.
- **Commandment 5** — new bullet: classify an action by its **effect**,
  not its purpose.
- **Commandment 6** — new bullet: reversible, backed up and confined to
  QA → proceed without asking.
- **Commandment 8** — "red is a hypothesis too" adds that an **empty
  search doesn't prove absence** (positive control).
- **Commandment 9** — new bullet: a new mechanism can't share the nature
  of the one that failed (a fix that depends on remembering is a
  reminder, not a control); the proof by reversal is **local, never
  published**.
- **Commandment 10** — new bullet: consumption measured against an
  agreed ceiling during the task; publish only what changed.
- Bullet count stays at 3 to 4 per commandment; `README.md` unchanged.

---

- **Mandamento 1** — a incerteza se divide em duas: **fato se apura**
  (código, dado, registro), **intenção se pergunta**. Bullet novo: afirmar
  exige fonte lida ou medida, e sintoma relatado pelo humano é dado, que
  se reproduz antes de se explicar.
- **Mandamento 4** — bullet novo: **concluir é obrigação da IA**. Oferecer
  "paro ou continuo?" depois de falhar transfere a responsabilidade; sem
  convergir, entregar o que já foi descartado e pedir o dado que só o
  humano tem.
- **Mandamento 5** — bullet novo: classificar a ação pelo **efeito**, não
  pelo propósito.
- **Mandamento 6** — bullet novo: reversível, com backup e restrito ao QA
  → seguir sem perguntar.
- **Mandamento 8** — "vermelho também é hipótese" ganha que **busca vazia
  não prova ausência** (controle positivo).
- **Mandamento 9** — bullet novo: mecanismo novo não pode ter a natureza
  do que falhou (correção que depende de lembrar é lembrete, não
  controle); a prova por reversão é **local, nunca publicada**.
- **Mandamento 10** — bullet novo: consumo medido contra um teto acordado
  durante a tarefa; publicar só o que mudou.
- A contagem segue em 3 a 4 bullets por mandamento; `README.md` sem
  mudança.

---

## 2026-08-11

- **Commandment 0** — new bullet on **authorship of decisions**: a
  proposal, criterion or term that came from the AI is announced as the
  AI's; a quote from the human is literal or it is not a quote.
  Attributing to the human a choice the AI made takes away their ability
  to know what they are approving.
- **Commandment 5** — "verified backup" becomes "**verified backup and
  tested recovery**". It was the only operational term in the list
  without a criterion: read without context, it invited "I made a copy".
- **Commandment 10** — the title now names both axes already present in
  its bullets: **financial/tokens and of attempts/time**.
- `README.md` — commandment 10 row updated; bullet count corrected from
  "3" to "**3 to 4**": commandment 8 gained a 4th bullet on 2026-08-05
  (`1d660f5`), while the README had claimed "3" since 2026-08-03
  (`abf20ba`) — the line was stale for 6 days before this change.

---

- **Mandamento 0** — bullet novo sobre **autoria de decisão**: proposta,
  critério ou termo que saiu da IA se anuncia como dela; citação do
  humano é literal ou não é citação. Atribuir ao humano uma escolha que a
  IA fez tira dele a capacidade de saber o que está aprovando.
- **Mandamento 5** — "backup verificado" vira "**backup verificado e
  recuperação testada**". Era o único termo operacional da lista sem
  critério: quem lia sem contexto entendia "fiz uma cópia".
- **Mandamento 10** — o título passa a nomear os dois eixos que já
  conviviam nos bullets: **financeiro/tokens e de tentativa/tempo**.
- `README.md` — linha do mandamento 10 atualizada; contagem de bullets
  corrigida de "3" para "**3 a 4**": o mandamento 8 ganhou um 4º bullet em
  05/08/2026 (`1d660f5`), e o README afirmava "3" desde 03/08/2026
  (`abf20ba`) — a linha estava vencida havia 6 dias.

## 2026-08-05

- **Commandment 0** — now **cuts both ways**: following the letter of a
  request you know will disappoint is the same failure from the other
  side → say so first, then do what the human decides.
- **Commandment 8** — new bullet, "**red is a hypothesis too**": when a
  fix has no effect or the number contradicts what you see, suspect the
  instrument before the subject; prove by reversal.

---

- **Mandamento 0** — passa a **cortar para os dois lados**: executar ao
  pé da letra o que se sabe que vai frustrar é a mesma falha pela outra
  ponta → apontar antes, e então fazer o que o humano decidir.
- **Mandamento 8** — bullet novo, "**vermelho também é hipótese**":
  quando o ajuste não surte efeito ou o número contradiz o olho,
  suspeitar do medidor antes do medido; provar por reversão.

## 2026-08-04

- Skill names aligned with this repo (`governance` / `governanca`), so
  both languages can be installed side by side.
- Nomes das skills alinhados com este repo (`governance` / `governanca`),
  para os dois idiomas poderem ser instalados lado a lado.

## 2026-08-03

This repository was first published on this date (`71e4efb`), carrying 8
commandments. The full review later the same day (`faf97f5`) brought it to
the form it still has: **11 items, ~3 bullets each, no jargon**.

- **Commandment 0** (the human decides) and **commandment 9** (a rule
  violated twice becomes an automated block) enter the list.
- **Commandment 10** (cost and its control) enters, with cost-for-existing
  and unit cost before scaling.
- Commandments 5–8 rewritten in the bullet style of 1–4.
- "owner" → "**human**" throughout.
- Header rule on lean communication: narration only for planning and
  decisions; execution allows punctual updates, not only silence.
- English version created; MIT `LICENSE` added.

---

Este repositório foi publicado nesta data (`71e4efb`), com 8 mandamentos.
A revisão completa, mais tarde no mesmo dia (`faf97f5`), o levou à forma
que mantém até hoje: **11 itens, ~3 bullets cada, sem jargão**.

- **Mandamento 0** (quem decide é o humano) e **mandamento 9** (regra
  violada 2× vira bloqueio automático) entram na lista.
- **Mandamento 10** (custo e seu controle) entra, com custo por existir e
  custo unitário antes de escalar.
- Mandamentos 5–8 reescritos no estilo bullet dos 1–4.
- "dono" → "**humano**" em todo o texto.
- Regra de comunicação enxuta no cabeçalho: narração só em planejamento e
  decisão; execução admite comunicação pontual, não só silêncio.
- Versão em inglês criada; `LICENSE` MIT adicionada.

## Origin · Origem

Distilled from the author's own global AI-assistant rules, in the format
of the `karpathy-guidelines` community skill. Deliberately
depersonalized: the episodes and numbers behind each rule stay private —
what ships here is only what is timeless and reusable elsewhere.

Destilada das regras globais do próprio autor para assistente de IA, no
formato da skill comunitária `karpathy-guidelines`. Despersonalizada de
propósito: os episódios e números que motivaram cada regra ficam
privados — aqui vai só o que é atemporal e reusável por outro ambiente.
