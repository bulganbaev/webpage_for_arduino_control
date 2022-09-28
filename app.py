from bottle import route, run

@route('/')
def hello():
    return "Hello World!"

@route('/login')
def login():
    return '<h1> On the login page</h1>'

@route('/register')
def register():
    return '<h1> On the register page</h1>'

if __name__ == '__main__':
    run(host='172.31.17.112', port=8080, debug=True, reloader= True)