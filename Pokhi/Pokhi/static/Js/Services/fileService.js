app.factory("fileService", ["$http" , function ($http) {

    var uploadFile = function (file) {

    }
    return {
        uploadFile: function (form, callback) {
            var formData = new FormData(form);
            $http({
                url: "api/files/uploadFile",
                method: "POST",
                data: formData,
                cache: false,
                headers: { 'Content-Type': undefined },
                transformRequest: angular.identity
            }).success(function (data, status, headers, config) {           
                console.log("success return", data);
                callback(data.success , data);;
            }).error(function (data, status, headers, config) {
                console.log("error return", data);
                callback(data.success ,status);
            });
        }
    }
}])