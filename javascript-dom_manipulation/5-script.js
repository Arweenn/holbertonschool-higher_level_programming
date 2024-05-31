document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  const updateHeader = document.querySelector('#update_header');

  updateHeader.addEventListener('click', function () {
	header.textContent = 'New Header!!!'
  });
});
