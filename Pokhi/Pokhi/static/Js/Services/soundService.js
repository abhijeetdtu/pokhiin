app.factory("soundService", [function () {
    createjs.Sound.registerSound("/static/Sounds/Symbolic Emotions.mp3", "Song");

    return {

        Play: function (id) {
            createjs.Sound.play("Song", {loop:-1});
        },

        Stop: function () {
            createjs.Sound.stop();
        }
    };

}]);