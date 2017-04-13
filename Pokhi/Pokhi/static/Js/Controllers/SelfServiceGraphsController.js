app.controller("SelfServiceGraphsController", ["$scope", "visualizationService" , function ($scope , visService) {

    $scope.type = "bar";
    $scope.measureSelected = {};

    visService.GetResource(function(data){
        $scope.data = data;
        $scope.records = data.records;
        $scope.fields = data.fields;
        $scope.generateChart("#graph", $scope.data, $scope.type);
    })

    $scope.measureSelect = function (measure) {
        $scope.measureSelected[measure] = !$scope.measureSelected[measure];       
        $scope.generateChart("#graph", $scope.data, $scope.type,$scope.x , $scope.y);
    }
    $scope.generateChart = function (elemId, json, type, x,y) {
        console.log($scope.measureSelected)
        var measureList = Object.keys($scope.measureSelected).filter(function (d) { return $scope.measureSelected[d] == true; });
        if (measureList.length == 0) return;

        var keysF = [];
        if(!(x == null || x == undefined))
            keysF.push(x);
        if(!(y == null || y == undefined))
            keysF.push(y);
      
        chart = c3.generate({
            bindto: elemId,
            zoom: {
                enabled:true
            },
            data: {
                type : type,
                json: json.records,
                keys: {
                    //                x: 'name', // it's possible to specify 'x' when category axis
                    value:measureList
                }
            },
           
        });
    }
    
}])