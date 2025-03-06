---
layout: default
permalink: /
---

<section>
<h1 style="text-align: left; font-size: 2rem;"> {{ "Embodied AI" | uppercase }} </h1>
<div>
An area of artificial intelligence focused on agents that interact with the world through a physical (or simulated) body. Embodied AI goes beyond purely abstract computational tasks by integrating perception (sight, hearing, touch, etc.), action (motor control), and decision-making to learn from and adapt to changing environments.
<img src="/assets/images/embodied-ai-robot.png" alt="Futuristic Humanoid AI Robot" style="width:100%; max-width:500px; display:block; margin:auto; border-radius:10px;">
</div>
</section>

<section style="text-align: center; padding: 50px 20px; background: linear-gradient(to right, #1a1a1a, #333); color: white;">
    <h1 style="font-size: 2.5rem; margin-bottom: 10px;">Welcome to Embodied AI Blog</h1>
    <p style="font-size: 1.2rem; max-width: 600px; margin: auto;">
        Exploring the intersection of artificial intelligence and physical interaction with the world.
    </p>
    <a href="/about" style="display: inline-block; margin-top: 20px; padding: 12px 24px; background: #f0a500; color: #fff; text-decoration: none; font-size: 1.1rem; border-radius: 5px;">
        Learn More
    </a>
</section>

<section style="padding: 40px 20px;">
    <h2 style="text-align: left; font-size: 1.5rem;">Latest Posts</h2>
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">

    {% for post in site.posts limit:2 %}

    <div style="max-width: 500px; padding: 15px; text-align: center;">
        <h3>
        <a href="{{ post.url }}" style="text-decoration: none; color: #333;">{{ post.title }}</a>
        </h3>
        <p style="color: #777;">{{ post.excerpt | truncatewords: 20 }}</p>
        <a href="{{ post.url }}" style="color: #f0a500; text-decoration: none;">Read More →</a>


    {% endfor %}
