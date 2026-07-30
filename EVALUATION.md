# Evaluation

Deep Study has been iterated through behavioral prompts, rubric grading, human review, and live-canvas examples. The current evidence is useful but deliberately bounded.

## What the current suite checks

The curated prompts cover:

- novice and advanced Guided Tutor openings;
- quiet Study Companion starts and retrieval-first returns;
- source-grounded misconception repair;
- first and second “I don't know” behavior;
- a genuinely curious Teach-Back Student rather than a disguised lecturer;
- natural movement between the three relationships;
- permission before elaborate visuals;
- live, editable, staged Excalidraw canvases with readable rendered output.

The public prompt and rubric files are in [`evals`](evals).

## Current acceptance result

The final selected cross-skill transition and live-canvas acceptance runs passed **17/17** rubric checks:

| Acceptance run | Passed |
| --- | ---: |
| Guided Tutor transition | 4/4 |
| Study Companion live recall map and teach-back transition | 6/6 |
| Teach-Back Student live provisional model and tutor transition | 7/7 |

The broader skill-specific suites also reached full pass rates for the selected with-skill runs.

## What that result means

It means the tested outputs satisfied the written behavioral rubrics in those runs. These are end-to-end **acceptance tests** for the skills, canvas mechanics, and transitions.

## What it does not mean

The 17/17 result is **not causal** evidence that:

- the skill caused every successful behavior;
- Deep Study outperforms an unassisted current model on natural prompts;
- the old skill versions could not pass the same scenarios;
- the product improves learner retention or transfer in real use.

Several transition and canvas prompts explicitly described the desired behavior. In some old-versus-new comparisons, both versions passed. Those tests are demanding system checks, but they do not isolate the effect of the revised skill text.

## Planned stronger comparison

After the packaged plugin works in a fresh installation, the next evaluation should include:

1. natural, minimal prompts that do not prescribe the desired pedagogy;
2. a pedagogy-isolation comparison with the same available tools and only the Deep Study instructions changed;
3. a whole-product comparison between stock ChatGPT/Codex and the installed plugin;
4. multiple runs per prompt;
5. blind grading and qualitative human review;
6. positive and negative activation cases;
7. learner-centered outcomes where feasible, such as delayed retrieval and transfer.

The goal is a sharper comparison earned by better experimental design, not by sabotaging the baseline.

