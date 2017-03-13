app.directive('validfile', function validFile() {

    var validFormats = ['jpg', 'pdf'];
    return {
        require: 'ngModel',
        link: function (scope, elem, attrs, ngModel) {
 
            ngModel.$validators.validFile = function (modelValue , viewValue) {
                console.log("validatin", modelValue , viewValue)

                var formats = attrs.formats || validFormats;
                var value = elem.val(),
                    ext = value.substring(value.lastIndexOf('.') + 1).toLowerCase();
                return formats.indexOf(ext) !== -1;
              
            };

            elem.on('change', function (event) {
                var files = event.target.files;
                if (!angular.isDefined(attrs.multiple)) {
                    files = files[0];
                } else {
                    files = Array.prototype.slice.apply(files);
                }
                ngModel.$setViewValue(files, event);

            });
        }
    };
});