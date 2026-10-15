const API_URL = "http://127.0.0.1:5000";

async function loadPatterns(){
    const response = await fetch(`${API_URL}/stats`);
    const stats = await response.json();

    const patternSelect = document.getElementById("pattern");
    patternSelect.innerHTML = "";

    stats.forEach(item =>{
        const option = document.createElement("option");
        option.value = item.pattern;
        option.textContent = item.pattern;
        patternSelect.appendChild(option);
    });
}

async function loadStats(){
    const response = await fetch(`${API_URL}/stats`);
    const stats = await response.json();

    const statsList = document.getElementById("stats_list");
    statsList.innerHTML = "";

    stats.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.pattern}: ${item.count} solved`;
        statsList.appendChild(li);
    });
}

async function loadProblems(){
    const response = await fetch(`${API_URL}/problems`);
    const problems = await response.json();

    const problemsList = document.getElementById("problems_list");
    problemsList.innerHTML = "";

    // list of saved problems along with delete buttons
    problems.forEach((item, i) => {
        const li = document.createElement("li");
        const button = document.createElement("button")
        button.type = "button";
        button.textContent = "Delete";
        button.id = `${i + 1}`;
        button.addEventListener("click", async function() {
            const response = await fetch(`${API_URL}/problems/${item.id}` , {
                method: "DELETE"
            });
            if(!response.ok) {
                console.error("Delete failed");
                return;
            }
            // event.preventDefault();

            // const Id = item.id;
            // await fetch(`${API_URL}/delete`, {
            // method: "POST",
            // headers: {"Content-Type": "application/json"},
            // body: JSON.stringify({Id})
            // });

            await loadProblems();
            await loadStats();
        });
        li.textContent = `${item.name}: ${item.pattern}`;
        li.appendChild(button)
        problemsList.appendChild(li);
    });
}

document.getElementById("add_form").addEventListener("submit", async function(event){
    event.preventDefault();

    const name = document.getElementById("name").value;
    const pattern = document.getElementById("pattern").value;
    const difficulty = document.getElementById("difficulty").value;

    await fetch(`${API_URL}/problems`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, pattern, difficulty})
    });

    document.getElementById("name").value = "";

    await loadStats();
    await loadProblems();
});

loadPatterns();
loadStats();
loadProblems();

const button = document.getElementById("reveal_problems");
const content = document.getElementById("saved_problems");

button.addEventListener("click", async function (){
    if (getComputedStyle(content).display === "none"){
        content.style.display = "flex";
    } else{
        content.style.display = "none";
    }
});