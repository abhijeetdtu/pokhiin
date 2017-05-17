app.directive("scrollLoad", ["$window" ,"$document", "displayService" ,function ($window , $document , displayService) {

    return {
        restrict:'E'
        ,scope: {
            onBottomReached : "="
        }
        , template: function () { return "<div class='virtual-scroll' style='height:50px'></div>" }

        , link: function ($scope, elem, attrs, ctrl) {
            console.log("scroll load", elem);
            $scope.triggered = false;
            
            angular.element($window).bind("scroll" , function () {

                if ($document[0].body.scrollTop + $window.innerHeight >= $document[0].body.scrollHeight) {
                    //console.log("reached bottom");
                    if ($scope.triggered === false) {
                        displayService.showLoading($scope,elem[0].querySelector(".virtual-scroll"));
                        $scope.triggered = true;
                        $scope.onBottomReached(function ($scope) {
                            return function () {
                                console.log("reached bottom execution complete");
                                $scope.triggered = false;
                                displayService.hideLoading($scope,elem[0].querySelector(".virtual-scroll"))
                            }
                        }($scope));
                    }
                    
                    
                }
            })
        }

    }
}])