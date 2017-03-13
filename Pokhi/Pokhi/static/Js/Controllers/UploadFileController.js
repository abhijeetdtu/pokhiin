app.controller("UploadFileController", ['$scope', 'fileService', 'displayService' , function ($scope,fileService , displayService) {

    $scope.PostFile = function () {
        fileService.uploadFile($("form[name=fileUploadForm]")[0], function (done , data) {
            if (done) {
                displayService.ShowModal($scope ,'UploadFileModal', 'Success', data.msg);
            }
            else
                displayService.ShowModal($scope, 'UploadFileModal', 'Error', data.msg)
        });
    }

}]);
