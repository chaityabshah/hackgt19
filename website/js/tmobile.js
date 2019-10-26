var currentFrameNumber = 0;
var currentFrame = $('#currentFrame');
var video = VideoFrame({
    id : 'video',
    frameRate: 24,
    callback : function(frame) {
        currentFrameNumber = frame;
    }
});
video.listen('frame')



setInterval(function() {
    if (selected) {
        
        
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



    } else {
        
        fetch("/getPie/" + currentFrameNumber + "/0")
            .then(function(response) {
                return response.json();
            })
            .then(function(dist) {
                clearPies();
                visCompanyPie(dist[0], "");
                visDevicePie(dist[1], "");

            });
        
    }


    fetch("/getCustomers/" + currentFrameNumber)
    .then(function(response) {
        return response.json();
      })
      .then(function(presentCustomers) {

        updatePeople(presentCustomers);

      });

}, 600)


setInterval(function() {


    if (selected) {
    document.getElementById("video_overlays").src = "/updateHeatMap/" + currentFrameNumber + "/" + selected;
    } else {
    document.getElementById("video_overlays").src = "/updateHeatMap/" + currentFrameNumber + "/" + 0;
    }
}, 1000)




