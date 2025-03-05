---
layout: post
title: "Markov Decision Processes"
date: 2025-02-01 00:00:00 +0900
comments: false
categories: embodied-ai markov-decision-process
---

**Markov Decision Processes**

**What Is an MDP?**

A Markov Decision Process is a mathematical framework that helps make good decisions when outcomes aren’t 100% certain. While it sounds complicated, the main idea is straightforward:

1.	You have a situation (called a state).

2.	You can choose something to do (called an action).

3.	There’s a chance you’ll end up in a new situation because of your choice (that’s the transition).

4.	You earn some type of “score” (called a reward) depending on that choice.

The goal in an MDP is to figure out how to make decisions (which actions to take) to maximize the total reward over time.

A High School Example: Choosing Clubs

Let’s imagine you’re choosing which after-school club to join. Each club has different outcomes:

•	Robotics Club: You spend time building cool gadgets. The reward might be learning engineering skills or scoring well in competitions.

•	Drama Club: You learn acting, build confidence, and maybe perform in plays (gaining a different kind of reward).

•	Study Group: You focus on homework, potentially boosting your grades in the future.

Each decision leads to different “states”—maybe you become a better programmer (Robotics Club), improve your public speaking skills (Drama), or raise your GPA (Study Group). If you stick with an MDP mindset, you’re basically tracking your choices, estimating likely outcomes, and aiming for the reward you value most (it might be fun, success, skills, or recognition).

The “Markov” Part

The word “Markov” means your next state depends only on where you are right now, not on how you arrived there. In other words, if you’re deciding whether to join Robotics Club in your sophomore year, that choice mostly depends on your current situation and interests—not what happened back in middle school. Real life can be more complicated, but the Markov assumption keeps things simpler for analysis.

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