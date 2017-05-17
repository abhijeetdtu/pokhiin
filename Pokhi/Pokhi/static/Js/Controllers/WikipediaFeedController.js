app.controller("WikipediaFeedController", ["$scope" ,"wikipediaService", function ($scope , wikiService) {

    $scope.pageList = [];
    wikiService.getFeed(function (data) {
        $scope.pageList = $scope.pageList.concat(data);
    });

    $scope.showFullSummary = {};
    $scope.MediaBodyClicked = function ($index, $event) {
        $scope.showFullSummary[$index] = typeof ($scope.showFullSummary[$index]) != undefined ? !$scope.showFullSummary[$index] : true;
        
    }
    $scope.LazyLoadInstance = new LazyLoad();
 
    $scope.onBottomReached = function (callback) {
        wikiService.getFeed(function (data) {        
            $scope.pageList = $scope.pageList.concat(data)
            callback();
        });
    }
}])