collective_mobifyjs = {

    getMetaValue: function(attr) {
        var metas = document.getElementsByTagName('meta');

        for (i=0; i<metas.length; i++) {
           if (metas[i].getAttribute("property") == attr) {
              return metas[i].getAttribute("content");
           }
        }

        return null;
    },

    init: function() {
        var resize_url = this.getMetaValue('mobify:resize_url') ||  "//cdn.mobify.com/mobifyjs/build/mobify-2.0.5.min.js";
        var backend_url = this.getMetaValue('mobify:resize_backend');

        !function(a,b,c,d,e){function g(a,c,d,e){var f=b.getElementsByTagName("script")[0];a.src=e,a.id=c,a.setAttribute("class",d),f.parentNode.insertBefore(a,f)}a.Mobify={points:[+new Date]};var f=/((; )|#|&|^)mobify=(\d)/.exec(location.hash+"; "+b.cookie);if(f&&f[3]){if(!+f[3])return}else if(!c())return;b.write('<plaintext style="display:none">'),setTimeout(function(){var c=a.Mobify=a.Mobify||{};c.capturing=!0;var f=b.createElement("script"),h="mobify",i=function(){var c=new Date;c.setTime(c.getTime()+3e5),b.cookie="mobify=0; expires="+c.toGMTString()+"; path=/",a.location=a.location.href};f.onload=function(){if(e)if("string"==typeof e){var c=b.createElement("script");c.onerror=i,g(c,"main-executable",h,mainUrl)}else a.Mobify.mainExecutable=e.toString(),e()},f.onerror=i,g(f,"mobify-js",h,d)})}(window,document,function(){var a=/webkit|msie\s10|(firefox)[\/\s](\d+)|(opera)[\s\S]*version[\/\s](\d+)|3ds/i.exec(navigator.userAgent);return a?a[1]&&+a[2]<4?!1:a[3]&&+a[4]<11?!1:!0:!1},

        // path to mobify.js
        resize_url,

        // calls to APIs go here
        function() {
            var capturing = window.Mobify && window.Mobify.capturing || false;

            if (capturing) {
                Mobify.Capture.init(function(capture){

                if (backend_url != null) {
                    // Override getImageURL to use another backend
                    Mobify.ResizeImages.getImageURL = function(url, options) {
                        return backend_url + options.maxWidth + "/" + url
                    };
                }

                var capturedDoc = capture.capturedDoc;

                var images = capturedDoc.querySelectorAll("img, picture");
                Mobify.ResizeImages.resize(images);

                // Render source DOM to document
                capture.renderCapturedDoc();
            });
          }
        });
    }
}

collective_mobifyjs.init();
