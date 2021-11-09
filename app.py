import time
from flask_limiter import Limiter
from flask_accept import accept
from flask_limiter.util import get_remote_address
from flask import Flask, render_template

app = Flask(__name__)
ip_list = []

# define visit rate for entire app
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10/minute"]
)

# get visitor ip and append it to global list
def register_ip():
    global ip_address
    ip_address = get_remote_address()
    timestamp = time.time()
    ip_list.append([timestamp, ip_address])

# main site with visitor ip information
@app.route('/')
@accept('text/html')
def index():
    register_ip()
    return render_template("main.html", visitor_ip = ip_address), 200, {'Content-Type': 'text/html; charset=utf-8'}

@index.support('text/plain')
def index_txt():
    register_ip()
    return render_template("main.txt", visitor_ip = ip_address), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@index.support('text/xml')
def index_xml():
    register_ip()
    return render_template("main.xml", visitor_ip = ip_address), 200, {'Content-Type': 'text/xml; charset=utf-8'}

@index.support('text/yaml')
def index_yaml():
    register_ip()
    return render_template("main.yaml", visitor_ip = ip_address), 200, {'Content-Type': 'text/yaml; charset=utf-8'}

# secondary site with list containing all visitorss' ip
@app.route('/history')
@accept('text/html')
def history():
    return render_template("history.html", data=ip_list), 200, {'Content-Type': 'text/html; charset=utf-8'}

@history.support('text/plain')
def history_txt():
    return render_template("history.txt", data=ip_list), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@history.support('text/xml')
def history_xml():
    return render_template("history.xml", data=ip_list), 200, {'Content-Type': 'text/xml; charset=utf-8'}

@history.support('text/yaml')
def history_yaml():
    return render_template("history.yaml", data=ip_list), 200, {'Content-Type': 'text/yaml; charset=utf-8'}

# use filter to convert timestamp into readable date
@app.template_filter('ctime')
def timectime(x):
    return time.ctime(x)

#bind the server to host ip
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)