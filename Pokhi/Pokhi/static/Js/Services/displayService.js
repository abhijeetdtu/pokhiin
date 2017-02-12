app.factory("displayService", [function () {

    var showingLoader = false;

    return {
        showLoader: function () {
            showingLoader = true;
            return true;
        },

        hideLoader: function () {
            showingLoader = false;
            return false;
        },

        getNavItems: function (viewName , navId) {
            switch (viewName) {
                case 'Home':
                    switch (navId) {
                        case 'Main':
                            return [['Research', 'glyphicon glyphicon-stats' , 'Views/Partials/Research.html']
                                , ['Music', 'glyphicon glyphicon-headphones', 'Views/Partials/Music.html']
                                , ['Geek', 'glyphicon glyphicon-qrcode', 'Views/Partials/Geek.html']
                            ]
                            break;
                    }
                    break;
            }
        }
    }
}])