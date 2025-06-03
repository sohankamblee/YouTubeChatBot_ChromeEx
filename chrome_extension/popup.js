document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.local.get(["transcript"], (result) => {
    const div = document.getElementById("transcript");
    if (result.transcript) {
      div.textContent = result.transcript;
    } else {
      div.textContent = "Transcript not available.";
    }
  });
});

