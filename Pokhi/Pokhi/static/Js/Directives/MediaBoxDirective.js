app.directive("mediaBox", ['$window' , function ($window) {

    return {
        restrict:'E',
        scope: {
            title:'=',
            summary:'=',
            content:'=',
            images: '=',
            keywords: '=',
            keypoints: '=',
            index: '&',
        },
        template:'<div ng-include="\'Views/Partials/MediaBox.html\'""></div>',
        //templateUrl : 'Views/Partials/MediaBox.html',
        link: function (scope, elem, attrs, ctrl) {
            scope.LazyLoadInstance = new LazyLoad();
            scope.MediaBodyClicked = function ( $event) {
                scope.showFullSummary = typeof (scope.showFullSummary) != undefined ? !scope.showFullSummary : true;
            }
            
            scope.safeSlice = function (arr, from, to) {
                if (arr === undefined || arr.length == 0)
                    return [];

                if (from > arr.length)
                    return [];

                var len = to - from + 1;
                var from = Math.min(from, arr.length - 1);
                var to = Math.min(to, arr.length);

                return arr.slice(from, to);
            }
            scope.scrollToTop = function (ev) {
                console.log($(elem)[0].offsetParent.offsetTop)
                $window.scrollTo(0, $(elem)[0].offsetParent.offsetTop);
            }
            

        }
    }

}]);