
(function () {

    var oucfeed = {
        ajax: $.ajax,
        root: (function () {
            var scripts = document.getElementsByTagName('script')
            var src = scripts[scripts.length-1].src
            var lastSlash = src.lastIndexOf("/")
            var root = lastSlash == -1 ? "" : src.slice(0, lastSlash+1)
            return root
        })(),
        postJSON: function (url, data, success) {
            url = this.root + url
            data = JSON.stringify(data)
            this.ajax({
                type: 'POST',
                url: url,
                data: data,
                success: success,
                dataType: 'json',
                contentType: 'application/json'
            })
        },
        postNews: function (news) {
            this.postJSON("news", news)
        }

    }

    window.oucfeed = oucfeed

})()
