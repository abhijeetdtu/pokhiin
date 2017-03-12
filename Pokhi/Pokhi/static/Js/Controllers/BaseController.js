app.controller("BaseController", ["$scope" ,"fileService" , "displayService", function ($scope , fileService , displayService) {

    $scope.PostFile = function () {
        fileService.uploadFile($("#fileUpload").prop("files"));
    }

    $scope.MainNavItems = displayService.getNavItems("Base" , "Main")
}])