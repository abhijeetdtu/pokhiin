app.directive("scrollShow", ["$window",  "$document" , function ($window , $document) {

    return {
        restrict: 'A',
        scope: {
            offset : '='
        },
        link: function (scope, elem, attrs, ctrl) {
            console.log($document[0].body.scrollTop)
            var newScroll;
            scope.scrollTop = $document[0].body.scrollTop;
            
            angular.element($window).bind("scroll", function (e) {
                newScroll = $document[0].body.scrollTop;
               
                elem.css("top", newScroll);
                console.log(newScroll , scope.scrollTop)
                if (newScroll - scope.scrollTop < 0) 
                    elem.show();
                else if (this.pageYOffset > scope.offset)
                    elem.hide();
                else
                    elem.show();

                scope.scrollTop = newScroll;
            })
        }
    }
}])