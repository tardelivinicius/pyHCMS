from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '030595'
app.config['MYSQL_DB'] = 'davidaulas'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '127.0.0.1'
app.config['MYSQL_CONNECT_TIMEOUT'] = 3000
app.config['MYSQL_READ_DEFAULT_FILE'] = ''
app.config['MYSQL_USE_UNICODE'] = True
app.config['MYSQL_CHARSET'] = ''
app.config['MYSQL_SQL_MODE'] = None
app.config['MYSQL_CURSORCLASS'] = None

from cms.login.routes import mod
from cms.register.routes import mod

app.register_blueprint(login.routes.mod)
app.register_blueprint(register.routes.mod, url_prefix='/register')