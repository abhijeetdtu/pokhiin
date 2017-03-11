app.factory("fileService", ["$http" , function ($http) {

    var uploadFile = function (file) {

    }
    return {
        uploadFile: function (files) {
            var formData = new FormData();

            // Loop through each of the selected files.
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                // Add the file to the request.
                formData.append('files', file);
            }

            console.log(formData);
            $http({
                url: "api/files/uploadFile",
                method: "POST",
                data: formData,
                cache: false,
                headers: { 'Content-Type': undefined },
                transformRequest: angular.identity
            }).success(function (data, status, headers, config) {
                console.log("success return", data);
                //callback(data.success);;
            }).error(function (data, status, headers, config) {
                console.log("error return", data);
                //callback(status);
            });
        }
    }
}])