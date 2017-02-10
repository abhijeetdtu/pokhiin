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
        }
    }
}])