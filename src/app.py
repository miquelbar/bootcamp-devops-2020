import os
from bottle import route, run, template, view, static_file

ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
DEBUG = True if os.getenv('DEBUG', 'False').lower() == 'true' else False
RELOADER = True if os.getenv('RELOADER', 'False').lower() == 'true' else False


@route('/hello/static/<filename:path>')
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
@view('home')
def index():
    return dict(environment=ENVIRONMENT)

@route('/hello')
@route('/hello/<name>')
@view('hello')
def hello(name='World'):
    return dict(name=name, environment=ENVIRONMENT)



run(host='0.0.0.0', port=8080, debug=DEBUG, reloader=RELOADER)