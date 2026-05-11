---
layout: post
title: "The Horizon Problem: Why Robots That Can Grasp Still Can't Make Breakfast"
date: 2026-05-11 21:25:01 +0200
comments: false
categories: embodied-ai control-planning foundation-models
---

The demo reel looks extraordinary. π₀ folds laundry. GR00T assembles a kit. OpenVLA transfers objects between containers with a fluency that would have seemed impossible three years ago. But hand any of these systems a task that requires fifteen sequential steps — say, clearing a table, loading a dishwasher, and wiping the counter — and the policy falls apart somewhere around step four. This is the **long-horizon execution problem**, and it is quietly the hardest open challenge in embodied AI right now.

1️⃣ **What "long-horizon" actually means — and why it's structurally different**

The distinction is not merely about task length. A **long-horizon task** requires maintaining consistent intent across a sequence where each step changes the world state, errors compound, and the agent must sometimes detect and recover from failure before proceeding. Short-horizon policies — even excellent ones — operate in a fundamentally different regime. They are trained and evaluated on episodes of two to thirty seconds. Their implicit "memory" is the observation window, typically one or a few frames. They have no representation of what has already been accomplished or what remains to be done. This is a category difference, not a scaling problem. Throwing more demonstration data at a standard VLA architecture does not solve it.

2️⃣ **Why the current generation of VLA architectures structurally fails here**

**Vision-Language-Action models** as currently designed — transformer backbones predicting action tokens conditioned on image and language — have no explicit state tracker. Every inference step is memoryless beyond what fits in the context window. This creates three failure modes. First, **error accumulation**: a small grasp miscalibration at step three shifts the world state just enough that step four's conditioning is out of distribution, and the policy hallucinations compound. Second, **goal drift**: without an explicit representation of completed sub-tasks, the policy may re-attempt actions it has already executed. Third, and most insidious, **missing replanning**: if a cup breaks or an object falls off the table, no current end-to-end VLA triggers a recovery branch. The policy simply continues issuing actions into an environment that no longer matches its implicit assumptions. Google DeepMind's SayCan work and the Code as Policies lineage tried to address planning with LLMs-as-orchestrators, but the interface between symbolic planner and low-level reactive policy remains fragile under real execution noise.

3️⃣ **The approaches gaining traction**

Three directions are producing real traction. **Hierarchical policy architectures** — a slow high-level planner emitting subgoals, a fast reactive controller executing them — restore explicit state tracking at the planning layer. Work like SERL and more recent subgoal-conditioned VLA variants from Stanford and CMU are proving this out in contact-rich domains. **Task and Motion Planning integration**, long considered too brittle for unstructured environments, is being rehabilitated by combining neural feasibility estimators with classical TAMP solvers: the neural component handles perception uncertainty while the symbolic layer enforces task-level consistency. And **language-conditioned replanning**, where a world model or VLM monitors execution and triggers re-planning when predicted versus observed states diverge, is emerging from labs at Berkeley and ETH Zurich as the missing error-recovery layer.

What all three share is explicit sequencing state that persists across the episode — something end-to-end imitation learning cannot extract from short-horizon demonstration data alone.

The field spent 2024–2025 solving the manipulation primitive. The next phase is about **temporal scaffolding**: how a robot tracks what it has done, detects when it has failed, and re-plans without human intervention. The labs that crack this won't just build better demos. They'll build the first robots that can actually be left alone in a kitchen.
