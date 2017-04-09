app.controller("ResearchController", ["$scope","$sce", "displayService", function ($scope,$sce, displayService) {

    $scope.sce = $sce;
    displayService.getGraphItems(function (data) {
        if (data.success)
            $scope.graphItems = data.data;
        else
            $scope.graphItems = [];
    });
    
}])