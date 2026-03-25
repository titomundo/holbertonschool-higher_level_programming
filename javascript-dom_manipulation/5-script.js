const button = document.getElementById('update_header');
const el = document.querySelector('header');

button.addEventListener('click', () => {
  el.textContent = 'New Header!!!';
});
