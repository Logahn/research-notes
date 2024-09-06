# LARGE LANGUAGE MODELS AS ANALOGICAL REASONERS

## Tasks: 

1. Propose an alternative title.
2. Discuss a missing experiment from the paper.
3. Submit a question about the paper.
4. What social or other impacts were overlooked or omitted?

**Alternative title:**
Analogical Prompting: Best of Zero-shot and Few-shot Chain of Thought

**Missing Experiments from the paper:**
- The work does not include CoT enhancing techniques like self-consistency and least-to-most. Self-comsistency is a strategy which  first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Least-to-most is a strategy which breaks down a complex problem into a series of simpler subproblems and then solve them in sequence.

**Question About the Paper:**
- How can the eneralization gap between high level problems and low-level exemplars be bridged?

**Social and Other Impacts overlooked:** 
- LLMs can repetitively generate identical problems during analogical prompting if not explicitly prompted to generate distinct problems.


**Idea of the paper:**
- For the model to be able to self-generate its own logical exemplars before answering a user's prompt.
- Obviates the need for manually feeding models exemplars
- Combining the strengths of Zero-Shot Chain -of-Thought(CoT) and Few-Shot CoT.

