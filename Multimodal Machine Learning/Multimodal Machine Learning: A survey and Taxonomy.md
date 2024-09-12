Multimodal Machine Learning: A survey and Taxonomy

Modality refers to the way in which something is felt or experienced.
Multimodal machine Learning aims to build models that can process and relate information from multiple modalities.

Purpose of this paper:Identification and exploration of core technical challenges in multimodal machine learning.

Challenges: 
1. Representation: could be interchanged with the term "features" referring to a tensor or vector representation of an entity. A multimodal representation is a representation of data using information from multiple such entities.
the representation should be easy to obtain even in the absence of some modalities, and finally, it should be possible to fill-in missing modalities given the observed ones.
Joint representations combine the unimodal signals into the same representation space, while coordinated representations process unimodal signals separately, but enforce certain similarity constraints on them to bring them to what we term a coordinated space.

To construct a multimodal representation using neural networks each modality starts with several individual neural layers followed by a hidden layer that projects the modalities into a joint space.

The joint multimodal representation is then be passed through multiple hidden layers itself or used directly for prediction.
Similarity models minimize the distance between modalities in the coordinated space.

Joint representations project multimodal data into a common space and are best suited for situations when all of the modalities are present during inference.

Coordinated representations, on the other hand, project each modality into a separate but coordinated space, making them suitable for applications where only one modality is present at test time

We categorize multimodal alignment into two types – implicit and explicit. In explicit alignment, we are explicitly interested in aligning sub-components between modalities.

In technical terms, multimodal fusion is the concept of integrating information from multiple modalities with the goal of predicting an outcome measure.

Multimodal co-learning allows for one modality to influence the training of another, exploiting the complementary information across modalities.

This challenge is exemplified by algorithms such as co-training,
multimodal representation learning, conceptual grounding, and zero shot learning (ZSL).