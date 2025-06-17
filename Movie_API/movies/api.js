async function fetchData() {
  try {
    const response = await fetch('http://localhost:8000/api/movies/');
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Fetch error:', error);
  }
}

fetchData();
