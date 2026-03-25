const button = document.getElementById('add_item');
const el = document.querySelector('.my_list');

button.addEventListener('click', () => {
  const child = document.createElement('li');
  child.innerHTML = 'Item';
  el.appendChild(child);
});
