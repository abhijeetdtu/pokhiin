app.directive('loader', function () {
    return {
        scope:{
            show : '='
        },
        template: function (element, attrs) {
            var display = (attrs.show == 'true')? 'display:block;':'display:none;';
                
            return ['<div id="loader" style="position:absolute;height:100%;width:100%;'+display+'" >',
                    '<div class="loader" style="position:absolute;left:45%;top:35%;"></div>',
                '</div>'].join("");
        }
    }
  });