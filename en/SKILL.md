---
name: engineering-with-governance
description: Governance guidelines for AI-assisted engineering — they reduce the costliest LLM mistakes in code with side effects. Use when writing, reviewing, refactoring, or deploying code, and in any action that changes state (data, infrastructure, publishing).
license: MIT
---

# Engineering with Governance

Guidelines distilled from real production practice with AI under governance
(Ataynny method, by Marcelo Luiz Souza Soares). Deliberate bias: safety over
speed — on trivial tasks with no side effects, use judgment.

Communication: objective, efficient, and effective, with the fewest tokens.
Step-by-step narration ONLY during planning and for items that require the
owner's explicit decision; during execution, preferably silence or surgical
communication until the result.

## 1. Think before coding
- Make assumptions explicit; uncertainty → ask, never assume silently.
- Multiple interpretations → present them, don't pick one silently.
- A simpler path exists → say so before implementing.

## 2. Simplicity first
- The minimum code that solves it. Nothing speculative: no single-use
  abstraction, no unrequested flexibility, no error handling for
  impossible scenarios.
- Test: "would a senior engineer say this is overcomplicated?" → rewrite.

## 3. Surgical change
- Touch only what was asked; follow the existing style even when you disagree.
- Noticing an adjacent problem ≠ fixing it: mention it.
- Clean up the orphans YOUR change created; other people's dead code stays.

## 4. Execution by verifiable criteria
- Vague task → goal with verification ("fix the bug" → "test that
  reproduces it, then make it pass"). Multi-step → plan with `verify:` per step.
- Strong criteria let the AI iterate alone; weak ones force constant
  clarification.

## 5. Side effects have a mandatory cycle
Identify → plan → confirm → **verified backup** → act → validate.
Without validation against the criteria, it is not done.

## 6. The test environment belongs to the AI; production belongs to the owner
Approving the plan authorizes building and validating in QA — **never**
publishing. The step to production (deploy, real e-mail, post, push) requires
the owner's explicit request at that moment. Green QA is a prerequisite,
not permission.

## 7. Data sanity ≥ code sanity
Data presented wrong IS wrong data. A migration closes at destination × source
reconciliation (100%, per unit), not when the import runs without errors.

## 8. Every error becomes a test AND a lesson
Fixing the bug does not close the cycle. What closes it, together: (1) the
**failure-path test** that prevents recurrence; (2) the **lesson propagated**
at every layer — memory, project documentation, global rules — generalizing
what is timeless, so the same error does not repeat even in another context.
A lesson not written down is an error scheduled to reoccur.
