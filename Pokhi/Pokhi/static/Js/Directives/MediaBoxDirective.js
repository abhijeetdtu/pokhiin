app.directive("mediaBox", [function () {

    return {
        restrict:'E',
        scope: {
            title:'=',
            summary:'=',
            content:'=',
            images: '=',
            keywords: '=',
            keypoints: '=',
            index: '&'
        },
        template:'<div ng-include="\'Views/Partials/MediaBox.html\'" onload="init();"></div>',
        //templateUrl : 'Views/Partials/MediaBox.html',
        link: function (scope, elem, attrs, ctrl) {
            scope.LazyLoadInstance = new LazyLoad();
            scope.MediaBodyClicked = function ( $event) {
                scope.showFullSummary = typeof (scope.showFullSummary) != undefined ? !scope.showFullSummary : true;
            }
            
            scope.safeSlice = function (arr, from, to) {

                if (from > arr.length)
                    return [];

                if (arr.length == 0)
                    return [];

                var len = to - from + 1;
                var from = Math.min(from, arr.length - 1);
                var to = Math.min(to, arr.length);

                return arr.slice(from, to);
            }

           
            

        }
    }

}]);