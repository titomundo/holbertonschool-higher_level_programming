/**
 * task 6: Star wars character
 */

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

async function getData () {
  // fetch and jsonify data response
  const res = await fetch(url);
  const data = await res.json();

  const el = document.getElementById('character');
  el.textContent = data.name;
}

getData();
