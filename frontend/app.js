function goToScreen(screenId) {
  const screens = document.querySelectorAll('.screen');
  screens.forEach(s => {
    s.classList.remove('active');
  });

  // small timeout ensures CSS transition triggers
  setTimeout(() => {
    const targetScreen = document.getElementById(screenId);
    targetScreen.classList.add('active');

    // If it's the output screen, auto-play the speech
    if (screenId === 'output') {
      playSpeech();
    }
  }, 20);
}

function sendToBackend(command) {
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ command: command })
  })
  .then(res => res.json())
  .then(data => {
    console.log("Backend response:", data); // debug in console
    if (data.prediction) {
      document.getElementById("outputText").innerText = data.prediction;
    } else {
      document.getElementById("outputText").innerText = "Error: " + data.error;
    }
    goToScreen("output");
  })
  .catch(err => {
    console.error("Fetch error:", err);
    document.getElementById("outputText").innerText = "⚠ Server not reachable";
    goToScreen("output");
  });
}


function showOutput(text) {
  document.getElementById('outputText').innerText = text;
  goToScreen('output');  // playSpeech() will be triggered here automatically
}

function playSpeech() {
  let text = document.getElementById('outputText').innerText;

  // Stop any ongoing speech before starting new
  speechSynthesis.cancel();

  if (text.trim() !== "") {
    let speech = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(speech);
  }
}