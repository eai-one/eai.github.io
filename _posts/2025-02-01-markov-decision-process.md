---
layout: post
title: "Markov Decision Processes"
date: 2025-02-01 00:00:00 +0900
comments: false
categories: embodied-ai markov-decision-process
---

**Markov Decision Processes:**
PART I - **What Is an MDP?**
A Markov Decision Process is a mathematical framework that helps make good decisions when outcomes aren’t 100% certain. While it sounds complicated, the main idea is straightforward:

1.	You have a situation (called a state).

2.	You can choose something to do (called an action).

3.	There’s a chance you’ll end up in a new situation because of your choice (that’s the transition).

4.	You earn some type of “score” (called a reward) depending on that choice.

The goal in an MDP is to figure out how to make decisions (which actions to take) to maximize the total reward over time.

How Do We Figure Out the Best Choices?

In an MDP, researchers or programmers often use algorithms to test different strategies (sometimes called policies) to see which one yields the highest reward. A policy is basically a rule saying, “Whenever I’m in this state, I’ll choose this action.” By trying out different policies, we can find the one that maximizes our long-term benefit.

One common method is Dynamic Programming, where you start from the end and work backward, estimating how valuable each state is. Another popular technique is Reinforcement Learning: the AI tries actions, sees what reward it gets, and gradually learns which actions work best over time—very much like trial and error in real life.

Why MDPs Are Cool

•	They’re Everywhere: From robotics and gaming to scheduling apps and self-driving cars, MDPs form the backbone of many decision-making systems.

•	They’re Adaptable: You can customize the “reward” depending on what you care about. Want to save time? Make reward = negative minutes spent. Want to earn points? Make reward = points collected.

•	They Help You Plan: An MDP can be a powerful tool for planning ahead. Even if you’re not coding, thinking about the future as a series of states and rewards can guide you to smarter decisions in school, clubs, or personal goals.

Takeaways
	1.	State: Where you are (or what’s happening) right now.
	2.	Action: What you decide to do next.
	3.	Transition: The probability of moving to a new state after your action.
	4.	Reward: The score or benefit you receive.

When you look at life through the lens of MDPs, you can break down your big decisions into simpler parts. Think about the states you might land in, the actions that could get you there, and the rewards you care about most.

PART II -

MDPs in a Nutshell

Formally, an MDP is defined by the tuple (S, A, P, R, \gamma):

•	￼S: A (possibly infinite) state space capturing all relevant configurations of the system.

•	￼A: An action space representing the set of all possible choices the decision-maker (or agent) can take.

•	￼P(s{\prime} \mid s, a): A state-transition probability that encodes how likely you are to land in state ￼ if you take action ￼ in state.

•	￼R(s, a) (or sometimes R(s, a, s{\prime}))): A reward function signifying the immediate benefit (or cost) received for taking action ￼ in state.

•	￼\gamma: A discount factor (0 < \gamma < 1) that weights the relative importance of future rewards versus immediate ones.

The Markov assumption states that transitions and rewards depend only on the current state and action, not on the history of how we arrived there. Though real-world systems often violate strict Markov properties, MDPs remain a powerful and tractable approximation.

The Bellman Equation

A cornerstone of MDPs is the Bellman equation, which provides a recursive relationship for the value function.
￼

V^\pi(s) \;=\; \mathbb{E}\bigl[R(s, \pi(s)) + \gamma\,V^\pi(S{\prime})\bigr],

From there, you can derive critical algorithms such as value iteration and policy iteration, which systematically converge to an optimal solution under appropriate conditions (e.g., a finite or discounted infinite-horizon MDP).

Key Solution Methods

1.	Value Iteration
This approach iteratively refines an estimate of the optimal value function V by applying the Bellman optimality update. After enough iterations (or until convergence within a defined tolerance), the derived greedy policy with respect to V￼ is optimal.

2.	Policy Iteration
Policy iteration alternates between policy evaluation—computing the value function of a given policy—and policy improvement—updating the policy by selecting actions that yield higher value. It often converges in fewer iterations but each iteration can be more computationally expensive than value iteration.

3.	Approximate Dynamic Programming
When the state space S is very large (or even continuous), classic value iteration or policy iteration becomes computationally infeasible. Approximate methods (function approximation, neural networks, basis functions) help handle large-scale or continuous MDPs.

4.	Model-Free Methods
In many real-world scenarios, we do not have a perfect model of P(s{\prime}|s,a) or R(s,a). Reinforcement learning (RL) methods like Q-learning or actor-critic approaches learn optimal policies from data by sampling transitions and rewards.

Discounting and Horizon Considerations

•	Finite Horizon: MDPs that end after a fixed number of steps T. Solutions often use backward induction to compute an optimal policy for each time step.

•	Infinite Horizon, Discounted: Uses a discount factor \gamma to ensure the sum of expected future rewards converges. Much of classical RL and control theory relies on this setting because it’s amenable to stable solutions (e.g., convergence proofs for value iteration and policy iteration).

•	Average-Reward Criterion: Instead of discounting, another perspective focuses on maximizing the long-run average of rewards. This framework is sometimes used in ongoing processes where discounting the future may not be as relevant.

Extensions: Beyond Basic MDPs

1.	Partial Observability (POMDPs)
In many real systems, the agent doesn’t directly observe the true state; it only gets observations. POMDPs introduce a belief space representation and generally involve higher computational complexity, but they more accurately model many real-world scenarios (e.g., robotics with noisy sensors).

2.	Constrained MDPs
Some tasks require satisfying constraints (energy usage, safety limits). Constrained MDPs incorporate these additional variables—leading to specialized solution methods like Lagrangian relaxation or primal-dual optimization.

3.	Hierarchical MDPs
Large problems can be decomposed into simpler “sub-MDPs.” Hierarchical frameworks (e.g., Hierarchical RL) reduce the decision space by grouping actions into higher-level “options,” facilitating more scalable solutions.

4.	Multi-Agent MDPs (or Stochastic Games)
When multiple decision-makers interact, the dynamics extend to multi-agent settings. Cooperative or competitive behaviors, equilibrium solutions (e.g., Nash equilibrium), and communication protocols emerge as additional complexities.

Applications in the Real World

•	Robotics Control: Trajectory optimization, manipulation tasks, and real-time feedback often rely on MDP formulations (though approximate methods are common due to high dimensionality).

•	Supply Chain & Operations Research: Inventory management, logistics, and scheduling problems use MDP-based or approximate dynamic programming techniques to balance costs and service levels.

•	Healthcare: Treatment policies can be framed as MDPs (e.g., deciding medication dosage), optimizing patient outcomes under uncertainty in disease progression.

•	Finance: Portfolio management, risk assessment, and algorithmic trading often involve Markov processes with uncertain returns.

Challenges and Frontiers

•	Scalability: Exact solutions scale poorly with increasing state and action spaces. Approximate solutions, hierarchical structures, or sampling-based algorithms are crucial for tackling large or continuous MDPs.

•	Robustness: Real systems deviate from ideal assumptions. Model errors, parameter uncertainties, and adversarial perturbations can degrade policy performance.

•	Multi-Criteria Optimization: Balancing multiple objectives (e.g., cost, reliability, user satisfaction) requires more nuanced formulations like vector-valued rewards or constrained MDPs.

•	Safety & Verification: In safety-critical domains (autonomous driving, industrial robotics), verifying that an MDP policy meets stringent safety criteria is an active and challenging research area.

