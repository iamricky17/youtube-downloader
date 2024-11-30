const BACKEND_URL = 'http://127.0.0.1:5000';

async function fetchInfo() {
  const url = document.getElementById('youtube-url').value;
  if (!url) {
    alert('Please enter a valid YouTube URL.');
    return;
  }

  const response = await fetch(`${BACKEND_URL}/fetch-info`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url }),
  });

  const data = await response.json();
  if (data.error) {
    alert(`Error: ${data.error}`);
    return;
  }

  document.getElementById('video-details').innerText = data.formats;
}

async function download() {
  const url = document.getElementById('youtube-url').value;
  const quality = document.getElementById('format-code').value;

  if (!url || !quality) {
    alert('Please provide both URL and format code.');
    return;
  }

  const response = await fetch(`${BACKEND_URL}/download`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url, quality }),
  });

  const data = await response.json();
  if (data.error) {
    alert(`Error: ${data.error}`);
    return;
  }

  alert(data.message);
}
