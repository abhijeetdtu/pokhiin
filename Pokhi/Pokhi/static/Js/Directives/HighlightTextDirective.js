app.directive("highlightText", ["$compile" , function ($compile) {

    return {
        restrict: 'E',
        scope:{
            text: '='
            , highlight: '='
            ,createSummary:'='
        },
        template: "<div class='highlight-text-directiveClass'></div>",
        link :function(scope , element, attrs , ctrl){
            var elem = $(element[0]);

            if (scope.highlight === undefined || scope.highlight.length == 0) {
                elem.html(scope.text);
                return;
            }
                
            var lines = scope.text.split(".");
            var allHightlightedLines = [];

            for (var i = 0 ; i < lines.length ; i++) {
                var createdElem = $("<span></span>");
                var anchor = $("<a></a>");

                createdElem.html(lines[i] + ".");
                createdElem.append(anchor);

                for (var j = 0 ; j < scope.highlight.length ; j++) {
                    //console.log(lines[i], scope.highlight[j][0], lines[i].search(scope.highlight[j][0]));
                    if (lines[i].toLowerCase().search(scope.highlight[j][0].toLowerCase()) >= 0) {
                        anchor.attr("id", scope.highlight[j][0].replace(" " , "_"));
                        createdElem.addClass("highlighted-text");
                        allHightlightedLines.push(i);
                        break;
                    }

                }
                elem.append(createdElem);
            }
            
            if (scope.createSummary) {
                var summary = $("<div></div>").append($("<h3></h3>").html("Summary"));
                summary.addClass("summary-title list-group");

                for (var i = 0; i < allHightlightedLines.length ; i++) {
                    var line = $("<span></span>").html(lines[allHightlightedLines[i]]);
                    line.addClass("summary-point list-group-item");
                    summary.append(line);
                }
                  
                elem.prepend(summary);
            }
                
        }

    }
}]);