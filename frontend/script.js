function loadIdeas() {
    fetch('http://127.0.0.1:5000/ideas')
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('list');
        list.innerHTML = "";

        data.forEach(idea => {
            const div = document.createElement('div');
            div.className = "card";
            div.innerHTML = `
                <h3>${idea.title}</h3>
                <p>${idea.description}</p>
                <strong>Score: ${idea.score}</strong>
            `;
            list.appendChild(div);
        });
    });
}