app.controller("WikipediaFeedController", ["$scope" ,"wikipediaService", "googleService" ,"displayService" , function ($scope , wikiService , googleService , displayService) {

    $scope.pageList = [];

    wikiService.getFeed(function (data) {
        data = data.map(function (d) {
            d["keypoints"] = d["keypoints"].map(function(kp){
                kp[0] = kp[0].replace(new RegExp("[ ]+") , " ");
                return kp;
            })
            
            return d;
        })
        $scope.pageList = $scope.pageList.concat(data);
    });

    $scope.showFullSummary = {};
    $scope.MediaBodyClicked = function ($index, $event) {
        $scope.showFullSummary[$index] = typeof ($scope.showFullSummary[$index]) != undefined ? !$scope.showFullSummary[$index] : true;
        
    }
   
 
    $scope.onBottomReached = function (callback) {
        wikiService.getFeed(function (data) {        
            $scope.pageList = $scope.pageList.concat(data)
            callback();
        });
    }

  

    $scope.showGoogleModal = function (query) {
        console.log("load", query, googleService.GetURLForQuery(query));
        displayService.ShowModalWithURL($scope, "GoogleModal" , googleService.GetURLForQuery(query));
    }
}])