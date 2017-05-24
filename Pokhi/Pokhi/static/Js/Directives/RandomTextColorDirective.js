app.directive("randomTextColor", [function () {

    return {
        restrict:'A',
        link: function (scope, element, attrs, ctrl) {
            
            scope.getRandomColor = function () {
                return "rgb(" + Math.floor(Math.random() * 125) + "," + Math.floor(Math.random() * 125) + "," + Math.floor(Math.random() * 125) + ")";
            }

            $(element[0]).css("color", function () {
                return scope.getRandomColor();
            });

            $(element[0]).css("font-weight","bold");
        }
    }
}])