---
layout: default
title: Blog
permalink: /blog/
---
<h1>Latest Posts</h1>

{% if page.url == "/blog/" %}
  {% for post in site.posts %}
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p>{{ post.excerpt }}</p>
  {% endfor %}
{% endif %}