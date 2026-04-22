// Submit Idea
function submitIdea() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('desc').value;

    if (!title || !description) {
        alert("Fill all fields!");
        return;
    }

    fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description })
    })
    .then(res => res.json())
    .then(data => {
        alert("Score: " + data.score);
    });
}

// Load Ideas
function loadIdeas() {
    fetch('http://127.0.0.1:5000/ideas')
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('list');
        list.innerHTML = "";

        data.forEach(idea => {
            const li = document.createElement('li');
            li.innerHTML = `
                <b>${idea.title}</b><br>
                ${idea.description}<br>
                Score: ${idea.score}
                <hr>
            `;
            list.appendChild(li);
        });
    });
}
