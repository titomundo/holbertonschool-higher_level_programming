const button = document.getElementById('toggle_header');
const el = document.querySelector('header');

button.addEventListener('click', () => {
  if (el.classList.contains('green')) {
    el.classList.replace('green', 'red');
  } else if (el.classList.contains('red')) {
    el.classList.replace('red', 'green');
  }
});
