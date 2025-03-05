---
layout: default
title: Blog
permalink: /blog/
---
<h1>Latest Posts</h1>

{% if page.url == "/blog/" %}
<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
{% endif %}