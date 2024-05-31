document.addEventListener('DOMContentLoaded', function () {
  const listMovies = document.querySelector('#list_movies');
  const fetchPromise = fetch('https://swapi-api.hbtn.io/api/films/?format=json');

  fetchPromise
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const newItem = document.createElement('li');
      newItem.textContent = movie.title;
      listMovies.appendChild(newItem);
    });
  });
});
