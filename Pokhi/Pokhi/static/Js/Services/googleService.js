app.factory("googleService", ["$http", function ($http) {

    var _googleBaseURL = "https://google.co.in/custom?btnG=Search&q=";
    var iframeElem = "<iframe href='$HREF$' class='$CLASSNAME$' ng-init='LazyLoadInstance.update();'></iframe>";

    var _getGoogleURLForQuery = function (query) {
        return encodeURI(_googleBaseURL + query.split(" ").join("+"));
    }

    var _getIframeForQuery = function (query, cls) {
        cls = cls === undefined ? "" : cls;
        return iframeElem.replace("$HREF$", _getGoogleLinkForQuery(query)).replace("$CLASSNAME$" , cls);
    }


    return {
        GetIFrameForQuery: _getIframeForQuery,
        GetURLForQuery: _getGoogleURLForQuery
    }
}]);