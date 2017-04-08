app.factory("soundService", ["$timeout" , function ($timeout) {
    //createjs.Sound.registerSound("/static/Sounds/Symbolic Emotions.mp3", "Song");

    var toPlay = {};

    createjs.Sound.addEventListener("fileload", handleFileLoad);
    function handleFileLoad(event) {
        // A sound has been preloaded.
        console.log(event, "sound loaded")
        if (toPlay[event.id]) {
            createjs.Sound.play(event.id, { loop: -1 });
            toPlay[event.id](true);
            toPlay[event.id] = true;
        }
    }

    var nxOnLoadFunctions = [];
    var nxLoaded = false;
    nx.onload = function () {
        nx.globalWidgets = false;
        console.log("nxloaded" , nxOnLoadFunctions , nx)
        nxLoaded = true;
        for (var i = 0 ; i < nxOnLoadFunctions.length; i++)
            nxOnLoadFunctions[i](nx);
    }


    return {

        Play: function (id, callback) {
            if (toPlay[id] == true) {
                //To make async always
                $timeout(function(){
                    callback(true);
                    createjs.Sound.play("Song", { loop: -1 });
                })
            }
            else   
                toPlay[id] = callback;
            //
        },

        Stop: function () {
            createjs.Sound.stop();
        },
        OnNxLoad: function (func) {
            if (nxLoaded)
                func(nx);
            else
                nxOnLoadFunctions.push(func);
        }
        
    };

}]);