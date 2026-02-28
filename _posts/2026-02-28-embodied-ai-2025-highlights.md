---
layout: post
title: "Embodied AI in 2025: A Year of Breakthroughs"
date: 2026-02-28 00:00:00 +0900
comments: false
categories: embodied-ai vla humanoid-robots foundation-models
---

It has been almost a year since our last post. A lot has happened in the world of embodied AI. This post is a catch-up covering the most significant developments from 2025 — a year that may well be remembered as the inflection point where AI truly entered the physical world.

---

**Vision-Language-Action (VLA) Models**: The most consequential architectural shift of 2025 was the rapid maturation of VLA models. These models bridge the gap between language understanding and physical action, allowing robots to interpret high-level natural language instructions, reason about their environment, and execute complex manipulation tasks — all within a single unified architecture. VLA models build on pretrained Vision-Language Models (VLMs) by fine-tuning them on robot demonstration data, inheriting their open-world generalization capabilities.

Key VLA models that defined the year:

1️⃣ **π₀ (Pi Zero) — Physical Intelligence**

π₀ is a flow-matching-based VLA built on Google's PaliGemma VLM, capable of generating smooth, high-frequency action trajectories at around 50 Hz. What makes π₀ particularly noteworthy is the complexity of the tasks it can handle: behaviors that combine both physical dexterity and long-horizon combinatorial planning — such as folding laundry from any starting configuration, a task that can run for tens of minutes. In 2025, the π₀ family expanded with **π₀.5** (focused on open-world generalization) and **π₀.6** (a model that learns from experience), each pushing the frontier of what a general-purpose robot policy can do.

2️⃣ **OpenVLA — Open-Source Democratization**

OpenVLA (Stanford) is a 7-billion parameter open-source VLA trained on ~970,000 robot episodes from the Open X-Embodiment dataset, covering 22 different robot embodiments. It frequently outperforms Google's RT-2 on manipulation benchmarks and supports parameter-efficient fine-tuning. Its open availability has become a catalyst for the research community, lowering the barrier to entry for robotics research. The **OpenVLA-OFT** extension, released in March 2025, further improved fine-tuning efficiency for specific deployments.

3️⃣ **GR00T N1 — NVIDIA's Open Humanoid Foundation Model**

Released in March 2025, NVIDIA's GR00T N1 is a foundation model specifically designed for generalist humanoid robots. It is notable not only for its capabilities but also for being open, providing the community with a strong starting point for humanoid robot control research. NVIDIA's NitroGen model, trained on 40,000+ hours of human gameplay data, also demonstrated that embodied reasoning techniques transfer across domains — from video game play to robot navigation.

4️⃣ **SmolVLA — Compact Models for Everyone**

HuggingFace's SmolVLA (~450M parameters) demonstrated that capable robot policies do not require massive compute. Designed to run on consumer-grade hardware and integrated with the LeRobot library, SmolVLA is an important step toward democratizing robotics research beyond well-funded labs.

---

**Humanoid Robots Move from Labs to the Real World**

2025 was the year humanoid robots stopped being curiosities and started being deployed. Companies like Tesla, 1X, and Figure have moved their humanoid robots into manufacturing, logistics, and service roles — sorting packages, assembling components, and assisting with inventory management.

✅ **Tesla Optimus**: In October 2025, Tesla unveiled significant updates to Optimus with advances in dexterity, balance, and object manipulation. Tesla's strategy relies heavily on simulation-to-real transfer: Optimus trains in large-scale simulated environments before behaviors are transferred to physical hardware, dramatically reducing real-world training time.

✅ **Unitree Robotics**: Perhaps the most disruptive development was on cost. Unitree's G1 humanoid launched at $16,000 — compared to industrial robot systems costing $500,000 just two years prior. Their R1 followed at $5,900. These robots combine reinforcement learning and large language models for real-time interaction, and their pricing signals that robotics is entering a Moore's Law-style cost compression curve that will continue to accelerate adoption.

---

**Tactile Intelligence — The Final Dexterity Frontier**

One of the persistent gaps in robotics has been the inability to handle objects that require nuanced touch — soft, fragile, or irregularly shaped items. 2025 saw meaningful breakthroughs in tactile sensing, enabling robots to handle a grape as carefully as a power tool. This dexterity gap had long blocked embodied AI from entering fields like electronics assembly, food handling, and surgical assistance. Solving it opens a significant surface area of real-world deployment.

---

**Key Technical Trends**

•	**Flow Matching & Diffusion**: These two techniques emerged as the most effective ways to train transformer-based policies to generate continuous action sequences. Originally developed for image generation, both flow matching (used in π₀) and diffusion processes (used in other policy architectures) have transferred cleanly to the action generation domain.

•	**Scaling Laws in Robotics**: Research this year clarified that scaling in robotics depends less on the number of demonstrations and more on the diversity of environments and objects encountered during training. Most existing robot datasets are collected in constrained lab settings — suggesting that real-world deployment and broader data collection pipelines will be the key unlock for the next capability jump.

•	**Simulation & Digital Twins**: Citi Research identified three pillars underpinning Physical AI progress: digital twin models, real-world edge data collection, and simulation. Simulation environments allow robots to practice millions of scenarios that would be impractical or dangerous to replicate physically. Digital twins enable AI systems to learn and optimize in virtual representations before deployment.

•	**Chain-of-Thought for Robots**: CoT-VLA (CVPR 2025) extended chain-of-thought reasoning — familiar from language models — into the VLA domain, enabling robots to reason step-by-step before executing actions. This is a meaningful step toward more interpretable and reliable robot decision-making.

---

**What This Means Going Forward**

The convergence of three forces is what makes 2025 a genuine inflection point for embodied AI:

1.	**Foundation models** that transfer general knowledge into robot policies (VLAs, GR00T, π₀)
2.	**Hardware cost compression** that brings humanoid robots into economically viable deployment
3.	**Sensing and dexterity advances** that unlock new categories of physical tasks

The gap between what robots can do in controlled research settings and what they can do in the real world is narrowing fast. The period ahead will be about scaling deployment, generating real-world data, and closing the remaining gap between human dexterity and robotic capability.

There is a lot more to cover. We will be back with deeper dives into specific topics — starting with VLA architectures, world models, and what sim-to-real transfer actually looks like in practice.
