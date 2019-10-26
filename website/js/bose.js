var currentFrameNumber = 1065;
var currentFrame = $('#currentFrame');
function getUsers() {
    fetch("/getCustomers/" + currentFrameNumber)
    .then(function(response) {
        return response.json();
      })
      .then(function(presentCustomers) {
        updatePeople(presentCustomers);
      });
}


function displayPies(selected)  {
    console.log(selected);
    fetch("/getPie/" + currentFrameNumber + "/" + selected)
    .then(function(response) {
        return response.json();
    })
    .then(function(dist) {
        fetch("/getCustomers/" + currentFrameNumber)
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

        });
    });
}



/*
setInterval(function() {
    

    
}, 600)
*/