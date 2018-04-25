from bottle import route, run

@route('/')
def index():
    return "hello"

run(host="localhost", port="9080", debug=True)
