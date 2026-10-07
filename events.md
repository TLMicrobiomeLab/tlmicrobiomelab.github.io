---
layout: default
title: Lab News & Events
description: Conference presentations, milestones, and social outings from the TLMR Lab.
permalink: /events/
---

<div class="container">
    <div class="page-header">
        <span class="eyebrow">News &amp; events</span>
        <h1>Lab News &amp; Events</h1>
        <p class="lead">Updates from the lab, conferences, and social outings.</p>
    </div>

    {% assign events = site.events | sort: "date" | reverse %}
    {% for event in events %}
    <article class="event" id="{{ event.date | date: '%Y-%m-%d' }}">
        {% if event.hero %}<div class="event-side">
            <div>
                <img src="{{ event.image | relative_url }}" alt="{{ event.title }}" loading="lazy">
                <p class="caption">{{ event.title }}</p>
            </div>
            <div>{% endif %}
        <div class="event-head">
            <span class="event-date"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>{% if event.date_display %}{{ event.date_display }}{% else %}{{ event.date | date: "%B %-d, %Y" }}{% endif %}</span>
            {% if event.tag %}<span class="tag">{{ event.tag }}</span>{% endif %}
            <h2>{{ event.title }}</h2>
        </div>
        {{ event.content }}
        {% if event.hero %}</div>
        </div>{% endif %}
    </article>
    {% endfor %}
</div>
