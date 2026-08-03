# Engineering with Governance · Engenharia com Governança

Governance guidelines for AI-assisted engineering — they reduce the costliest
LLM mistakes in code with side effects. Distilled from real production
practice: the Ataynny method, by Marcelo Luiz Souza Soares
([ataynny.com](https://ataynny.com)).

Diretrizes de governança para engenharia assistida por IA — reduzem os erros
mais caros de LLM em código com efeito colateral. Destiladas de prática real
de produção: método Ataynny, por Marcelo Luiz Souza Soares
([ataynny.com](https://ataynny.com)).

## The 10+1 commandments · Os 10+1 mandamentos

Ten numbered principles plus the zeroth — the one that rules them all.
Dez princípios numerados mais o zero — o que manda em todos.

| # | English | Português (BR) |
|---|---------|----------------|
| 0 | The human decides — never the AI | Quem decide é o humano, nunca a IA |
| 1 | Think before acting | Pensar antes de agir |
| 2 | Simplicity first | Simplicidade primeiro |
| 3 | Surgical change | Mudança cirúrgica |
| 4 | Execution by verifiable criteria | Execução por critério verificável |
| 5 | Side effects have a mandatory cycle | Efeito colateral tem ciclo obrigatório |
| 6 | QA belongs to the AI; PROD belongs to the human | QA é da IA; PROD é do humano |
| 7 | Data sanity ≥ code sanity | Sanidade dos dados ≥ sanidade do código |
| 8 | Every error becomes a test AND a lesson | Todo erro vira teste E aprendizado |
| 9 | A rule violated twice becomes an automated block | Regra violada 2× vira bloqueio automático |
| 10 | Cost and its control are fundamental requirements | Custo e seu controle são requisitos fundamentais |

Each principle is 3 bullets — the full text is a 5-minute read.
Cada princípio tem 3 bullets — o texto completo se lê em 5 minutos.

## Versions · Versões

- **English:** [`en/SKILL.md`](en/SKILL.md)
- **Português (BR):** [`pt-br/SKILL.md`](pt-br/SKILL.md)

## Installation · Instalação

Each version is a self-contained skill file in the [Agent Skills](https://code.claude.com/docs/en/skills)
format (Markdown with YAML frontmatter).

**Claude Code** — copy the file of your language as `SKILL.md` into a skill
folder, personal or per-project:

```bash
mkdir -p ~/.claude/skills/engineering-with-governance
curl -o ~/.claude/skills/engineering-with-governance/SKILL.md \
  https://raw.githubusercontent.com/MarceloSoares1970/engineering-with-governance/main/en/SKILL.md
```

(For the PT-BR version, replace `en/SKILL.md` with `pt-br/SKILL.md`; for a
single project, use `.claude/skills/` inside the repo instead.)

**Other agent harnesses** — any tool that loads Markdown skills can consume
the file as-is. It also works as plain reading guidelines for humans.

**Claude Code** — copie o arquivo do seu idioma como `SKILL.md` para uma
pasta de skill, pessoal (`~/.claude/skills/`) ou por projeto
(`.claude/skills/`). Qualquer harness de agente que carregue skills em
Markdown consome o arquivo como está — e ele também funciona como diretrizes
de leitura para humanos.

## About · Sobre

The Ataynny method comes from building and operating production SaaS with AI
under engineering governance. More at [ataynny.com](https://ataynny.com).

O método Ataynny nasce da construção e operação de SaaS em produção com IA
sob governança de engenharia. Mais em [ataynny.com](https://ataynny.com).

Credit where due: the community skill distilling **Andrej Karpathy**'s
guidelines for AI-assisted coding helped complement and reinforce lessons
we had already learned in production, and informed the shape of this skill.

Crédito a quem merece: a skill da comunidade que destila as diretrizes de
**Andrej Karpathy** para código assistido por IA ajudou a complementar e
reforçar lições que já havíamos aprendido em produção, e influenciou a
forma desta skill.

## License · Licença

[MIT](LICENSE) — Copyright (c) 2026 Marcelo Soares
