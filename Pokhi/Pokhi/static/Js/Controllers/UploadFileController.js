app.controller("UploadFileController", ['$scope', 'fileService', 'displayService' , function ($scope,fileService , displayService) {

    $scope.DeleteFile = function (id) {
        displayService.showLoading($scope);
        fileService.deleteFile(id, function (success , data) {
            if (success) {
                displayService.ShowModal($scope, 'UploadFileModal', 'Success', data.msg);
            }
            $scope.GetUploadedFilesForUser();
            displayService.hideLoading($scope);
        });
    }
    $scope.GetUploadedFilesForUser = function () {
        fileService.getAllUploadedFilesForUser(function (success , files) {
            $scope.userFiles = files;
            //$scope.$apply();
        })
    }
    $scope.PostFile = function () {
        displayService.showLoading($scope);
        fileService.uploadFile($("form[name=fileUploadForm]")[0], function (done , data) {
            if (done) {
                displayService.ShowModal($scope ,'UploadFileModal', 'Success', data.msg);
            }
            else
                displayService.ShowModal($scope, 'UploadFileModal', 'Error', data.msg)
            $scope.GetUploadedFilesForUser();
            displayService.hideLoading($scope);
        });

    }

    $scope.GetUploadedFilesForUser();
}]);
