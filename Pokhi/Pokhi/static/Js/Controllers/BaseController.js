app.controller("BaseController", ["$scope" ,"fileService" , "displayService", function ($scope , fileService , displayService) {

    $scope.MainNavItems = displayService.getNavItems("Base" , "Main")
}])