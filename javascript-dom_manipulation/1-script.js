const colorChanger = document.querySelector('#red_header');
const header = document.querySelector('header');
colorChanger.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
