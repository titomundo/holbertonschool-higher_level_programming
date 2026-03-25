/**
 * task 7: Star wars movies
 */

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

async function getData () {
  // fetch and jsonify data response
  const res = await fetch(url);
  const data = await res.json();
  const el = document.getElementById('list_movies');

  data.results.forEach(element => {
    const children = document.createElement('li');
    children.textContent = element.title;
    el.appendChild(children);
  });
}

getData();
