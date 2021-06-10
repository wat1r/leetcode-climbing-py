from html import escape

from flask import Flask, request

app = Flask(__name__)


@app.route('/index')
def index():
    user = {'username': '阿飞'}
    html = '''
    <html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>

    '''
    return html


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"


#     如果当前使用了 GET 方法， Flask 会自动添加 HEAD 方法支持，并且同时还会 按照 HTTP RFC 来处理 HEAD 请求。同样， OPTIONS 也会自动实现。


"""
https://www.cnblogs.com/Zhengnengjin/p/Eternity_Znj.html
"""
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8990)

# 127.0.0.1 - - [10/Jun/2021 11:46:16] "GET /user/afei HTTP/1.1" 200 -
# 127.0.0.1 - - [10/Jun/2021 11:46:39] "GET /post/111 HTTP/1.1" 200 -
# 127.0.0.1 - - [10/Jun/2021 11:46:46] "GET /path/ll/ll HTTP/1.1" 200 -
