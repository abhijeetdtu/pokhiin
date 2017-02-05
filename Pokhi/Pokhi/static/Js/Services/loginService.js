app.factory('loginService', ['$http' , function ($http) {

    return {
        login: function (username , password) {
            $http({
                url: "api/login",
                method: "POST",
                data: { "username": username , "password" : password }
            }).success(function (data, status, headers, config) {
                $scope.data = data;
                console.log("login return", data);
            }).error(function (data, status, headers, config) {
                $scope.status = status;
                console.log("login return", data);
            });
        }
    }
}])