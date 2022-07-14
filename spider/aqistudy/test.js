var debugflag = false;
  document.onkeydown = function() {
    if ((e.ctrlKey) && (e.keyCode == 83)) {
      alert("检测到非法调试，CTRL + S被管理员禁用");
      return false;
    }
  }
  document.onkeydown = function() {
    var e = window.event || arguments[0];
    if (e.keyCode == 123) {
      alert("检测到非法调试，F12被管理员禁用");
      return false;
    }
  }
  document.oncontextmenu = function() {
    alert('检测到非法调试，右键被管理员禁用');
    return false;
  }
  !function () {
    const handler = setInterval(() => {
      if (window.outerWidth - window.innerWidth > 230 ||
       window.outerHeight - window.innerHeight > 230) {
        // document.write((window.outerWidth - window.innerWidth) + ',' + (window.outerHeight - window.innerHeight));
        document.write('检测到非法调试, 请关闭调试终端后刷新本页面重试!<br/>');
        document.write("Welcome for People, Not Welcome for Machine!<br/>");
        debugflag = true;
      }
      const before = new Date();
      (function() {}
        ["constructor"]("debugger")())
      const after = new Date();
      const cost = after.getTime() - before.getTime();
      if (cost > 50) {
        debugflag = true;
        document.write('检测到非法调试, 请关闭调试终端后刷新本页面重试!<br/>');
        document.write("Welcome for People, Not Welcome for Machine!<br/>");
      }

    }, 2000)
  }();