document.addEventListener('DOMContentLoaded', function () {
  const helloTag = document.querySelector('#hello');
  const fetchPromise = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');

  fetchPromise
  .then(response => response.json())
  .then(data => helloTag.textContent = data.hello);
});
