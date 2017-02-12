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
        },

        logout: function (callback) {
            $http({
                url: "api/users/logout",
                method: "GET",
            }).success(function (data, status, headers, config) {
                console.log("logout return", data);
                callback(data.success);
                if (data.success == true)
                    console.log("success");
                else
                    console.log("fail");
            }).error(function (data, status, headers, config) {
                callback(status);
            });
        },


        getCurrentUser: function (callback) {
            $http({
                url: "api/users/getcurrentuser",
                method: "GET",
            }).success(function (data, status, headers, config) {
                if (typeof data != 'undefined' && data.success) {
                    console.log("currentuser", data.data);
                    //callback(data.success);
                    if (data.data.isAuthenticated == 'true') {
                        console.log("success");
                        currentUser = data.data;          
                    }
                    else {
                        currentUser = null;
                        console.log("fail");
                    }
                    callback(currentUser);
                }
            }).error(function (data, status, headers, config) {
                callback(status);
            });
        }
    }
}])