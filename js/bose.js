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
    fetch("/getUserData/" + selected)
    .then(function(response) {
        return response.json();
    })
    .then(function(dist) {
        fetch("/getTop5/" + selected)
            .then(function(response) {
                return response.json();
            })
            .then(function(top5) {
                fetch("/getGenres/" + selected)
                .then(function(response) {
                    return response.json();
                })
                .then(function(genres)  {
                    fetch("/getValence/" + selected)
                    .then(function(response) {
                        return response.json();
                    })
                    .then(function(valence) {
                        console.log(valence)
                        var name = selected;
                        clearPies();
                        console.log(genres);
                        visCompanyPie(genres, name);
                        clearGauge();
                        var powerGauge = gauge('#power-gauge', {
                            size: 350,
                            clipWidth: 350,
                            clipHeight: 200,
                            ringWidth: 60,
                            maxValue: 1,
                            transitionMs: 4000,
                        });
                        powerGauge.render();
                        powerGauge.update(valence);
                        //visDevicePie(dist[1], name);
                        clearTopSongs();
                        visTopSongs(top5);
                        //clearHist();
                        //visualizeHist(dist[2], name);
                        clearLineChart();
                        if (dist["volume"]!= undefined) {
                            visLineChart(dist, "volume", "linechart");
                        }
                        if (dist["bass"] != undefined) {
                            visLineChart(dist, "bass", "linechart1");
                        }
                    });

                })
            })
    });
}

function clearTopSongs() {
    top_songs = document.getElementById("top_songs");
    top_songs.innerHTML = '';
}
function visTopSongs(top5) {
    //songs = [["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"], ["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"],["https://semantic-ui.com/images/avatar/small/jenny.jpg", "Old Town Road - Lil Nas X"]];
    
    top_songs = document.getElementById("top_songs");
    for (var i = 0; i < top5[0].length; i++) {
        img_url = top5[1][i];
        title = top5[0][i];
        
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
}