app.directive('loader', function () {
    return {
        scope:{
            show : '='
        },
        template: function (element, attrs) {
            var display = (attrs.show == 'true')? 'display:block;':'display:none;';
                
            return ['<div id="loader" class="loaderHolder" style="'+display+'" >',
                    '<div class="loader" style="position:absolute;left:45%;top:35%;"></div>',
                '</div>'].join("");
        }
    }
  });