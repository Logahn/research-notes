# Multimodal Machine Learning 11-777
Louise-Phillipe Morency

Tokenization is an important part of multimodal machine learning

Multimodal means multimodalities and we often define them based on how humans can perceive their environments.
There have been improvements in technology and thus an increase in the modalities available to machines.

**Human centric modalities:**
- Language
- Acoustic: Intonation, voice quality, expressions
- Visual: Gestures, Body language, eye contact, facial expression.

**Machine centric modalities:**
- Touch: Hepatics and Motion
- Physiological: Skin conductance, electrocardiogram
- MObile: GPS, accelerometer, light sensors

Modality is the way something is perceived.

There are modalities that are raw-er than others which can be called abstract. The raw ones are closer to the sensors than others. There is a spectrum to modality and this is determined by how easily they are interpritable to the sensors.

Multimodal is the scientific study of heterogeneous (because modalities are different instructures and representations) and interconnected (connected and interacting) data.

Modalities interconnection:
The interconnection of multimodality is broken down into 
- **Connection**: Independent of the fact that we are gonna fuse information from two modalities, **how much is shared berween them before fusion?** It focuses in shared information between modalities discarding the uniqueness of the information in different modalities.
There are two ways to connect modalities: 
1. Statistical: Association(co-occurence), Dependency(asynchronous)
2. Semantic: Correspondence (This is human driven and more referred to as grounding), Relationship(how info from one modality is used for info in another modality)

- **Interaction**:  Interaction is a process affecting each modality to create new responses. Interactions happen during inference. 
 
## Core research challenges in multimodal learning:
1. *Representation* studies how to represent and summarize multimodal data to reflect the heterogeneity and interconnections between individual modality elements. 
2. *Alignment* aims to identify the connections and interactions across all elements.
3. *Reasoning* aims to compose knowledge from multimodal evidence usually through multiple inferential steps for a task.
4. *Generation* involves learning a generative process to produce raw modalities that reflect cross-modal interactions, structure, and coherence.
5. *Transference* aims to transfer knowledge between modalities and their representations.
6. *Quantification* involves empirical and theoretical studies to better understand the multimodal learning process.

### Principles of modalities:
- Modalities are heterogeneous cause they have diverse qualities, structures and representations.
- Modalities are connected since they are often related.
- Modalities interact to give rise to new information during inference. 

### Coming up with good research ideas (The scientific methods)
1. Initial observations and ideas
2. Literature review
3. Research questions and hypothesis
4. Test with experiments
5. Analyze data
6. Report conclusions

Come up with a Yes-No question, a hypothesis(falsifiable / verifiable) and a reason why you think it will be true or not true.

Avoid questions like "Does cross-attention improve performance on this dataset?" The answer is usually Yes, but you cannot say why.

Instead, phrase your questions like this: "Is the alignment between modalities really necessary in this dataset?" Now you analyse data and see if cross alignment is necessary or not.

## Multimodal navigation datasets:
- VNLA
- nuScenese
- Waymo
- Agroverse
- Room-to-room
- Room-across-room (RxR) *
- Winoground *