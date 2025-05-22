// static/script.js
document.addEventListener("DOMContentLoaded", function () {
    // Dynamically populate the homepage with popular items
    const popularItemsContainer = document.getElementById("popular-items");
    if (popularItemsContainer) {
        fetch("/")
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, "text/html");
                const items = doc.querySelectorAll(".popular-item");
                items.forEach(item => popularItemsContainer.appendChild(item.cloneNode(true)));
            });
    }

    // handiling whitespace
    const searchForm = document.querySelector("form");
    const searchInput = document.querySelector("input[name='q']");
    
    if (searchForm && searchInput) {
        searchForm.addEventListener("submit", function (event) {
            const query = searchInput.value.trim();
            if (!query) {
                event.preventDefault();
                searchInput.value = "";
                searchInput.focus();
            }
        });
    }
});
