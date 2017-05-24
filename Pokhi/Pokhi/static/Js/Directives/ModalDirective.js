app.directive('modal',["$http", function ($http) {
    return {
        restrict: 'E',
        template: function () { return "<div ng-include src=\"'Views/Partials/Modal.html'\"></div>" },
        scope: {
            id: "@key",
            title: "@",
            msg: "@",
            src:'@'
        },
        link: function (scope , element , attrs ,ctrl) {
            scope.alertClasses = {
                "Error": "alert alert-warning",
                "Success": "alert alert-success"
            };

            if (attrs.src) {
                $http({
                    url:src
                })
                .success(function (html) {
                    $(element[0]).find(".modal-content").html(html);
                })
            }
        }
      
    };
}]);
