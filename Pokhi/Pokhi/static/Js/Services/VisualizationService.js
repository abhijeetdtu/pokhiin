app.factory("visualizationService", ["$http" , function ($http) {

    var camelCaseToRegular = function (str) {
        console.log(str);
        return str.replace(/([A-Z])/g, ' $1')
                     .replace(/^./, function (str) { return str.toUpperCase(); })
    }
    var tryToConvert = function (string) {
        var regex = /^(\d+.?\d*)%?$/
        var r = regex.exec(string);
        if (r)
            return parseFloat(r[1]);
        else
            return string
    }

    var getResource = function (callback) {
        $http({
            url: "https://data.gov.in/api/datastore/resource.json?resource_id=e48df1f8-9dc5-4bd1-a59c-ccd7b9314373&api-key=54f6530135d98e6597e84b5f4009de12"
            ,methods : "GET"
        }).success(function (data) {
            var returnData = {};
            var row = {};
            returnData.records = [];
            var keys =  Object.keys(data.fields);
            returnData.fields = Object.keys(data.fields).map(function (d) {
                return camelCaseToRegular(d);
            });
            
            for (var i = 0; i < data.records.length ; i++) {
                row = {};
                for (var j = 0; j < returnData.fields.length ; j++) {
                    row[returnData.fields[j]] = tryToConvert(data.records[i][keys[j]])
                }
                returnData.records.push(row);
            }
            
            console.log(returnData)
            callback(returnData);
        })
    }

    return {

        GetResource: getResource
    }
}])