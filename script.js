const API_URL = "http://127.0.0.1:5000";

async function loadPatterns(){
    const response = await fetch('${API_URL}/stats');
    const stats = await response.json();

    const patternSelect = document.getElementById("pattern");
    patternSelect.innerHTML = "";

    stats.forEach(item =>{
        const option = document.createElement("option");
        option.value = item.pattern;
        patternSelect.appendChild(option);
    });
}

async function loadStats(){
    const response = await fetch('${API_URL}/stats');
    const stats = await response.json();

    const statsList = document.getElementById("stats-list");
    statsList.innerHTML = "";

    stats.forEach(item => {
        const li = document.createElement("li");
        li.textContent = '${item.pattern}: ${item.count} solved';
        statsList.appendChild(li);
    });
}

document.getElementById("add-form").addEventListener("submit", async function(event){
    event.preventDefault();

    const name = document.getElementById("name").value;
    const pattern = document.getElementById("pattern").value;
    const difficulty = document.getElementById("difficulty").value;

    await fetch('${API_URL}/problems', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, pattern, difficulty})
    });

    document.getElementById("name").value = "";
    loadStats();
});

loadPatterns();
loadStats();