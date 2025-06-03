function getYouTubeVideoID() {
  const url = window.location.href;
  if (url.includes("watch?v=")) {
    return new URLSearchParams(window.location.search).get("v");
  }
  return null;
}

let lastVideoId = null;

setInterval(() => {
  const currentId = getYouTubeVideoID();
  if (currentId && currentId !== lastVideoId) {
    lastVideoId = currentId;
    chrome.runtime.sendMessage({ type: "video_id_changed", videoId: currentId });
  }
}, 1000);
