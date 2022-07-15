// rpc使用的代码
!function () {
    // 防止重复创建websocket
    if (window.flagLX) {

    } else {
        window.weiboLX = makeRequest;
        var ws = new WebSocket("ws://127.0.0.1:9999");
        window.flagLX = true;
        ws.onopen = function (evt) {
        };
        ws.onmessage = function (evt) {
            var lx = evt.data;
            var result = lx.split(",");
            var res = window.weiboLX(result[0], result[1], 7, false);
            ws.send(JSON.stringify(res));
        }
    }
}();



//抖音东方甄选直播间实时数据推送
//https://live.douyin.com/80017709309

window.dataWs = s.toObject();
!function () {
    // 防止重复创建websocket
    var res = window.dataWs;
    if (window.flagLX) {
        window.wsDouying.send(JSON.stringify(res));
    } else {

        var ws = new WebSocket("ws://127.0.0.1:9876");
        window.flagLX = true;
        window.wsDouying = ws;
        ws.onopen = function (evt) {
        };
        ws.onmessage = function (evt) {
            ws.send(JSON.stringify(res));
        }
    }
}();