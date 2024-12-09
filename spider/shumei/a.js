function generateTimeFormat() {
    var e = new Date(), t = function (n) {
        return +n < 10 ? "0" + n : n.toString();
    };
    return ((e.getFullYear().toString() + t(e.getMonth() + 1)) + t(e.getDate()) + t(e.getHours()) + t(e.getMinutes())) + t(e.getSeconds());
}

function getCaptchaUuid() {
    var i = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    var n = "";
    var c = i.length;
    for (var r = 0; r < 18; r++) {
        n += i.charAt(Math.floor(Math.random() * c));
    }
    return generateTimeFormat() + n;
}WW