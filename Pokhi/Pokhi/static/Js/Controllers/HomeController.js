app.controller("HomeController", ["$scope", '$timeout', 'loginService' , function ($scope ,$timeout, loginService) {
    console.log("home")

   
    $scope.GetRandomColor = function () {
        return "rgb(" + Math.floor(Math.random() * 155 + 100) + "," + Math.floor(Math.random() * 155 + +100) + "," + Math.floor(Math.random() * 155 + +100) + ")";
    }


    $scope.CreateCircle = function (stage,x) {
        if (x == null || typeof x == 'undefined')
            x = Math.random() * stage.canvas.width;
        var circle = new createjs.Shape();
        circle.graphics.beginFill($scope.GetRandomColor()).drawCircle(x, Math.random() * window.innerHeight, 10 + 40 * Math.random());
        stage.addChild(circle);
        createjs.Tween.get(circle, { loop: true })
             .to({ scale : 0.8 }, 500*Math.random() + 500, createjs.Ease.getPowInOut(4))
             .to({ alpha: 0 }, 1000 * Math.random() + 500, createjs.Ease.getPowInOut(2))
             .to({ alpha: 1 }, 1000 * Math.random() + 500, createjs.Ease.getPowInOut(2))
             .to({ scale: 1 / 0.8 }, 1000, createjs.Ease.getPowInOut(4));

    }

    $scope.Canvas = function () {
        var stage = new createjs.Stage("viewport");
        console.log(stage.canvas.width)

        $scope.CreateCircle(stage , 0);
        for (var i = 0 ; i < 100 ; i++) {
            $scope.CreateCircle(stage);
        }
        createjs.Ticker.setFPS(60);
        createjs.Ticker.addEventListener("tick", stage);
    }

    $scope.canvasResize = function () {
        console.log("REsizing", document.getElementById("canvasHolder").clientWidth);
        var canvasHolder = document.getElementById("canvasHolder");
        var width = canvasHolder.clientWidth;
        $("#viewport").attr("width", width);
        $scope.Canvas();
    }
    $(window).on("resize", $scope.canvasResize);
    $timeout(function () { $scope.canvasResize()}, 50);

    //$scope.canvasResize();
}])