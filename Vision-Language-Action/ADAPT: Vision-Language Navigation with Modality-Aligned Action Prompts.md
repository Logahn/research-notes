## ADAPT: Vision-Language Navigation with Modality-Aligned Action Prompts

Vision-Language Navigation (VLN) is a challenging task
that requires an embodied agent to perform action-level
modality alignment, i.e., make instruction-asked actions se-
quentially in complex visual environments.

When starting navigation, the instruction-related
action prompt set is retrieved from a pre-built action prompt
base and passed through a prompt encoder to obtain the
prompt feature. Then the prompt feature is concatenated
with the original instruction feature and fed to a multi-layer
transformer for action prediction.

Start -> Instruction prompt retrieval -> Prompt feature + instruction feature -> Multilayer transformer -> Action prediction.

To collect high-quality
action prompts into the prompt base, we use the **Contrastive
Language-Image Pretraining (CLIP) model which has pow-
erful cross-modality alignment ability.**

Focus on Navigation for in-home robots and personal assistants.

**Baseline:** Vln bert: A recurrent vision-
and-language bert for navigation.

VLN agents still learn the action-
level modality alignment in an implicit way, which largely
limits the robust action decision under different scenes.

Experiment is based on being explicit in the provision of prompts to agents (task-specific objectives)

_To this end, we propose modAlity-aligneD Action PrompTs
(ADAPT), where the agent is provided with explicit action
prompts to make action decision._

Action prompt -> {image subprompt + text sub-prompt} (Multimodal sub-prompts)

Did experiments using 2 benchmarks. R2R and RxR benchmarks. R- Room
Experiments show that introducing explicit action prompts is promising for improving agent's navigation performance.
VLNBERT adds a recurrent function to help the agent recognize time-dependent input.

For obtaining the text sub-prompt, we use a simple
nearest-verb-search scheme, that is, finding the nearest verb
(which is in a pre-built verb vocabulary) just before a spe-
cific object/location word.

**Limitations:** With regards to the limitation of our work, our constructed action prompt base in ADAPT contains more or
less noise due to the ability of CLIP, the scene complexity
and instruction diversity in the VLN task. The future work
includes finding action prompts of better quality.

Implementation: [ADAPT](https://github.com/expectorlin/ADAPT)

Baseline
Limitations
Reasons for the work
Build upon the work
