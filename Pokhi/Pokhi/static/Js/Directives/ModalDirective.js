app.directive('modal', function () {
    return {
        restrict: 'E',
        template: function () { return "<div ng-include src=\"'Views/Partials/Modal.html'\"></div>" },
        scope: {
            id: "@key",
            title: "@",
            msg: "@",
        },
        link: function (scope , element , attrs ,ctrl) {
            scope.alertClasses = {
                "Error": "alert alert-warning",
                "Success": "alert alert-success"
            };
        }
      
    };
});
