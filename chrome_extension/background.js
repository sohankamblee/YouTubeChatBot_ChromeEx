chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "video_id_changed") {
    fetch("http://localhost:8000/get_transcript", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_id: message.videoId }),
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        // Save to storage for popup to access
        chrome.storage.local.set({ transcript: data.transcript });
      }
    })
    .catch(err => console.error("Fetch error:", err));
  }
});
