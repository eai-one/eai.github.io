---
layout: post
title: "The Sim-to-Real Gap Isn't a Physics Problem — It's a Contact Problem"
date: 2026-04-19 17:24:17 +0200
comments: false
categories: embodied-ai sim-to-real manipulation contact-dynamics
---

When **sim-to-real transfer** finally cracked locomotion — ANYmal bounding over rubble, Cassie walking off treadmills, Unitree's G1 handling stairs without a flinch — the conventional wisdom was that dexterous manipulation would follow the same playbook. It hasn't. A decade of parallelised simulation, aggressive **domain randomisation**, and ever-faster physics engines has produced bipeds that can hike and quadrupeds that can dance, but robot hands that can reliably insert a USB connector or unscrew a bottle cap under novel conditions remain unsolved at scale. The reason isn't the quality of the physics engines. It's contact.

1️⃣ **Why locomotion got away with it**

Legged locomotion contacts are brief and periodic. Each footfall lasts tens of milliseconds; the robot's survival criterion is staying upright, not achieving a precise geometric outcome at the interface. Domain randomisation over terrain height, mass, friction, and actuator latency turned out to be sufficient — ETH Zürich's 2019 ANYmal paper crystallised this, and IsaacGym's millions of parallel rollouts made the pipeline almost industrial. The physics doesn't need to be exact. It needs to be varied enough that the policy learns to handle surprise. Manipulation lives in a different regime entirely.

2️⃣ **What makes manipulation contact fundamentally harder**

Dexterous manipulation contact is persistent, multi-point, and outcome-determining. When a gripper closes on an object, the exact distribution of normal and friction forces across the contact surface determines whether the object slips, tips, or moves as intended. That distribution depends on:

• **Contact geometry** — local surface normals at every contact point, which are functions of microscale surface finish, not just CAD geometry
• **Material compliance** — the elastic modulus of fingertip silicone, object shells, and coatings determines how **Hertzian contact patches** actually deform under load
• **Coulomb friction** — notoriously hard to simulate; real surfaces exhibit direction-dependent, history-dependent, and velocity-dependent friction that standard complementarity solvers flatten into a single scalar μ

MuJoCo's implicit complementarity solver and IsaacLab's recent articulation overhaul have meaningfully improved rigid-body fidelity. But "better at rigid bodies" is not the same as "accurate for contact-rich assembly and in-hand manipulation."

3️⃣ **Where the field is converging**

Three approaches are gaining traction, and the most serious labs are running all three in parallel.

✅ **Real-to-sim contact calibration.** Rather than guessing friction and stiffness priors, teams at MIT, Stanford, and CMU are using short real-robot interaction sequences to fit contact model parameters, then randomising around the fit. This narrows the domain gap considerably versus randomising over arbitrary uniform priors.

✅ **Differentiable contact simulation.** NVIDIA Warp and Google's Brax both support differentiable contact dynamics, allowing gradients to flow through contact events into policy parameters. Early results on peg-in-hole and tight-clearance assembly tasks suggest this reduces the sim-to-real gap specifically where contact geometry is predictable and constrained.

✅ **Reactive rather than predictive policies.** The most robust manipulation systems — including **π₀**, recent **ACT** variants trained on ALOHA hardware, and DeepMind's RoboAgent derivatives — succeed partly because they react to contact feedback in real time rather than depending on accurate forward-predicted contact states. Force/torque sensing and fingertip tactile arrays transform unpredictable contact into a recoverable signal rather than a failure mode.

The trajectory is becoming clear. Simulation will keep improving, but the real architectural leverage is in designing policies that don't need perfect contact prediction — systems that use compliance, sensory feedback, and learned recovery behaviours to make contact errors correctable rather than catastrophic. The teams that crack reliable in-hand manipulation at scale will almost certainly get there not by closing the simulation gap entirely, but by building policies robust enough that the residual gap stops mattering.
