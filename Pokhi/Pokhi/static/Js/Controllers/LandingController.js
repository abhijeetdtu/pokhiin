app.controller("LandingController", ['$scope', '$state', function ($scope, $state) {

    console.log("landing");
    $state.go("home");
    $scope.GoHome = function () {
        console.log("going home");
        $state.go("home");
    }
    
}])