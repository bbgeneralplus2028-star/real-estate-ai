async function searchProperties() {
    const query = document.getElementById("searchInput").value;

    const res = await fetch(`/api/search?q=${query}`);
    const data = await res.json();

    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    data.results.forEach(item => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <h3>${item.title}</h3>
            <p>Price: $${item.price}</p>
            <p>Location: ${item.location}</p>
        `;
        resultsDiv.appendChild(div);
    });
}
