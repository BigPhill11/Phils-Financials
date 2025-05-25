
document.addEventListener('DOMContentLoaded', () => {
    const content = document.getElementById('content');

    const addSection = (title, body, take) => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `<h2>${title}</h2><p>${body}</p><p><em>💬 GPT's Take: ${take}</em></p>`;
        content.appendChild(card);
    };

    addSection('Market Recap', data.marketRecap.summary, data.marketRecap.gptTake);

    data.headlines.forEach(headline => {
        addSection(`Headline: ${headline.title}`, headline.summary, headline.gptTake);
    });

    addSection('Economic Events', data.events.today.join('<br>'), data.events.gptTake);
    addSection('M&A / Deals', data.deals.summary, data.deals.gptTake);

    const quoteCard = document.createElement('div');
    quoteCard.className = 'card';
    quoteCard.innerHTML = `<h2>Quote of the Day</h2><p>${data.quote.text}</p>`;
    content.appendChild(quoteCard);
});
