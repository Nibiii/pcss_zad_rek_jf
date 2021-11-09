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
@accept('text/html') # for clients requesting html content
def index():
    register_ip()
    return render_template("main.html", visitor_ip = ip_address), 200, {'Content-Type': 'text/html; charset=utf-8'} # return html file containing user IP

@index.support('text/plain') # for clients requesting txt content
def index_txt():
    register_ip()
    return render_template("main.txt", visitor_ip = ip_address), 200, {'Content-Type': 'text/plain; charset=utf-8'} # return txt file containing user IP

@index.support('text/xml') # for clients requesting xml content
def index_xml():
    register_ip()
    return render_template("main.xml", visitor_ip = ip_address), 200, {'Content-Type': 'text/xml; charset=utf-8'} # return xml file containing user IP

@index.support('text/yaml') # for clients requesting yaml content
def index_yaml():
    register_ip()
    return render_template("main.yaml", visitor_ip = ip_address), 200, {'Content-Type': 'text/yaml; charset=utf-8'} # return yaml file containing user IP

# secondary site with list containing all visitorss' ip
@app.route('/history')
@accept('text/html') # for clients requesting html content
def history():
    return render_template("history.html", data=ip_list), 200, {'Content-Type': 'text/html; charset=utf-8'} # return html file containing all previous IPs and it's request time

@history.support('text/plain') # for clients requesting txt content
def history_txt():
    return render_template("history.txt", data=ip_list), 200, {'Content-Type': 'text/plain; charset=utf-8'} # return txt file containing all previous IPs and it's request time

@history.support('text/xml') # for clients requesting xml content
def history_xml():
    return render_template("history.xml", data=ip_list), 200, {'Content-Type': 'text/xml; charset=utf-8'} # return xml file containing all previous IPs and it's request time

@history.support('text/yaml') # for clients requesting yaml content
def history_yaml():
    return render_template("history.yaml", data=ip_list), 200, {'Content-Type': 'text/yaml; charset=utf-8'} # return yaml file containing all previous IPs and it's request time

# use filter to convert timestamp into readable date
@app.template_filter('ctime')
def timectime(x):
    return time.ctime(x)

#bind the server to host ip
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)