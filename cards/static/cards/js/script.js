function filterCards() {
    let input = document.getElementById('search').value.toLowerCase();
    let cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        let name = card.querySelector('h3').innerText.toLowerCase();
        let profession = card.querySelector('p').innerText.toLowerCase();

        if (name.includes(input) || profession.includes(input)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}
