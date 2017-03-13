app.controller("LandingController",
    [   '$scope',
        '$rootScope',
        '$state',
        '$timeout',
        'loginService',
        'displayService',
        'soundService',
    function ($scope, $rootScope, $state,$timeout, loginService, displayService, soundService) {



    $scope.GoHome = function () {
        console.log("going home");
        $state.go("home");
    }

    $scope.showLoader = false;
    $scope.isLoggedIn = null;

    $scope.showLoading = function (elemSelector) {
        if(elemSelector)
            $(elemSelector).append($("#loader"));
        $scope.showLoader = true;
    }

    $scope.hideLoading = function (elemSelector) {
        if (elemSelector) {
            $(body).append($("#loader"));
            $(elemSelector).remove($("#loader"));
        }
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
        displayService.showLoading($scope);
        loginService.login($scope.username, $scope.password, function (isLoggedIn) {
            if (isLoggedIn) {
                $state.go("base");
                $scope.isLoggedIn = isLoggedIn;
            }
            else 
                displayService.ShowModal($scope, 'LoginMessageModal', 'Error', 'Invalid username or password');
           
            displayService.hideLoading($scope);
            
        });
        
    }

    $scope.logout = function () {
        displayService.showLoading($scope);
        loginService.logout(function (isLoggedOut) {
            if (isLoggedOut) {
                $state.go("home");
                $scope.isLoggedIn = null;
            }
            displayService.hideLoading($scope);
        });
    }
    d3.select("#logo").transition()
        .delay(500)
        .duration(3000)
        .styleTween("opacity", function () { return d3.interpolate(0, 1); });

    $timeout(function () {
        $scope.PlayMusic();
    },10000)

    $scope.StopMusic = function () {
        soundService.Stop();
        $scope.playing = false;
    }


    $scope.PlayMusic = function () {
        soundService.Play();
        $scope.playing = true;
    }
}])