app.factory('loginService', ['$http' , function ($http) {

    return {
        login: function (username , password , callback) {
            $http({
                url: "api/users/login",
                method: "POST",
                data: { "username": username , "password" : password }
            }).success(function (data, status, headers, config) {
                console.log("login return", data);
                callback(data.success);
                if (data.success == true)
                    console.log("success");
                else
                    console.log("fail");
            }).error(function (data, status, headers, config) {
                callback(status);
            });
        }
    }
}])