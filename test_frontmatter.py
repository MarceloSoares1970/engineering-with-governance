#!/usr/bin/env python3
"""Valida o frontmatter YAML e a estrutura dos SKILL.md.

Por que existe: em 04/ago/2026 a `description` foi reescrita com um ':'
seguido de espaço dentro do valor sem aspas ("não recarregar: seria
repetir"). O YAML lê isso como início de um novo mapeamento e o arquivo
inteiro deixa de parsear, o que o GitHub exibe como

    Error in user YAML: mapping values are not allowed in this context

Um SKILL.md com frontmatter inválido pode não carregar como skill, então
o defeito é funcional, não estético. Passou despercebido porque nada
verificava o frontmatter, e o erro só aparece na página do GitHub.

Em 11/ago/2026 um segundo defeito passou por aqui: o título do mandamento 10
foi escrito quebrado em duas linhas ("## 10. ... —" + "financeiro/tokens..."),
e em Markdown o `##` termina no fim da linha. O resultado seria um cabeçalho
truncado com um parágrafo órfão abaixo. Este teste passou nos dois casos,
porque só olhava o frontmatter — guard que existe não é guard que cobre o
defeito da vez. Daí a checagem de ESTRUTURA abaixo.

Escopo declarado: valida frontmatter + estrutura de cabeçalho + a contagem de
mandamentos. NÃO valida o conteúdo do texto — para isso não existe gate.

Roda sem dependências (não exige PyYAML).
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
ARQUIVOS = ("pt-br/SKILL.md", "en/SKILL.md")
OBRIGATORIAS = ("name", "description", "license")


def valida(caminho: Path) -> list[str]:
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    erros: list[str] = []

    if linhas[0] != "---":
        return [f"{caminho}: não começa com '---'"]
    try:
        fim = linhas.index("---", 1)
    except ValueError:
        return [f"{caminho}: frontmatter não é fechado por '---'"]

    chaves = []
    for i, linha in enumerate(linhas[1:fim], start=2):
        if not linha.strip():
            continue
        if not re.match(r"^[a-z_]+: \S", linha):
            erros.append(f"{caminho}:{i}: não está no formato 'chave: valor'")
            continue

        chave, valor = linha.split(": ", 1)
        chaves.append(chave)

        # O caso que quebrou: ': ' solto num valor sem aspas.
        entre_aspas = valor.startswith('"') and valor.endswith('"')
        if not entre_aspas:
            m = re.search(r":\s", valor)
            if m:
                col = len(chave) + 2 + m.start() + 1
                erros.append(
                    f"{caminho}:{i}: coluna {col}: ':' seguido de espaço em valor "
                    f"sem aspas quebra o YAML. Reescreva sem os dois-pontos, ou "
                    f'envolva o valor inteiro em aspas duplas. Trecho: '
                    f"...{valor[max(0, m.start()-28):m.start()+10]!r}"
                )
        # '#' solto vira comentário e trunca o valor
        if not entre_aspas and re.search(r"\s#", valor):
            erros.append(f"{caminho}:{i}: '#' em valor sem aspas vira comentário")

    for obrigatoria in OBRIGATORIAS:
        if obrigatoria not in chaves:
            erros.append(f"{caminho}: falta a chave '{obrigatoria}'")

    return erros


def valida_estrutura(caminho: Path) -> list[str]:
    """Cabeçalhos íntegros e os 11 mandamentos presentes.

    O `##` do Markdown termina no fim da linha: título quebrado em duas vira
    cabeçalho truncado + parágrafo órfão. O sintoma é um cabeçalho terminando
    em pontuação de continuação (— , : ; ,) ou uma linha de texto colada logo
    abaixo sem linha em branco.
    """
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    erros: list[str] = []
    numerados = []

    for i, linha in enumerate(linhas, start=1):
        if not linha.startswith("## "):
            continue
        titulo = linha.rstrip()
        if titulo.endswith(("—", "-", ":", ";", ",")):
            erros.append(
                f"{caminho}:{i}: cabeçalho termina em '{titulo[-1]}' — título "
                f"quebrado em duas linhas? O '##' do Markdown acaba no fim da "
                f"linha; junte tudo numa só. Trecho: {titulo[:60]!r}"
            )
        seguinte = linhas[i] if i < len(linhas) else ""
        if seguinte.strip() and not seguinte.startswith(("-", "*", "#", "|", ">")):
            erros.append(
                f"{caminho}:{i+1}: texto solto logo abaixo do cabeçalho "
                f"{titulo[:40]!r} — provável continuação de um título quebrado. "
                f"Trecho: {seguinte[:50]!r}"
            )
        m = re.match(r"^## (\d+)\.", titulo)
        if m:
            numerados.append(int(m.group(1)))

    esperado = list(range(0, 11))  # 10+1 mandamentos: 0 a 10
    if numerados != esperado:
        erros.append(
            f"{caminho}: mandamentos numerados {numerados} — esperado {esperado}. "
            f"Falta algum, sobra, ou um título quebrou e deixou de ser cabeçalho."
        )
    return erros


def main() -> int:
    todos: list[str] = []
    for nome in ARQUIVOS:
        caminho = RAIZ / nome
        if not caminho.exists():
            todos.append(f"{nome}: arquivo não encontrado")
            continue
        erros = valida(caminho) + valida_estrutura(caminho)
        print(f"{'✅' if not erros else '❌'} {nome}")
        todos.extend(erros)

    if todos:
        print("\nProblemas encontrados:\n")
        for e in todos:
            print(f"  {e}")
        return 1

    print("\nFrontmatter e estrutura válidos nos dois idiomas (11 mandamentos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
