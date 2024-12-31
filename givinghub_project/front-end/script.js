const BASE_URL = "http://127.0.0.1:5000";

// Fetch and display opportunities
async function fetchOpportunities() {
  const response = await fetch(`${BASE_URL}/opportunities`);
  const data = await response.json();
  const opportunityList = document.getElementById("opportunity-list");

  opportunityList.innerHTML = data.map(opportunity => `
    <div>
      <h3>${opportunity.title}</h3>
      <p>${opportunity.description}</p>
      <p><strong>Category:</strong> ${opportunity.category}</p>
      <p><strong>Location:</strong> ${opportunity.location}</p>
    </div>
  `).join("");
}

// Add a new opportunity
document.getElementById("add-opportunity-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const category = document.getElementById("category").value;
  const location = document.getElementById("location").value;

  await fetch(`${BASE_URL}/opportunities`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description, category, location })
  });

  alert("Opportunity added successfully!");
  fetchOpportunities();
});

fetchOpportunities();