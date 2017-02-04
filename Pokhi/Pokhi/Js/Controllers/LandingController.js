app.controller("LandingController", ['$scope', '$state', function ($scope, $state) {

    $scope.GoHome = function () {
        console.log("going home");
        $state.go("home");
    }
    
}])