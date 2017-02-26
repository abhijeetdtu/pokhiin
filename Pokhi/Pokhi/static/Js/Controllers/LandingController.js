﻿app.controller("LandingController", ['$scope', '$rootScope', '$state','loginService', 'displayService' ,function ($scope,$rootScope, $state , loginService , displayService) {

    console.log("landing");
   
    $scope.GoHome = function () {
        console.log("going home");
        $state.go("home");
    }

    $scope.showLoader = false;
    $scope.isLoggedIn = null;

    $scope.showLoading = function () {
        $scope.showLoader = true;
    }

    $scope.hideLoading = function () {
        $scope.showLoader = false;
    }

    loginService.getCurrentUser(function (currentUser) {

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {
            console.log(toState);
            if (toState.name != 'home' && $scope.isLoggedIn == null)
                $state.go('home');

        });
        $rootScope.$on('$stateChangeSuccess', function (event, toState, toParams, fromState, fromParams) {

        });

        console.log("Got user", currentUser);
        $scope.isLoggedIn = currentUser;
        if ($scope.isLoggedIn != null)
            $state.go("base");
        else
            $state.go("home");
    });

    
  

    $scope.login = function () {
        console.log($scope.username, $scope.password);
        $scope.showLoading();
        loginService.login($scope.username, $scope.password, function (isLoggedIn) {
            if (isLoggedIn) {
                $state.go("base");
                $scope.isLoggedIn = isLoggedIn;
            }
            $scope.hideLoading();
        });
        
    }

    $scope.logout = function () {
        loginService.logout(function (isLoggedOut) {
            if (isLoggedOut) {
                $state.go("home");
                $scope.isLoggedIn = null;
            }
        });
    }
    d3.select("#logo").transition()
        .delay(500)
        .duration(3000)
        .styleTween("opacity", function () { return d3.interpolate(0,1); });
}])