#!/usr/bin/env python3
"""Valida o frontmatter YAML dos SKILL.md.

Por que existe: em 04/ago/2026 a `description` foi reescrita com um ':'
seguido de espaço dentro do valor sem aspas ("não recarregar: seria
repetir"). O YAML lê isso como início de um novo mapeamento e o arquivo
inteiro deixa de parsear, o que o GitHub exibe como

    Error in user YAML: mapping values are not allowed in this context

Um SKILL.md com frontmatter inválido pode não carregar como skill, então
o defeito é funcional, não estético. Passou despercebido porque nada
verificava o frontmatter, e o erro só aparece na página do GitHub.

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


def main() -> int:
    todos: list[str] = []
    for nome in ARQUIVOS:
        caminho = RAIZ / nome
        if not caminho.exists():
            todos.append(f"{nome}: arquivo não encontrado")
            continue
        erros = valida(caminho)
        print(f"{'✅' if not erros else '❌'} {nome}")
        todos.extend(erros)

    if todos:
        print("\nFrontmatter inválido:\n")
        for e in todos:
            print(f"  {e}")
        return 1

    print("\nFrontmatter válido nos dois idiomas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
