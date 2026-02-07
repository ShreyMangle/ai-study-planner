let topics = [];
let timerInterval = null;

function addTopic() {
  const topic = document.getElementById("topic").value.trim();
  const difficulty = document.getElementById("difficulty").value;
  const confidence = document.getElementById("confidence").value;
  const deadline = document.getElementById("deadline").value;

  if (!topic || !difficulty || !confidence || !deadline) {
    alert("Please fill all fields");
    return;
  }

  const newTopic = {
    name: topic,
    difficulty: Number(difficulty),
    confidence: Number(confidence),
    deadline_days: Number(deadline),
    weight: 1.0
  };

  topics.push(newTopic);

  console.log(" Topic added:", newTopic);
  console.log(" Current topics:", topics);

  alert("Topic added successfully!");

  document.getElementById("topic").value = "";
  document.getElementById("difficulty").value = "";
  document.getElementById("confidence").value = "";
  document.getElementById("deadline").value = "";
}


async function generatePlan() {
  console.log(" Sending topics:", topics);

  if (topics.length === 0) {
    alert("No topics added!");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/api/v1/plan", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        daily_hours: 4,
        learning_pace: "medium",
        topics: topics
      })
    });

    if (!response.ok) {
      throw new Error("Server error: " + response.status);
    }

    const data = await response.json();

    console.log(" API response:", data);

    document.getElementById("output").textContent =
      JSON.stringify(data, null, 2);

  } catch (err) {
    console.error("Fetch failed:", err);
    alert("Backend not reachable. Check console.");
  }
}

function startPomodoro() {
  let time = 25 * 60;
  const display = document.getElemtById("timer");

  if (timerInterval) clearInterval(timerInterval);

  timerInterval = setInterval(() => {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    display.textContent =
      `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;

    if (time-- <= 0) {
      clearInterval(timerInterval);
      alert("Session complete! How did that feel?");
    }
  }, 1000);
}
