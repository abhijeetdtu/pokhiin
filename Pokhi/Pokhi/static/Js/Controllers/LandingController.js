app.controller("LandingController", ['$scope', '$state','loginService' ,function ($scope, $state , loginService) {

    console.log("landing");
    $state.go("home");
    $scope.GoHome = function () {
        console.log("going home");
        $state.go("home");
    }

    $scope.isLoggedIn = $("#isLoggedIn").val() == 'False' ? false : true;

    $scope.login = function () {
        console.log($scope.username, $scope.password);
        loginService.login($scope.username, $scope.password, function (isLoggedIn) {
            if (isLoggedIn) {
                $state.go("base");
                $scope.isLoggedIn = isLoggedIn;
            }
        });
    }
}])