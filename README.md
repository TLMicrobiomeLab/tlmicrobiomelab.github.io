# Translational Livestock Microbiome Research (TLMR) Lab

This is the source code for the **Translational Livestock Microbiome Research Lab** website.

**Live Website:** [Translational Livestock Microbiome Research Lab](https://tlmicrobiomelab.github.io/)

## About the Lab
The TLMR Lab is dedicated to solving complex livestock agricultural challenges through microbiome science. Our research integrates multiomics data (metagenomics, metatranscriptomics, metabolomics) to decode host-microbe interactions in livestock species.

**Key Research Areas:**
* **Host-Microbe Interactions:** Ruminants and swine gut health.
* **Microbiome Therapeutics:** Probiotics, prebiotics, and early-life interventions.
* **Antimicrobial Resistance (AMR):** Mitigating resistance in livestock environments.
* **Sustainability:** Improving feed efficiency and reducing enteric methane emissions.

## Adding News & Events
Each news item lives in its own file in `_events/`, named `YYYY-MM-DD-short-slug.md`. The News page lists every file, newest first, and the home page slider automatically shows the three most recent.

```yaml
---
title: "TLMR Lab at EAAP 2026, Hamburg"
date: 2026-09-09
date_display: June 2025        # optional, overrides the formatted date (e.g. when only the month is known)
tag: Conference                # Conference, Milestone, Social, Community, ...
image: /images/eaap2026/eaap-1.jpg   # used on the home page slider
location: Hamburg, Germany     # optional, shown under the date on the home page
summary: "One or two sentences for the home page slider."
hero: true                     # optional, shows `image` beside the text instead of a photo grid
---

<div class="prose">
    <p>Story text...</p>
</div>
<div class="photo-grid cols-3">
    <div class="photo-tile">
        <img src="{{ '/images/folder/photo.jpg' | relative_url }}" alt="Describe the photo" loading="lazy">
        <p class="caption">Caption.</p>
    </div>
</div>
```

Put photos in a folder under `images/` (JPEG, about 1200 px on the long side). Use `cols-3` or `cols-4` on the grid to fix the number of columns, or omit it for an automatic layout.

## Local Development
To run this website locally on your computer:

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    bundle install
    ```
3.  Run the Jekyll server:
    ```bash
    bundle exec jekyll serve
    ```
4.  Open your browser to `http://localhost:4000`.

## Credits
* **Built with:** [Jekyll](https://jekyllrb.com/)
* **Hosted on:** GitHub Pages
* This site was created and maintained by Zisanur Rahman, PhD. For any suggestion or queries, email at a.rahman@umanitoba.ca
