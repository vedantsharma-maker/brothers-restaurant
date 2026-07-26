async function loadRestaurants() {

    const response = await fetch("http://127.0.0.1:800/restaurants");

    const restaurants = await response.json();

    console.log(restaurants);


}

fetch("http://127.0.0.1:8000/restaurants")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
