from flask import Flask, jsonify  # flask库
import time  # 时间模块

app = Flask(__name__)  # 创建一个服务，赋值给APP


# 定义的方法名必须和接口路径相同
# 由于路径是'/test'，所以方法名为test()
# 浏览器直接访问直接为'Get'方法
@app.route('/test', methods=['Get'])  # 指定接口访问的路径，支持什么请求方式get，post
def test():
    response_data = {
        "SystemTimeObject": {
            "VIIDServerID": "123",
            "TimeMode": "1",
            "LocalTime": time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())),
        }
    }
    return jsonify(response_data['SystemTimeObject'])


if __name__ == '__main__':
    # 这个host：windows就一个网卡，可以不写，而linux有多个网卡，写成0.0.0.0可以接受任意网卡信息
    # 端口号默认5000，可以手动设置，这里我设置成了8802
    app.run(host='127.0.0.1', port=8808, debug=True)
