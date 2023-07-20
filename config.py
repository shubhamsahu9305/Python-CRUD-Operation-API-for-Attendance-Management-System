# Imported Flask object for app.py file
from app import app
# imported flaskext.mysql for MySql database connection
from flaskext.mysql import MySQL

# Created mysql object
mysql = MySQL()
# MySql configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'student_attendance_management'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
