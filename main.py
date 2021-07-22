from flask import Flask, request, make_response, redirect

app = Flask (__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip2', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip2')
    return "Hello flaskd como cookie: {}".format(user_ip)