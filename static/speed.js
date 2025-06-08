document.getElementById("calcBtn").addEventListener("click", async () => {
  const distance = document.getElementById("distance").value;
  const time = document.getElementById("time").value;
  const resultBox = document.getElementById("result");

  if (!distance || !time) {
    resultBox.innerHTML = " Please enter both distance and time.";
    return;
  }

  try {
    const response = await fetch(
      `/speed?distance_km=${distance}&time_seconds=${time}`
    );
    const data = await response.json();

    if (data.error) {
      resultBox.innerHTML = ` Error: ${data.error}`;
    } else {
      resultBox.innerHTML = `
        • ${data.speed_km_per_sec} km/s<br>
        • ${data.speed_m_per_sec} m/s
      `;
    }
  } catch (err) {
    resultBox.innerHTML = " Server error. Please try again.";
    console.error(err);
  }
});
