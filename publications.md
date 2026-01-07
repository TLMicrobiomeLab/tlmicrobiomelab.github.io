---
layout: default
title: Publications
permalink: /publications/
---

<div class="content-wrapper">

<h1>Publications</h1>
<p style="margin-bottom: 2rem;">
    This list is automatically retrieved from PubMed.
    <br>
    <a href="https://pubmed.ncbi.nlm.nih.gov/?term=Derakhshani+H%5BAuthor%5D" target="_blank" style="font-size: 0.9rem;">View on PubMed &rarr;</a>
</p>

<hr style="border: 0; border-top: 1px solid #ddd; margin-bottom: 2rem;">

<div id="loading-message" style="color: #666; font-style: italic;">
    Loading publications from PubMed...
</div>

<div id="pubmed-container"></div>

</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        // =================================================================
        // CONFIGURATION: SMARTER SEARCH FILTER
        // =================================================================
        // This query finds "Derakhshani H" BUT filters for specific keywords
        // to exclude the psychiatrist (Horeyeh) and ensure papers are found.
        const searchTerm = 'Derakhshani H[Author] AND (Hooman[Author])'; 
        
        const maxResults = 200; // Increased to ensure we don't "miss" papers if the list is long
        // =================================================================

        const container = document.getElementById('pubmed-container');
        const loading = document.getElementById('loading-message');

        // 1. Search for IDs
        const searchUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${encodeURIComponent(searchTerm)}&retmode=json&retmax=${maxResults}&sort=date`;

        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {
                const ids = data.esearchresult.idlist;
                
                if (ids.length === 0) {
                    loading.textContent = "No publications found matching these criteria.";
                    return;
                }

                // 2. Fetch Details for those IDs
                const summaryUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=${ids.join(',')}&retmode=json`;
                
                return fetch(summaryUrl);
            })
            .then(response => response ? response.json() : null)
            .then(data => {
                if (!data) return;

                const papers = data.result;
                const idList = data.result.uids; 
                
                // --- Grouping Logic ---
                const papersByYear = {};

                idList.forEach(id => {
                    const paper = papers[id];
                    if (!paper.title) return; 

                    // Extract Year safely
                    let year = "Unknown";
                    if (paper.pubdate) {
                        year = paper.pubdate.substring(0, 4);
                    }

                    if (!papersByYear[year]) {
                        papersByYear[year] = [];
                    }
                    papersByYear[year].push(paper);
                });

                // Sort years descending (2025, 2024, ...)
                const sortedYears = Object.keys(papersByYear).sort().reverse();

                // Build HTML
                let htmlContent = '';

                sortedYears.forEach(year => {
                    htmlContent += `<h2 style="color: #00A9B7; border-bottom: 2px solid #eee; padding-bottom: 0.5rem; margin-top: 2.5rem;">${year}</h2>`;
                    htmlContent += `<ul style="list-style: none; padding: 0;">`;

                    papersByYear[year].forEach(paper => {
                        // Format Authors
                        let authors = paper.authors.map(a => a.name).join(", ");
                        
                        // Bold name in the list
                        authors = authors.replace("Derakhshani H", "<strong>Derakhshani H</strong>");

                        if (paper.authors.length > 15) {
                            authors = paper.authors.slice(0, 15).map(a => a.name).join(", ") + ", et al.";
                        }

                        htmlContent += `
                            <li style="margin-bottom: 1.5rem;">
                                <div style="font-weight: 500; margin-bottom: 0.25rem; font-size: 1.05rem; line-height: 1.4;">
                                    ${authors}. (${year}). 
                                    <span style="font-style: italic;">${paper.title}</span>
                                </div>
                                <div style="font-size: 0.95rem; color: #555;">
                                    <em>${paper.fulljournalname}</em>. 
                                    <a href="https://doi.org/${paper.elocationid}" target="_blank" style="color: #002F5F; margin-left: 8px; font-size: 0.85rem; font-weight: bold;">[View Article]</a>
                                </div>
                            </li>
                        `;
                    });

                    htmlContent += `</ul>`;
                });

                container.innerHTML = htmlContent;
                loading.style.display = 'none';
            })
            .catch(error => {
                console.error('Error fetching PubMed data:', error);
                loading.textContent = "Error loading publications. Please try refreshing.";
            });
    });
</script>
