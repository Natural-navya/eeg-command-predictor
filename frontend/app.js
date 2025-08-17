function goToScreen(screenId) {
  const screens = document.querySelectorAll('.screen');
  screens.forEach(s => {
    s.classList.remove('active');
  });

  setTimeout(() => {
    const targetScreen = document.getElementById(screenId);
    targetScreen.classList.add('active');
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
    console.log("Backend response:", data); 
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
  goToScreen('output'); 
}

function playSpeech() {
  let text = document.getElementById('outputText').innerText;


  speechSynthesis.cancel();

  if (text.trim() !== "") {
    let speech = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(speech);
  }

}
