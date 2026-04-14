const locationCoords = {
    "Rohini": { lat: 28.7494, lon: 77.0565 },
    "Dwarka": { lat: 28.5921, lon: 77.0460 },
    "Shahdara": { lat: 28.6721, lon: 77.2872 },
    "Laxmi Nagar": { lat: 28.6328, lon: 77.2773 },
    "Saket": { lat: 28.5245, lon: 77.2066 },
    "Karol Bagh": { lat: 28.6519, lon: 77.1909 },
    "Najafgarh": { lat: 28.6090, lon: 76.9855 },
    "Janakpuri": { lat: 28.6219, lon: 77.0878 }
};

async function updateTemperature() {
    const location = document.getElementById("location").value;
    const coords = locationCoords[location];

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${coords.lat}&longitude=${coords.lon}&current=temperature_2m`;

    const response = await fetch(url);
    const data = await response.json();

    document.getElementById("temp").value = Math.round(data.current.temperature_2m);
}

document.getElementById("location").addEventListener("change", updateTemperature);
window.onload = updateTemperature;

document.getElementById("predictionForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const dayInput = document.getElementById("day_of_week").value.trim();
    const formattedDay = dayInput.charAt(0).toUpperCase() + dayInput.slice(1).toLowerCase();

    const data = {
        location: document.getElementById("location").value,
        temp: parseInt(document.getElementById("temp").value),
        holiday: parseInt(document.getElementById("holiday").value),
        last_week_attendance: parseInt(document.getElementById("last_week_attendance").value),
        day_of_week: formattedDay,
        doses_per_vial: parseInt(document.getElementById("doses_per_vial").value)
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML = `
        <div class="result-grid">
            <div class="result-card blue">
                <strong>👥 Expected Attendance</strong><br>${result.expected_attendance}
            </div>
            <div class="result-card green">
                <strong>💉 Recommended Doses</strong><br>${result.recommended_doses}
            </div>
            <div class="result-card cyan">
                <strong>🧪 Vials to Open</strong><br>${result.vials_to_open}
            </div>
            <div class="result-card yellow">
                <strong>⚠️ Wastage Risk</strong><br>${result.wastage_risk}
            </div>
        </div>
    `;

    // Live district heatmap intelligence
    document.querySelectorAll(".zone").forEach(zone => {
        zone.style.background = "#6c757d";
        zone.style.color = "white";
    });

    const selectedZone = document.getElementById(data.location);

    if (result.wastage_risk === "High") {
        selectedZone.style.background = "#dc3545";
    } else if (result.wastage_risk === "Medium") {
        selectedZone.style.background = "#ffc107";
        selectedZone.style.color = "#222";
    } else {
        selectedZone.style.background = "#28a745";
    }
});