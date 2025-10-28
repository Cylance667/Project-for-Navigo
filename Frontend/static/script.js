window.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("globe");
  const latInput = document.getElementById("latInput");
  const lonInput = document.getElementById("lonInput");
  const addBtn = document.getElementById("addPinBtn");
  const panel = document.getElementById("side-panel");
  const panelContent = document.getElementById("panel-content");
  const closePanel = document.getElementById("closePanel");

  const globe = Globe()(container)
    .globeImageUrl("//unpkg.com/three-globe/example/img/earth-night.jpg");

  // Utility: open side panel and populate content
  function openPanel(data) {
    panel.classList.remove("hidden");
    const { timezone, news, weather } = data;

    panelContent.innerHTML = `
      <h3>Location Info</h3>
      <p><strong>Timezone:</strong> ${timezone}</p>

      <h4>Weather</h4>
      <p>${weather.description}, ${weather.temperature} °${weather.unit}</p>

      <h4>News</h4>
        ${news.map(item => `<a href="${item.url}" style="color: cyan;">${item.title}</a><br>`).join('')}
    `;
  }

  //Functions to show/hide loading overlay
  function showLoading() {
  const overlay = document.getElementById("loading-overlay");
  overlay.classList.add("active");
  }

  function hideLoading() {
    const overlay = document.getElementById("loading-overlay");
    overlay.classList.remove("active");
  }

  closePanel.addEventListener("click", () => {
    panel.classList.add("hidden");
  });

  // Function to set a single pin wherever the user clicks on the globe
  function setSinglePin(lat, lon) {

    globe.pointsData([{ lat, lng: lon, size: 0.3, color: "red" }]);

    showLoading();

    fetch("/process_pin", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lat, lon }),
    })
      .then(res => {
        if (!res.ok) throw new Error(`Flask error: ${res.status}`);
        return res.json();
      })
      .then(json => {
        console.log("Response from backend:", json);
      
      hideLoading();

        if (json.status === "success" && json.result) {
          openPanel(json.result);
        } else {
          openPanel({ error: json.message || "No result field returned." });
        }
      })
      .catch(err => {
        console.error("Error fetching backend:", err);
        openPanel({ error: "Failed to fetch backend response." });
      });
  }

  globe.onGlobeClick(({ lat, lng }) => setSinglePin(lat, lng));

  // Handle manual input
  addBtn.addEventListener("click", () => {
    const lat = parseFloat(latInput.value);
    const lon = parseFloat(lonInput.value);
    setSinglePin(lat, lon);
  });

  // slow globe rotation
  globe.controls().autoRotate = true;
  globe.controls().autoRotateSpeed = 0.5;
});
