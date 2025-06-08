// Fetch data from FastAPI backend
async function fetchAsteroids() {
  const results = document.getElementById("results");
  results.innerHTML = "Loading asteroid data...";

  try {
    const res = await fetch("/asteroids");
    const data = await res.json();

    let output = "";

    const dates = Object.keys(data.near_earth_objects);

    dates.forEach((date) => {
      output += `<h2>${date}</h2>`;
      data.near_earth_objects[date].forEach((asteroid) => {
        output += `
          <p>
            <strong>${asteroid.name}</strong><br>
            Close approach date: ${
              asteroid.close_approach_data[0].close_approach_date
            }<br>
            Diameter: ${asteroid.estimated_diameter.meters.estimated_diameter_max.toFixed(
              2
            )} meters<br>
            Speed: ${parseFloat(
              asteroid.close_approach_data[0].relative_velocity
                .kilometers_per_hour
            ).toFixed(2)} km/h
          </p>
        `;
      });
    });

    results.innerHTML = output;
  } catch (error) {
    results.innerHTML = "❌ Error fetching asteroid data.";
    console.error(error);
  }
}

// Back button
document.getElementById("backBtn").addEventListener("click", () => {
  window.location.href = "/";
});

fetchAsteroids();
