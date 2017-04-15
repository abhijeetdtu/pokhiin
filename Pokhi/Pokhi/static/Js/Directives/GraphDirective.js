app.directive("graph",["$timeout" ,  function ($timeout) {

    return {
        restrict:'E',
        scope:{
            key: '=',
            data:'='
        },
        template: function (element, attrs) { return '<div ng-include="\'/Views/Partials/GraphTemplate.html\'" onload="init()"></div>' },

        link: function ($scope, element, attrs, controller) {
            $scope.typesOfChart = ['line' , 'bar' , 'pie' ,'spline' , 'area']
            $scope.graphId = attrs.key + "-" + "graph";

            $scope.measureSelected = {};
            $scope.data = attrs.data;
            $scope.xAxisCategories = [];
            $scope.chartParams = {};
            $scope.chartParams.axis = {};
            $scope.chartType =  attrs.type || "line";

            $scope.collapseMeasurePanel = function () {
            }
            $scope.setAsXAxis = function (measure) {
                $scope.xAxisCategories = $scope.dataset.records.map(function (d) { return d[measure] });
                console.log($scope.xAxisCategories)
                $scope.generateChart();
            }
            $scope.measureSelect = function (measure) {
                $scope.measureSelected[measure] = !$scope.measureSelected[measure];
                $scope.generateChart();
            }
            $scope.chartTypeSelect = function (chartType) {
                $scope.chartType = chartType;
                $scope.generateChart();
            }
            $scope.$watch('data', function (newValue, oldValue) {
 
                if (newValue && newValue[0][0] != oldValue) {                   
                    $scope.dataset = newValue[0][0];
                    console.log($scope.dataset)
                }
            });
           
            $scope.generateChart = function () {
                var elemId = "#" + $scope.graphId;
                
                var measureList = Object.keys($scope.measureSelected).filter(function (d) { return $scope.measureSelected[d] == true; });
                var categories = $scope.xAxisCategories.length > 0 ? $scope.xAxisCategories : [];
                if (measureList.length == 0) return;

                $scope.chart = c3.generate({
                    bindto: elemId,
                    zoom: {
                        enabled: true
                    },
                    data: {
                        type: $scope.chartType,
                        json: $scope.dataset.records,
                        keys: {
                            //                x: 'name', // it's possible to specify 'x' when category axis
                            value: measureList
                        }
                    },
                    axis: {
                        x: {
                            type:'category',
                            categories: categories,
                            tick: {
                                rotate: 90,
                                multiline: false
                            },
                          }
                    }
                });
            }
        }
    }
}])