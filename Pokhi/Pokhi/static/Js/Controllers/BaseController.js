app.controller("BaseController", ["$scope" ,"fileService" ,function ($scope , fileService) {

    $scope.PostFile = function () {
        console.log($("#fileUpload").prop("files"));
        fileService.uploadFile($("#fileUpload").prop("files"));
    }
}])