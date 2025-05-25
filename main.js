
function showTab(id) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.style.display = 'none');
    document.getElementById(id).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('market').innerHTML = `<h2>Market Recap</h2><p>${data.marketRecap.longSummary}</p><p><strong>TL;DR:</strong> ${data.marketRecap.tldr}</p>`;
    document.getElementById('headlines').innerHTML = '<h2>Headlines</h2>' + data.headlines.map(h => `<h3>${h.title}</h3><p>${h.summary}</p><p><em>${h.gptTake}</em></p>`).join('<hr>');
    document.getElementById('deals').innerHTML = '<h2>M&A / IPOs</h2>' + data.deals.map(d => `<h3>${d.title}</h3><p>${d.summary}</p><p><em>${d.gptTake}</em></p>`).join('<hr>');
    document.getElementById('events').innerHTML = `<h2>Economic Events</h2><ul>${data.events.map(e => `<li>${e}</li>`).join('')}</ul>`;
    document.getElementById('gpt').innerHTML = `<h2>GPT Daily Take</h2><p>${data.gptAnalysis}</p>`;
});
