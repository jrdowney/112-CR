
function fetchCatalog() {
    // will create a GET AJAX req to API
    // get the list of movies
    // travel the array to get each movie
    // display the movie on HTML

    $.ajax({
        type: "GET",
        url: '/api/movies/?order_by=-release_year',
        success: function(res) {
            var list = res.objects;
            for(let i=0; i< list.length; i++) {
                displayMovie(list[i]);
            }
        },
        error: function(details){
            console.log("Error", details);
        }
    });
}

function displayMovie(movie){
    let container = $("#catalog");

    var syntax = 
    `<div class="card" style="width: 18rem;">
    <img src="${ movie.image_url }" class="card-img-top" alt="Movie image">
    <div class="card-body">
      <h4 class="card-title">${ movie.title }</h4>
      
    </div>
    <div class="card-footer text-muted mx-auto">
        <a href="/details/${movie.id}" class="btn btn-primary">See details</a>
    </div>
  </div>`

    container.append(syntax);
}

function init() {
    console.log('Catalog CSR page');

    fetchCatalog();
}

window.onload = init;

/*

    examples of POST API

*/

function example_CreateGenre() {
    let newGe = {
        name:"created using JS"
    };

    $.ajax({
        type: "POST",
        url: '/api/genres/',
        contentType: 'application/json',
        data: JSON.stringify(newGe),
        success: function(res) {
          console.log( 'Yeii obj created')
        },
        error: function(details){
            console.log("Error", details);
        }
    });
}

function example_CreateMovie() {
    let movie = {
        title: 'created using JS',
        director : 'something',
        release_year : 2020,
        price : 123.23,
        image_url : 'something',
        description : 'A super expensive movie',
        genre :  "/api/genres/3/" // trick
    }

    $.ajax({
        type: "POST",
        url: '/api/movies/',
        contentType: 'application/json',
        data: JSON.stringify(movie),
        success: function(res) {
          console.log( 'Yeii obj created')
        },
        error: function(details){
            console.log("Error", details);
        }
    });
}

