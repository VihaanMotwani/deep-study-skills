# Research basis

Deep Study is an evidence-informed synthesis. Its component techniques have research support; the exact three-skill conversational system has not itself been validated in a controlled learning-outcomes study.

## Why three learning relationships?

The divisions are functional rather than taxonomic:

1. **Guided Tutor:** the AI supplies and adapts the instructional path.
2. **Study Companion:** external material supplies the path; the AI supports and checks learning.
3. **Teach-Back Student:** the learner supplies the explanation; the AI's provisional understanding becomes the object being tested.

These relationships create different responsibilities, failure modes, and conversational behaviors. They are not claimed as the only scientifically valid modes of learning.

## Guided Tutor

The tutor follows `model → scaffold → fade → retrieve`.

- **Worked examples, self-explanation, and fading.** Atkinson, Renkl, and Merrill found that self-explanation prompts combined with faded worked-out steps improved near and far transfer without more time on task. This supports showing a representative solution, asking the learner to explain consequential steps, and progressively removing support.  
  Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). [Transitioning from Studying Examples to Solving Problems](https://eric.ed.gov/?id=EJ678596).
- **Constructive and interactive engagement.** The ICAP framework distinguishes passive reception from active, constructive, and interactive engagement. It supports having the learner generate explanations, predictions, and inferences instead of only consuming a polished answer.  
  Chi, M. T. H., & Wylie, R. (2014). [The ICAP Framework](https://www.tandfonline.com/doi/abs/10.1080/00461520.2014.965823).
- **Retrieval practice.** Retrieval of studied prose produced stronger delayed retention than repeated study in Roediger and Karpicke's experiments, despite repeated study sometimes looking better immediately. This supports ending a cycle with reconstruction rather than another visible summary.  
  Roediger, H. L., & Karpicke, J. D. (2006). [Test-Enhanced Learning](https://doi.org/10.1111/j.1467-9280.2006.01693.x).
- **Adaptive assistance.** Expertise-reversal research indicates that support useful to novices can become redundant for higher-prior-knowledge learners. This supports diagnosing briefly and fading or restoring help based on demonstrated performance.  
  Wiedbusch et al. (2025). [A cornerstone of adaptivity](https://www.sciencedirect.com/science/article/pii/S0959475225000660).

## Study Companion

The checkpoint follows `unaided recall → probe → apply → source check → repair → retrieve again`.

- **Retrieval before review.** The testing effect supports asking the learner to reconstruct before seeing a summary. A meta-analysis of practice testing likewise found a general learning benefit relative to non-testing conditions, with outcomes depending on feedback and test design.  
  Roediger & Karpicke (2006), above.  
  Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). [Rethinking the Use of Tests](https://doi.org/10.3102/0034654316689306).
- **Constructive follow-up.** ICAP supports following recall with explanation, application, comparison, or prediction rather than reducing a checkpoint to recognition questions.
- **Correction after generation.** Deep Study lets the learner attempt recall, then checks against the source and asks for a repaired retrieval. This is a design synthesis: it seeks the benefit of generation without leaving consequential errors uncorrected.

The decision to wait for the learner to return is a portability and autonomy choice. Research does not establish that every learner needs a fixed Pomodoro, an automatic interruption, or a particular interval.

## Teach-Back Student

The cycle follows `teach → question → student attempt → accuracy review → reteach → retry`.

- **Learning by teaching.** Kobayashi's meta-analysis found positive effects from preparing to teach and larger effects from teaching after preparation; interactive teaching showed larger effects than noninteractive teaching. This supports an AI student that asks questions and attempts to use what it was taught rather than serving as a silent audience.  
  Kobayashi, K. (2019). [Learning by preparing-to-teach and teaching](https://onlinelibrary.wiley.com/doi/full/10.1111/jpr.12221).
- **Knowledge building rather than retelling.** Roscoe and Chi distinguish productive explanation and questioning from simple knowledge-telling. This supports questions about relationships, causes, implications, and examples.  
  Roscoe, R. D., & Chi, M. T. H. (2007). [Understanding Tutor Learning](https://eric.ed.gov/?id=EJ782047).
- **Teachable agents.** Betty's Brain has learners build a causal model that a simulated student reasons from, inspect the student's performance, and revise the model. This supports separating the student's provisional understanding from transparent expert accuracy review.  
  Biswas et al. [Betty's Brain overview and classroom discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC6473007/).
- **Checkpointed correction.** AHRQ's clinical teach-back work is not the same pedagogy, but its “chunk and check” practice is relevant to timing: repair consequential misunderstandings after a manageable segment rather than interrupting every sentence or postponing all correction.  
  Agency for Healthcare Research and Quality. [Use the Teach-Back Method](https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html).

## What is a product-design inference?

Research does not directly validate:

- the exact wording or personality of the AI;
- the three-mode bundle as a whole;
- live Excalidraw whiteboarding as a universal learning improvement;
- one-question-per-turn as an optimum for every learner;
- the specific two-step “I don't know” support ladder;
- automatic improvement in grades, exam performance, or long-term retention.

Those choices translate broader findings into an AI conversation. They should be judged through behavior tests now and learner-outcome studies later.

