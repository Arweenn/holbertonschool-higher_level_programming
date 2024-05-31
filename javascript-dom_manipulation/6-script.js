document.addEventListener('DOMContentLoaded', function () {
  const characterSection = document.querySelector('#character');
  const fetchPromise = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');

  fetchPromise
    .then(response => response.json())
    .then(data => characterSection.textContent = data.name);
});
