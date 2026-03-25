/**
 * task 8: Say Hello!
 */

const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

async function getData () {
  // fetch and jsonify data response
  const res = await fetch(url);
  const data = await res.json();
  const el = document.getElementById('hello');
  el.textContent = data.hello;
}

getData();
