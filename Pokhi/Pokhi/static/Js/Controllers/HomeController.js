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
        var circle = new createjs.Shape();
        circle.graphics.beginFill("DeepSkyBlue").drawCircle(0, 0, 50);
        circle.x = 100;
        circle.y = 100;
        stage.addChild(circle);
        stage.update();
        
        createjs.Ticker.setInterval(25);
        createjs.Ticker.setFPS(40);

        createjs.Ticker.addEventListener("tick", function (event){ 
            circle.x += event.delta / 1000 * 100;

            circle.x %= window.innerWidth;
            // this will log a steadily increasing value:
            //console.log("total time: "+createjs.Ticker.getTime());
            stage.update();
        });
    }

    $scope.Canvas();
}])