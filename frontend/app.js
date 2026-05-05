async function search() {
    const q = document.getElementById("searchInput").value;

    const res = await fetch(`/api/search?q=${q}`);
    const data = await res.json();

    const results = document.getElementById("results");
    results.innerHTML = "";

    data.results.forEach(r => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <h3>${r.title}</h3>
            <p>$${r.price}</p>
            <p>${r.location}</p>
        `;
        results.appendChild(div);
    });
}
