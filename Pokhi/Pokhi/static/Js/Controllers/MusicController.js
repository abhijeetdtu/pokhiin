app.controller("MusicController", ['$scope', 'soundService' , function ($scope , soundService) {


    $scope.GridSize = [10, 10];
    $scope.Play = function () {
        
    }
    //play a middle 'C' for the duration of an 8th note
    
    $scope.onClick = function (data) {
       // console.log("click", data);
    }

    $scope.onSq = function (mtx) {
        $scope.mtx = mtx;
        console.log("Setting up seq");
       
    }
    
}]);