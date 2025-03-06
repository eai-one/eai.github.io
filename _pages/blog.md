---
layout: default
title: Blog
permalink: /blog/
---

<h1>Latest Posts</h1>

  <ul>
    {% for post in paginator.posts %}
      <li>
        <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
        {{ post.excerpt }}
      </li>
    {% endfor %}
  </ul>

<!-- Pagination Links -->
  <div class="pagination">
    {% if paginator.previous_page %}
      <a href="{{ paginator.previous_page_path }}" class="prev">&laquo; Previous</a>
    {% endif %}

    <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>

    {% if paginator.next_page %}
      <a href="{{ paginator.next_page_path }}" class="next">Next &raquo;</a>
    {% endif %}
  </div>

