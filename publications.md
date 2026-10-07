---
layout: default
title: Publications
description: Peer-reviewed publications from the Translational Livestock Microbiome Research Lab.
permalink: /publications/
---

<div class="container">
    <div class="page-header">
        <span class="eyebrow">Publications</span>
        <h1>Publications</h1>
        <p class="lead">Peer-reviewed research from the lab and our collaborators, updated automatically from PubMed.</p>
    </div>

    <div class="pub-toolbar">
        <span class="muted small" id="pub-count"></span>
        <a href="https://pubmed.ncbi.nlm.nih.gov/?term=Derakhshani+H%5BAuthor%5D+NOT+(Depression+OR+Psychiatry+OR+rTMS)" target="_blank" rel="noopener" class="btn btn-outline btn-sm">View on PubMed</a>
    </div>

    <div id="loading-message" class="pub-loading"><span class="spinner" aria-hidden="true"></span> Loading publications…</div>

    <div id="pubmed-container"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {

    // =================================================================
    // PART 1: MANUAL PAPERS (add non-PubMed items here)
    // =================================================================
    const manualPapers = [
        {
            title: "Effects of dietary fiber on fecal microbiota of grower–finisher pig offspring from parents with divergent estimated breeding value for feed conversion ratio.",
            authors: ["Azevedo P", "Jin S", "Wu Y", "Derakhshani H", "Xu H", "Lei H", "Verschuren L", "Yang C"],
            year: "2025",
            journal: "Canadian Journal of Animal Science",
            link: "https://cdnsciencepub.com/doi/10.1139/cjas-2024-0100"
        },
        {
            title: "Selection for feed efficiency improves production traits and digestibility and its relationship to the fecal microbiota in both Large White dam and sire lines.",
            authors: ["Beens L", "Rajendiran E", "Derakhshani H", "Mejicanos G", "Yang C", "Nyachoti M", "Lei H", "Verschuren L", "Bergsma R", "Rodas-Gonzalez A"],
            year: "2024",
            journal: "Canadian Journal of Animal Science",
            link: "https://cdnsciencepub.com/doi/10.1139/cjas-2024-0009"
        },
        {
            title: "Metagenomic comparison of effects of mesophilic and thermophilic manure anaerobic digestion on antimicrobial resistance genes and mobile genetic elements.",
            authors: ["Flores-Orozco D", "Levin D", "Kumar A", "Sparling R", "Derakhshani H", "Cicek N"],
            year: "2024",
            journal: "Environmental Advances",
            link: "https://www.sciencedirect.com/science/article/pii/S2666765723001308"
        }
        // Add more here using the same format { ... },
    ];

    // =================================================================
    // PART 2: CONFIGURATION (the "exclusion" search)
    // Lists what we are NOT, to filter out an unrelated author with the same name.
    // =================================================================
    const searchTerm = 'Derakhshani H[Author] NOT (Depression OR Psychiatry OR "Transcranial Magnetic Stimulation" OR rTMS OR "Major Depressive Disorder")';
    const maxResults = 200;
    const highlightAuthors = ["Derakhshani H"];
    // =================================================================

    const container = document.getElementById("pubmed-container");
    const loading = document.getElementById("loading-message");
    const countEl = document.getElementById("pub-count");

    const escapeHtml = (s) => String(s)
        .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

    const linkIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/></svg>';

    function pubmedLink(p) {
        // Prefer a real DOI from articleids; fall back to the PubMed record.
        const doi = (p.articleids || []).find(a => a.idtype === "doi");
        if (doi && doi.value) return "https://doi.org/" + doi.value.replace(/^doi:\s*/i, "");
        return "https://pubmed.ncbi.nlm.nih.gov/" + p.uid + "/";
    }

    function render(allPapers) {
        // Sort by year (descending); keep PubMed's date order within a year.
        allPapers.sort((a, b) => Number(b.year) - Number(a.year));

        const byYear = {};
        allPapers.forEach(p => { (byYear[p.year] = byYear[p.year] || []).push(p); });

        const years = Object.keys(byYear).filter(y => y !== "Unknown").sort().reverse();
        let html = "";
        let total = 0;

        years.forEach(year => {
            const papers = byYear[year];
            total += papers.length;
            html += `<h2 class="pub-year">${year} <small>${papers.length} ${papers.length === 1 ? "paper" : "papers"}</small></h2>`;
            html += `<ul class="pub-list">`;

            papers.forEach(paper => {
                let authors = paper.authors.slice();
                let etAl = "";
                if (authors.length > 15) { authors = authors.slice(0, 15); etAl = ", et al."; }
                let authorsStr = authors.map(escapeHtml).join(", ") + etAl;
                highlightAuthors.forEach(name => {
                    authorsStr = authorsStr.split(escapeHtml(name)).join(`<strong>${escapeHtml(name)}</strong>`);
                });

                const title = escapeHtml(paper.title);
                const titleHtml = paper.link
                    ? `<a href="${escapeHtml(paper.link)}" target="_blank" rel="noopener">${title}</a>`
                    : title;
                const linkHtml = paper.link
                    ? `<a class="pub-link" href="${escapeHtml(paper.link)}" target="_blank" rel="noopener">View article ${linkIcon}</a>`
                    : "";

                html += `
                    <li class="pub">
                        <div class="pub-title">${titleHtml}</div>
                        <div class="pub-authors">${authorsStr}</div>
                        <div class="pub-meta"><em>${escapeHtml(paper.journal || "")}</em> ${linkHtml}</div>
                    </li>`;
            });
            html += `</ul>`;
        });

        container.innerHTML = html;
        if (countEl) countEl.textContent = `${total} publications`;
        loading.style.display = "none";
    }

    const searchUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${encodeURIComponent(searchTerm)}&retmode=json&retmax=${maxResults}&sort=date`;

    fetch(searchUrl)
        .then(r => r.json())
        .then(data => {
            const ids = data.esearchresult.idlist;
            if (!ids.length) return null;
            const summaryUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=${ids.join(",")}&retmode=json`;
            return fetch(summaryUrl).then(r => r.json());
        })
        .then(data => {
            let allPapers = manualPapers.slice();
            if (data && data.result) {
                const manualTitles = new Set(manualPapers.map(p => p.title.toLowerCase().slice(0, 60)));
                data.result.uids.forEach(id => {
                    const p = data.result[id];
                    if (manualTitles.has((p.title || "").toLowerCase().slice(0, 60))) return; // avoid duplicates
                    allPapers.push({
                        title: p.title,
                        authors: p.authors ? p.authors.map(a => a.name) : ["Unknown"],
                        year: p.pubdate ? p.pubdate.substring(0, 4) : "Unknown",
                        journal: p.fulljournalname || p.source,
                        link: pubmedLink(p)
                    });
                });
            }
            render(allPapers);
        })
        .catch(err => {
            console.error("Publications error:", err);
            // Still show the manual list if PubMed is unreachable.
            render(manualPapers.slice());
            const note = document.createElement("p");
            note.className = "muted small";
            note.textContent = "Live PubMed results are temporarily unavailable. Showing a partial list.";
            container.prepend(note);
        });
});
</script>
