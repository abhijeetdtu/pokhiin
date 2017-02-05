app.controller("HomeController", ["$scope", 'loginService' , function ($scope , loginService) {
    console.log("home")
    $scope.message = "Welcome to home";

    $scope.login = function () {
        console.log($scope.username, $scope.password);
        loginService.login($scope.username, $scope.password);
    }
}])