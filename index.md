---
layout: default
title: Home
permalink: /
---

<section class="hero">
    <div class="container hero-inner">
        <div>
            <span class="eyebrow">University of Manitoba · Department of Animal Science</span>
            <h1>Decoding the livestock microbiome to improve <em>animal health</em> and <em>sustainability</em></h1>
            <p class="lead">
                The Translational Livestock Microbiome Research (TLMR) Lab studies how livestock hosts and their resident microbes interact, and translates those discoveries into practical solutions for agriculture.
            </p>
            <div class="btn-group">
                <a href="{{ '/projects' | relative_url }}" class="btn btn-primary">Our research</a>
                <a href="{{ '/people' | relative_url }}" class="btn btn-outline">Meet the team</a>
                <a href="{{ '/prospective' | relative_url }}" class="btn btn-accent">Join the lab</a>
            </div>
            <div class="hero-meta">
                <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11a7 7 0 0 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>Winnipeg, Manitoba, Canada</span>
                <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16v16H4z"/><path d="M4 9h16M9 20V9"/></svg>Multi-omics, culturing &amp; modelling</span>
            </div>
        </div>
        <div class="hero-logo">
            <img src="{{ '/images/logo5.png' | relative_url }}" alt="TLMR Lab logo" width="360" height="360">
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">What we do</span>
            <h2>Three pillars of livestock microbiome science</h2>
            <p>We integrate metagenomics, metatranscriptomics, and metabolomics with anaerobic culturing to understand the microbiome and put that understanding to work.</p>
        </div>

        <div class="grid grid-3">
            <a href="{{ '/projects' | relative_url }}#health" class="card pillar">
                <div class="icon-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/></svg></div>
                <h3>Microbiome &amp; Health</h3>
                <p>How early-life microbial colonization shapes immune development and resilience against pathogens in swine and ruminants.</p>
                <span class="more">Learn more →</span>
            </a>
            <a href="{{ '/projects' | relative_url }}#amr" class="card pillar">
                <div class="icon-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg></div>
                <h3>Antimicrobial Resistance</h3>
                <p>Mapping the resistome of livestock environments to develop strategies that reduce the spread of antimicrobial resistance genes.</p>
                <span class="more">Learn more →</span>
            </a>
            <a href="{{ '/projects' | relative_url }}#sustainability" class="card pillar">
                <div class="icon-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 20c0-8 5-14 14-15-1 9-7 14-14 15z"/><path d="M5 20c3-4 6-7 10-10"/></svg></div>
                <h3>Sustainability</h3>
                <p>Targeting rumen fermentation pathways to improve feed efficiency and reduce enteric methane emissions from cattle.</p>
                <span class="more">Learn more →</span>
            </a>
        </div>
    </div>
</section>

<section class="section section-alt">
    <div class="container" style="padding-top: 3.5rem; padding-bottom: 3.5rem;">
        <div class="section-head center">
            <span class="eyebrow">Our approach</span>
            <h2>From the barn to the bench to the field</h2>
            <p>A translational pipeline that pairs classical anaerobic microbiology with modern sequencing and computation.</p>
        </div>
        <div class="steps">
            <div class="step">
                <h3>Culture</h3>
                <p>Anaerobic isolation of rumen and gut microbes to build a living biobank of strains and genomes.</p>
            </div>
            <div class="step">
                <h3>Sequence</h3>
                <p>Illumina and Oxford Nanopore sequencing for genome-resolved metagenomics and metatranscriptomics.</p>
            </div>
            <div class="step">
                <h3>Model</h3>
                <p>Bioinformatics, metabolic modelling, and machine learning to link microbial function to host phenotypes.</p>
            </div>
            <div class="step">
                <h3>Translate</h3>
                <p>Probiotics, postbiotics, feed strategies, and surveillance tools that producers and veterinarians can use.</p>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-head" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
            <div>
                <span class="eyebrow">Latest from the lab</span>
                <h2 style="margin: 0;">News &amp; events</h2>
            </div>
            <a href="{{ '/events' | relative_url }}" class="btn btn-outline btn-sm">All news &amp; events</a>
        </div>

        {% assign latest = site.events | sort: "date" | reverse | slice: 0, 3 %}
        <div class="news-slider" id="news-slider">
            <div class="news-track" id="news-track" aria-live="polite">
                <div class="news-strip" id="news-strip">
                {% for event in latest %}
                <a href="{{ '/events' | relative_url }}#{{ event.date | date: '%Y-%m-%d' }}" class="news-slide">
                    <img src="{{ event.image | relative_url }}" alt="{{ event.title }}" loading="lazy">
                    <div class="body">
                        <span class="date">{% if event.date_display %}{{ event.date_display }}{% else %}{{ event.date | date: "%B %Y" }}{% endif %}{% if event.location %} · {{ event.location }}{% endif %}</span>
                        <h3>{{ event.title }}</h3>
                        <p>{{ event.summary }}</p>
                        <span class="more">Read more →</span>
                    </div>
                </a>
                {% endfor %}
                </div>
            </div>
            <div class="news-controls">
                <button class="news-arrow" type="button" data-dir="-1" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button>
                <div class="news-dots" id="news-dots" role="tablist" aria-label="Choose a news item"></div>
                <button class="news-arrow" type="button" data-dir="1" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>
            </div>
        </div>
    </div>
</section>

<script>
(function () {
    const slider = document.getElementById("news-slider");
    const track = document.getElementById("news-track");
    const strip = document.getElementById("news-strip");
    const dotsEl = document.getElementById("news-dots");
    if (!slider || !strip) return;
    const slides = Array.from(strip.children);
    if (slides.length < 2) { slider.querySelector(".news-controls").style.display = "none"; return; }

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let index = 0, timer = null;

    slides.forEach((_, i) => {
        const b = document.createElement("button");
        b.type = "button"; b.setAttribute("role", "tab");
        b.setAttribute("aria-label", "Show item " + (i + 1));
        b.addEventListener("click", () => { go(i); restart(); });
        dotsEl.appendChild(b);
    });
    const dots = Array.from(dotsEl.children);

    function go(i) {
        index = (i + slides.length) % slides.length;
        strip.style.transform = "translateX(" + (-slides[index].offsetLeft) + "px)";
        dots.forEach((d, k) => d.setAttribute("aria-selected", k === index ? "true" : "false"));
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function restart() { stop(); if (!reduceMotion) timer = setInterval(() => go(index + 1), 7000); }

    slider.querySelectorAll(".news-arrow").forEach(btn =>
        btn.addEventListener("click", () => { go(index + Number(btn.dataset.dir)); restart(); }));

    // Swipe support (touch and mouse drag).
    let startX = null, moved = false;
    track.addEventListener("pointerdown", e => { startX = e.clientX; moved = false; stop(); });
    track.addEventListener("pointermove", e => { if (startX !== null && Math.abs(e.clientX - startX) > 8) moved = true; });
    track.addEventListener("pointerup", e => {
        if (startX === null) return;
        const dx = e.clientX - startX;
        if (Math.abs(dx) > 40) go(index + (dx < 0 ? 1 : -1));
        startX = null; restart();
    });
    track.addEventListener("pointercancel", () => { startX = null; restart(); });
    // A drag should not count as a click on the slide link.
    slides.forEach(a => a.addEventListener("click", e => { if (moved) e.preventDefault(); }));

    slider.addEventListener("mouseenter", stop);
    slider.addEventListener("mouseleave", restart);
    slider.addEventListener("focusin", stop);
    slider.addEventListener("focusout", restart);
    window.addEventListener("resize", () => go(index));

    go(0); restart();
})();
</script>

<section class="section">
    <div class="container">
        <div class="cta-band">
            <div>
                <span class="eyebrow">Work with us</span>
                <h2>Interested in joining the lab?</h2>
                <p>We welcome motivated graduate students, undergraduates, and postdoctoral researchers with backgrounds in microbiology, animal science, molecular biology, or bioinformatics.</p>
            </div>
            <div class="btn-group">
                <a href="{{ '/prospective' | relative_url }}" class="btn btn-light">Opportunities</a>
                <a href="mailto:hooman.derakhshani@umanitoba.ca" class="btn btn-accent">Contact Dr. Derakhshani</a>
            </div>
        </div>
    </div>
</section>
