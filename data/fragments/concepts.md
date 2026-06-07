## Concepts

A 60-second taxonomy, distilled from the surveys below:

- **By substrate.** *Parametric* memory lives in model weights (fine-tuning, model
  editing, memory layers). *Contextual* (token-level) memory lives outside the
  model and is fed through the context window (RAG stores, memory engines,
  scratchpads). *Latent* memory lives in hidden states and KV caches.
- **By function.** *Working* memory is the active context of the current task.
  *Episodic* memory records what happened (events, sessions, trajectories).
  *Semantic* memory stores facts and knowledge. *Procedural* memory captures
  skills and how-to knowledge (prompts, code, workflows).
- **By lifecycle.** Memory systems differ in how they *write* (extraction,
  summarization), *index* (vectors, graphs, profiles), *retrieve* (semantic,
  temporal, multi-hop), *update* (conflict resolution, versioning) and *forget*
  (decay, eviction, consolidation).

Most production systems today are contextual episodic-plus-semantic stores with
vector or graph indexes; most open research problems sit in lifecycle operations
(consolidation, forgetting, self-organization) and in pushing memory back into
parameters and latents.
