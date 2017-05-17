app.factory("displayService", ['$compile' ,"$http",'$timeout',function ($compile , $http , $timeout) {

    var showingLoader = false;
    var navItems = {};
    navItems["Home"] = {};
    //navItems["Home"]["Main"] = [//['Research', 'glyphicon glyphicon-stats', 'Views/Partials/Research.html'],
    //                             ['GraphsAPI', 'glyphicon glyphicon-stats', 'Views/Partials/SelfServiceGraphs.html']
    //                            , ['Music', 'glyphicon glyphicon-headphones', 'Views/Partials/Music.html']
    //                            //, ['Geek', 'glyphicon glyphicon-qrcode', 'Views/Partials/Geek.html']
    //                            , ['Pong', 'glyphicon glyphicon-qrcode', 'Apps/Pong/index.html']]

    navItems["Home"]["Main"] = [    ['Labs', 'static/Images/LabsBanner2.jpg', 'Views/Partials/SelfServiceGraphs.html']
                                   , ['Showcase', 'static/Images/ShowcaseBanner.jpg', 'Views/Partials/Music.html']
                                ]

    navItems["Labs"] = {};
    navItems["Labs"]["Main"] = [
                                ['Research', 'glyphicon glyphicon-stats', 'Views/Partials/Research.html']
                                ,['Graphs', 'static/Images/LabsBanner2.jpg', 'Views/Partials/SelfServiceGraphs.html']
                                ]

    navItems["Showcase"] = {};
    navItems["Showcase"]["Main"] = [
                                    ['WikiFeed', 'glyphicon glyphicon-headphones', 'Views/Partials/WikipediaFeed.html']
                                 ,['Music', 'glyphicon glyphicon-headphones', 'Views/Partials/Music.html']
                                , ['Pong', 'glyphicon glyphicon-qrcode', 'Apps/Pong/index.html']
                                ]

    navItems["Base"] = {};
    navItems["Base"]["Main"] = [['Upload', 'glyphicon glyphicon-cloud-upload', 'Views/Partials/UploadFile.html']];

    navItems["Config"] = {};
    navItems["Config"].thumbnailHeight = 50;
    var ErrorMsg = "Welcome Error";


    var GetRandomColor = function () {
        return "rgb(" + Math.floor(Math.random() * 155 + 100) + "," + Math.floor(Math.random() * 155 + +100) + "," + Math.floor(Math.random() * 155 + +100) + ")";
    }


    var CreateCircle = function (stage, x) {
        if (x == null || typeof x == 'undefined')
            x = Math.random() * stage.canvas.width;
        var circle = new createjs.Shape();
        circle.graphics.beginFill(GetRandomColor()).drawCircle(x, Math.random() * window.innerHeight, 10 + 40 * Math.random());
        stage.addChild(circle);
        createjs.Tween.get(circle, { loop: true })
             .to({ scale: 0.8 }, 500 * Math.random() + 500, createjs.Ease.getPowInOut(4))
             .to({ alpha: 0 }, 1000 * Math.random() + 500, createjs.Ease.getPowInOut(2))
             .to({ alpha: 1 }, 1000 * Math.random() + 500, createjs.Ease.getPowInOut(2))
             .to({ scale: 1 / 0.8 }, 1000, createjs.Ease.getPowInOut(4));

    }

    var _Canvas = function () {
        var stage = new createjs.Stage("viewport");
        console.log(stage.canvas.width)

        CreateCircle(stage, 0);
        for (var i = 0 ; i < 100 ; i++) {
            CreateCircle(stage);
        }
        createjs.Ticker.setFPS(60);
        createjs.Ticker.addEventListener("tick", stage);
    }

    var canvasResize = function () {
        console.log("REsizing", document.getElementById("canvasHolder").clientWidth);
        var canvasHolder = document.getElementById("canvasHolder");
        var width = canvasHolder.clientWidth * 0.95;
        $("#viewport").attr("width", width);
        $("#viewport").attr("height", 50);
        _Canvas();
    }
    $(window).on("resize", canvasResize);
    $timeout(function () { canvasResize() }, 50);

    return {
       showLoading: function (scope,elem) {
            scope.showLoader = true;
            var isGlobal = elem ? false : true;
            var loader = $compile("<loader show='true' is-global="+isGlobal+"/>")(scope);
            if (elem)
                $(elem).append(loader);
            else
                $("body").append(loader);
        },

        hideLoading: function (scope , elem) {
            scope.showLoader = false;
            if (elem)
                $(elem).find("loader").remove();
            else
                $("body").find("loader").remove();
        },

        ShowModal : function (scope ,modalId, type, msg) {
            scope.ModalType = type;
            scope.ModalMsg = msg;
            $("#"+modalId).modal('show');
        },
        getNavItems: function (viewName, navId) {
            return navItems[viewName][navId];
            switch (viewName) {
                case 'Home':
                    switch (navId) {
                        case 'Main':
                            return navItems[viewName][navId];
                            break;
                    }
                    break;

                case 'Base':
                    switch (navId) {
                        case 'Main':
                            return navItems["Home"]["Main"].concat(navItems["Base"]["Main"])
                            break;
                    }
                    break;
            }
        },

        getGraphItems: function (callback) {
            $http({
                url: "/api/research/getGraphItems",
            }).success(function (data) {
                callback(data);
            })
        }
        , canvasResize: canvasResize
      


    }
}])

