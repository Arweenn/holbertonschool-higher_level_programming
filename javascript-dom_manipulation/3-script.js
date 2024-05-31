document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  const toggle = document.querySelector('#toggle_header');
  toggle.addEventListener('click', function () {
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
});
