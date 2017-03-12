app.factory("displayService", [function () {

    var showingLoader = false;
    var navItems = {};
    navItems["Home"] = {};
    navItems["Home"]["Main"] = [['Research', 'glyphicon glyphicon-stats', 'Views/Partials/Research.html']
                                , ['Music', 'glyphicon glyphicon-headphones', 'Views/Partials/Music.html']
                                , ['Geek', 'glyphicon glyphicon-qrcode', 'Views/Partials/Geek.html']
                                , ['Pong', 'glyphicon glyphicon-qrcode', 'Apps/Pong/index.html']]

    navItems["Base"] = {};
    navItems["Base"]["Main"] = [['Upload', 'glyphicon glyphicon-stats', 'Views/Partials/UploadFile.html']]

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
        }
    }
}])