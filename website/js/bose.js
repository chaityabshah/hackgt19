var currentFrameNumber = 1065;
function getUsers() {
    fetch("/getUsers")
    .then(function(response) {
        return response.json();
      })
      .then(function(presentCustomers) {
        updatePeople(presentCustomers);
      });
}

function displayPies(selected)  {
    console.log(selected);
    fetch("/getUserData/" + selected)
    .then(function(response) {
        return response.json();
    })
    .then(function(dist) {
        fetch("/getUsers")
        .then(function(response) {
            return response.json();
        })
        .then(function(presentCustomers) {
            var name = "";
            for (var i = 0; i < presentCustomers.length; i++) {
                if (presentCustomers[i].id == selected) {
                    name = presentCustomers[i].name;
                }
            }
            clearPies();
            visCompanyPie(dist[0], name);
            visDevicePie(dist[1], name);
            visTopSongs();

        });
    });
}

function visTopSongs() {
    songs = [["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"], ["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"],["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"]];
    
    top_songs = document.getElementById("top_songs");
    for (var i = 0; i < songs.length; i++) {
        img_url = songs[i][0];
        title = songs[i][1];
        
        var p = document.createElement('p');
        var span = document.createElement('span');
        var img = document.createElement('img');
        img.className = "ui avatar image";
        img.src = img_url;
        span.innerHTML = (i+1) + ". " + title;
        top_songs.appendChild(p);
        p.appendChild(img);
        p.appendChild(span);
    }
    //"<p><img class=\"ui avatar image\" src=\""+img_url+"\"> "+ title + "</p>"
}