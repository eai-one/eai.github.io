---
layout: post
title: "Flow Matching Is Replacing Diffusion Policy — Here's the Mechanism"
date: 2026-03-01 00:00:00 +0900
comments: false
categories: embodied-ai flow-matching learning-from-demonstration
---

The action generation layer of robot learning has quietly undergone a revolution in the past eighteen months. **Diffusion Policy** — Chi et al.'s 2023 paper that demonstrated score-based generative models could handle the multimodal, high-dimensional distributions that plague imitation learning — was a genuine breakthrough. But the field is now migrating to something faster, simpler to train, and better suited to the latency demands of real hardware: **flow matching**. Understanding why this transition is happening, and what it unlocks, matters whether you're building manipulation systems or trying to read the next wave of robotics papers.

1️⃣ **What Diffusion Policy actually solved — and where it strains**

Before diffusion, robot policies trained with behavioral cloning collapsed in the face of multimodal demonstrations. If a human teleoperator sometimes grasps left, sometimes right, the policy averaged the two and grasped nowhere. Diffusion Policy solved this elegantly: by modelling the action distribution as a reverse-denoising process, the policy could represent sharp, distinct modes. The UNet and Transformer variants both worked. The problem is inference. A standard **DDPM** sampler requires 100 denoising steps; DDIM pushed that down to 10–25. At a control frequency of 10–30 Hz, spending 30–80 ms per action generation is expensive and, on edge hardware, often infeasible. Researchers worked around this with chunked action execution — predict a sequence of future actions, execute them open-loop, re-plan — but this trades responsiveness for throughput.

2️⃣ **Flow matching: straight paths, fewer steps**

**Conditional Flow Matching (CFM)**, introduced by Lipman et al. in 2022 and operationalized in robotics primarily through **rectified flow** variants, learns a velocity field that transports samples from a simple prior (Gaussian noise) to the data distribution along approximately straight trajectories. In contrast to the curved, Langevin-diffusion paths that DDPM traces, these near-linear paths can be integrated accurately in as few as 4–8 function evaluations without quality collapse. The training objective is also cleaner: instead of matching a score function via denoising, you regress directly onto the velocity field connecting noise to data, which turns out to be lower-variance and faster to converge. On policy benchmarks, CFM-based policies match or exceed diffusion policy on task success while cutting inference cost by 3–5×.

3️⃣ **π₀ as the proof of concept at scale**

Physical Intelligence's **π₀** (Black et al., 2024) is the highest-profile demonstration of this shift. Built on a PaliGemma vision-language backbone and fine-tuned with a flow-matching action head, π₀ handles dexterous, contact-rich tasks — folding laundry, assembling boxes, bussing tables — that previous VLA architectures failed on. The flow matching head is central to why it works at real hardware speeds: generating a 50-step action chunk takes under 10 ms on the onboard compute they target. **OpenVLA-OFT** (open-source, University of Michigan, late 2024) followed a similar path, adding a flow-matching fine-tuning stage that meaningfully improved dexterous manipulation over the base VLA. The pattern is becoming a template.

4️⃣ **What the next iteration looks like**

The frontier now is **consistency models** applied to robot actions — single-step generation with quality competitive to multi-step flow matching, by distilling a trained flow model. Early results from labs including CMU and Stanford suggest this is viable and would push inference to sub-millisecond territory, finally decoupling action generation from the control loop entirely. Paired with **hierarchical** architectures that run slow language-level planning and fast flow-based reactive control at different timescales, you start to see the shape of a genuinely capable manipulation stack. The move from diffusion to flow matching isn't hype-driven churn — it is the field resolving a real engineering tension between expressiveness and speed, and the papers landing in 2026 will assume this foundation.
