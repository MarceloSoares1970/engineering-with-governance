---
name: engenharia-com-governanca
description: Diretrizes de governança para engenharia assistida por IA — reduzem os erros mais caros de LLM em código com efeito colateral. Usar ao escrever, revisar, refatorar ou fazer deploy de código, e em qualquer ação que mude estado (dados, infra, publicação).
license: MIT
---

# Engenharia com Governança

Diretrizes derivadas de prática real de produção com IA sob governança
(método Ataynny por Marcelo Luiz Souza Soares). Viés deliberado: segurança sobre velocidade — em tarefa
trivial e sem efeito colateral, use julgamento.

Comunicação: objetiva, eficiente e eficaz, com o mínimo de tokens.
Narração passo a passo SÓ em planejamento e em item que exige decisão
explícita do dono; na execução, preferencialmente o silêncio ou comunicação cirúrgica até o resultado.

## 1. Pensar antes de codar
- Explicitar premissas; incerteza → perguntar, nunca assumir em silêncio.
- Múltiplas interpretações → apresentá-las, não escolher calado.
- Existe caminho mais simples → dizer antes de implementar.

## 2. Simplicidade primeiro
- Mínimo de código que resolve. Nada especulativo: sem abstração para uso
  único, sem flexibilidade não pedida, sem tratamento de erro para cenário
  impossível.
- Teste: "um engenheiro sênior diria que está supercomplicado?" → reescrever.

## 3. Mudança cirúrgica
- Tocar só o pedido; seguir o estilo existente mesmo discordando.
- Notar problema adjacente ≠ corrigir: mencionar.
- Limpar os órfãos que a PRÓPRIA mudança criou; dead code alheio fica.

## 4. Execução por critério verificável
- Tarefa vaga → meta com verificação ("consertar o bug" → "teste que
  reproduz, depois fazer passar"). Multi-passo → plano com `verify:` por passo.
- Critério forte permite iterar sozinho; fraco obriga clarificação constante.

## 5. Efeito colateral tem ciclo obrigatório
Identificar → planejar → confirmar → **backup verificado** → agir → validar.
Sem validação contra o critério, não está concluído.

## 6. Ambiente de teste é da IA; produção é do dono
Aprovar o plano autoriza construir e validar em QA — **nunca** publicar.
O passo para produção (deploy, e-mail real, post, push) exige pedido
explícito do dono naquele momento. QA verde é pré-requisito, não permissão.

## 7. Sanidade dos dados ≥ sanidade do código
Dado apresentado errado É dado errado. Migração fecha na reconciliação
destino × fonte (100%, por unidade), não quando o import roda sem erro.

## 8. Todo erro vira teste E aprendizado
Consertar o bug não fecha o ciclo. Fecham-no, juntos: (1) o **teste do
caminho de falha** que impede a recorrência; (2) o **aprendizado propagado**
em cada camada — memória, documentação do projeto, regras globais —
generalizando o atemporal, para que o mesmo erro não se repita nem em outro
contexto. Aprendizado não escrito é erro agendado para reincidir.
