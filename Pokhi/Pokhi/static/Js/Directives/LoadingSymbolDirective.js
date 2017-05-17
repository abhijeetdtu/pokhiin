app.directive('loader', function () {
    return {
        scope:{
            show: '=',
            isGlobal : '&'
        },
        template: function (element, attrs) {
            var display = (attrs.show === 'true')? 'display:block;':'display:none;';
            var loaderHolderClass = attrs.isGlobal === 'true' ? "loaderHolder-global" : "loaderHolder-local";
        
            return ['<div id="loader" class="' + loaderHolderClass + '" style="' + display + '" >',
                    '<div class="loader" style="position:absolute;left:45%;top:35%;"></div>',
                '</div>'].join("");
        }
    }
  });