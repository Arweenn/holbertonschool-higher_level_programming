document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});
