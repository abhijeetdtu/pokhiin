app.controller("HomeController", ["$scope", '$timeout', 'loginService' ,'displayService' , function ($scope ,$timeout, loginService , displayService) {
    console.log("home")

    $scope.MainNavItems = displayService.getNavItems("Home", "Main");
    $scope.NavItems = {};

    $scope.NavItems["Labs"] = displayService.getNavItems("Labs", "Main");
    $scope.NavItems["Showcase"] = displayService.getNavItems("Showcase", "Main");

    $scope.TotalNavItems = [];
    for (var i in $scope.NavItems)
        $scope.TotalNavItems = $scope.TotalNavItems.concat($scope.NavItems[i].map(function (d,index) {
            console.log(d, index);
            d.push(i);
            d.push(index == 0);
            console.log(d, index);
            return d;
        }));
    console.log($scope.TotalNavItems);
    $scope.selectedThumbnail = null;
    //$scope.canvasResize();
}])