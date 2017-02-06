app.controller("HomeController", ["$scope", 'loginService' , function ($scope , loginService) {
    console.log("home")
    $scope.message = "Welcome to home";

    $scope.login = function () {
        console.log($scope.username, $scope.password);
        loginService.login($scope.username, $scope.password, function (isLoggedIn) {
            if(isLoggedIn)
                $state.go("base")
        });
    }

    $scope.Canvas = function () {
        
        var canvas = document.getElementById("viewport");
        canvas.clientWidth = window.innerWidth;
        //canvas.clientHeight = window.innerheight;

        var stage = new createjs.Stage("viewport");
        console.log(stage)
        var circles = [];
        for (var i = 0 ; i < 100 ; i++) {
            var circle = new createjs.Shape();
            circle.graphics.beginFill("DeepSkyBlue").drawCircle(Math.random() * window.innerWidth, Math.random() * window.innerHeight, 10 + 40*Math.random());

            circles.push(circle);
            stage.addChild(circle);
            stage.update();

        }

        createjs.Ticker.setInterval(25);
        createjs.Ticker.setFPS(40);        
        createjs.Ticker.addEventListener("tick", function (event) {
            for (var i = 0 ; i < 100 ; i++) {
                circles[i].x += (event.delta / 1000) * Math.random()*80 + 1;
                circles[i].x %= window.innerWidth;
            }
            // this will log a steadily increasing value:
            //console.log("total time: "+createjs.Ticker.getTime());
            stage.update();
        });
    }

    $scope.Canvas();
}])