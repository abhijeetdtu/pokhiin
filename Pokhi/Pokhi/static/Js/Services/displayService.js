app.factory("displayService", ['$compile' ,"$http", function ($compile , $http) {

    var showingLoader = false;
    var navItems = {};
    navItems["Home"] = {};
    navItems["Home"]["Main"] = [['Research', 'glyphicon glyphicon-stats', 'Views/Partials/Research.html']
                                , ['Music', 'glyphicon glyphicon-headphones', 'Views/Partials/Music.html']
                                , ['Geek', 'glyphicon glyphicon-qrcode', 'Views/Partials/Geek.html']
                                , ['Pong', 'glyphicon glyphicon-qrcode', 'Apps/Pong/index.html']]

    navItems["Base"] = {};
    navItems["Base"]["Main"] = [['Upload', 'glyphicon glyphicon-cloud-upload', 'Views/Partials/UploadFile.html']]
    var ErrorMsg = "Welcome Error";
    return {
        showLoading: function (scope,elem) {
            scope.showLoader = true;
            var isGlobal = elem ? false : true;
            var loader = $compile("<loader show='true'/>")(scope);
            if (elem)
                elem.append(loader);
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
        getNavItems: function (viewName , navId) {
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
    }
}])

