document.addEventListener('DOMContentLoaded', function () {
  const colorChanger = document.querySelector('#red_header');
  const header = document.querySelector('header');
  colorChanger.addEventListener('click', function () {
    header.classList.add('red');
  });
});
