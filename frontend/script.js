const API_URL = "https://fixboard-lrqx.onrender.com";

const issueForm = document.getElementById("issueForm");
const issuesList = document.getElementById("issuesList");

async function loadIssues() {
  try {
    const response = await fetch(`${API_URL}/issues`);
    const issues = await response.json();

    issuesList.innerHTML = "";

    if (issues.length === 0) {
      issuesList.innerHTML = "<p>No issues submitted yet.</p>";
      return;
    }

    issues.forEach((issue) => {
      const issueCard = document.createElement("div");
      issueCard.className = "issue-card";

      issueCard.innerHTML = `
                <h3>${issue.title}</h3>
                <p>${issue.description}</p>
                <p><strong>Category:</strong> ${issue.category}</p>
                <p class="status">Status: ${issue.status}</p>
                <p><small>Created at: ${issue.created_at}</small></p>
            `;

      issuesList.appendChild(issueCard);
    });
  } catch (error) {
    issuesList.innerHTML = "<p>Failed to load issues.</p>";
    console.error(error);
  }
}

issueForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const category = document.getElementById("category").value;

  const issueData = {
    title: title,
    description: description,
    category: category,
  };

  try {
    const response = await fetch(`${API_URL}/issues`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(issueData),
    });

    const result = await response.json();

    if (response.ok) {
      alert("Issue submitted successfully!");
      issueForm.reset();
      loadIssues();
    } else {
      alert(result.error || "Something went wrong.");
    }
  } catch (error) {
    alert("Failed to submit issue.");
    console.error(error);
  }
});

loadIssues();
