---
layout: default
title: Publications
permalink: /publications/
---

<div class="content-wrapper">

<h1>Publications</h1>
<p style="margin-bottom: 2rem;">
    Browse our research output below.
    <br>
    <a href="https://pubmed.ncbi.nlm.nih.gov/?term=Derakhshani+H%5BAuthor%5D+NOT+(Depression+OR+Psychiatry+OR+rTMS)" target="_blank" style="font-size: 0.9rem;">View on PubMed &rarr;</a>
</p>

<hr style="border: 0; border-top: 1px solid #ddd; margin-bottom: 2rem;">

<div id="loading-message" style="color: #666; font-style: italic;">
    Loading publications...
</div>

<div id="pubmed-container"></div>

</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        
        // =================================================================
        // PART 1: MANUAL PAPERS (Add your non-PubMed items here)
        // =================================================================
        const manualPapers = [
            {
                title: "Effects of dietary fiber on fecal microbiota of grower–finisher pig offspring from parents with divergent estimated breeding value for feed conversion ratio",
                authors: ["P Azevedo", "S Jin", "Y Wu", "H Derakhshani", "H Xu", "H Lei", "L Verschuren", "C Yang"],
                year: "2025",
                journal: "Canadian Journal of Animal Science",
                link: "https://cdnsciencepub.com/doi/10.1139/cjas-2024-0100", // Optional
                type: "Research Article" // Optional label
            },
            {
                title: "Selection for feed efficiency improves production traits and digestibility and its relationship to the fecal microbiota in both Large White dam and sire lines",
                authors: ["L Beens", "E Rajendiran", "H Derakhshani", "G Mejicanos", "C Yang", "M Nyachoti", "H Lei", "L Verschuren", "R Bergsma", "A Rodas-Gonzalez"],
                year: "2024",
                journal: "Canadian Journal of Animal Science",
                link: "https://cdnsciencepub.com/doi/10.1139/cjas-2024-0009", // Optional
                type: "Research Article" // Optional label
            }
            // Add more here using the same format { ... },
        ];

        // =================================================================
        // PART 2: CONFIGURATION (The "Exclusion" Search)
        // =================================================================
        // Instead of listing what you ARE (which misses things), we list what you are NOT.
        // This filters out the psychiatrist "Horeyeh Derakhshani" explicitly.
        const searchTerm = 'Derakhshani H[Author] NOT (Depression OR Psychiatry OR "Transcranial Magnetic Stimulation" OR rTMS OR "Major Depressive Disorder")'; 
        const maxResults = 200; 
        // =================================================================

        const container = document.getElementById('pubmed-container');
        const loading = document.getElementById('loading-message');

        // 1. Search PubMed
        const searchUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=${encodeURIComponent(searchTerm)}&retmode=json&retmax=${maxResults}&sort=date`;

        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {
                const ids = data.esearchresult.idlist;
                if (ids.length === 0) return []; // Return empty if none found
                
                // Fetch details
                const summaryUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=${ids.join(',')}&retmode=json`;
                return fetch(summaryUrl).then(res => res.json());
            })
            .then(data => {
                let allPapers = [...manualPapers]; // Start with manual papers

                // If PubMed returned data, process it
                if (data && data.result) {
                    const pubmedPapers = data.result.uids.map(id => {
                        const p = data.result[id];
                        // Format PubMed authors to match manual format
                        const authorList = p.authors ? p.authors.map(a => a.name) : ["Unknown"];
                        
                        return {
                            title: p.title,
                            authors: authorList,
                            year: p.pubdate ? p.pubdate.substring(0, 4) : "Unknown",
                            journal: p.fulljournalname,
                            link: `https://doi.org/${p.elocationid}`,
                            source: "PubMed"
                        };
                    });
                    
                    // Merge PubMed papers into the list
                    allPapers = allPapers.concat(pubmedPapers);
                }

                // --- SORTING & GROUPING ---
                
                // 1. Sort everything by Year (Descending)
                allPapers.sort((a, b) => b.year - a.year);

                // 2. Group by Year
                const papersByYear = {};
                allPapers.forEach(paper => {
                    if (!papersByYear[paper.year]) papersByYear[paper.year] = [];
                    papersByYear[paper.year].push(paper);
                });

                // 3. Build HTML
                let htmlContent = '';
                const sortedYears = Object.keys(papersByYear).sort().reverse();

                sortedYears.forEach(year => {
                    if(year === "Unknown") return; // Skip bad data

                    htmlContent += `<h2 style="color: #00A9B7; border-bottom: 2px solid #eee; padding-bottom: 0.5rem; margin-top: 2.5rem;">${year}</h2>`;
                    htmlContent += `<ul style="list-style: none; padding: 0;">`;

                    papersByYear[year].forEach(paper => {
                        // Format Authors: Bold "Derakhshani H"
                        let authorsStr = paper.authors.join(", ");
                        authorsStr = authorsStr.replace("Derakhshani H", "<strong>Derakhshani H</strong>");
                        
                        // Truncate long author lists
                        if (paper.authors.length > 15) {
                            authorsStr = paper.authors.slice(0, 15).join(", ") + ", et al.";
                        }

                        // Check if link exists
                        const linkHtml = paper.link 
                            ? `<a href="${paper.link}" target="_blank" style="color: #002F5F; margin-left: 8px; font-size: 0.85rem; font-weight: bold;">[View Article]</a>` 
                            : '';

                        htmlContent += `
                            <li style="margin-bottom: 1.5rem;">
                                <div style="font-weight: 500; margin-bottom: 0.25rem; font-size: 1.05rem; line-height: 1.4;">
                                    ${authorsStr}. (${year}). 
                                    <span style="font-style: italic;">${paper.title}</span>
                                </div>
                                <div style="font-size: 0.95rem; color: #555;">
                                    <em>${paper.journal}</em>. 
                                    ${linkHtml}
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
                console.error('Error:', error);
                loading.textContent = "Error loading publications.";
            });
    });
</script>
