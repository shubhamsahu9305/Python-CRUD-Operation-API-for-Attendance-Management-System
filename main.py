# Imported Flask Object
from app import app
# Imported Flask-MySql Object
from config import mysql
# Request & Jsonify is imported to input data and JSON conversion respectively
from flask import request, jsonify
# To create log file
import logging
# To limit size of logfile
from logging.handlers import RotatingFileHandler

# log file format initialization
logging.basicConfig(
    handlers=[
        RotatingFileHandler('C:/Users/shubham.sahu/PycharmProjects/PythonAssignment/log/logfile.log', maxBytes=1000000,
                            backupCount=5)],
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%d-%m-%YT%H:%M:%S')


# Endpoint for create operation on users table
@app.route('/api/create_users', methods=['POST'])
def create_users():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of users table in JSON format
        json = request.json
        user_type = json['user_type']
        full_name = json['full_name']
        username = json['username']
        email = json['email']
        user_password = json['user_password']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if user_type and full_name and username and email and user_password and submitted_by \
                and request.method == 'POST':
            # Sql query for create operation
            sqlQuery = "INSERT INTO users(user_type, full_name, username, email, user_password, submitted_by)" \
                       " VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (user_type, full_name, username, email, user_password, submitted_by)
            # Executed sql query to add elements to users table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Data added to users table successfully')
            response.status_code = 200
            logging.info('Data added to users table successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for create operation on courses table
@app.route('/api/create_courses', methods=['POST'])
def create_courses():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of courses table in JSON format
        json = request.json
        course_name = json['course_name']
        department_id = json['department_id']
        semester = json['semester']
        student_class = json['class']
        lecture_hours = json['lecture_hours']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if course_name and department_id and semester and student_class and lecture_hours and submitted_by \
                and request.method == 'POST':
            # Sql query for create operation
            sqlQuery = "INSERT INTO courses(course_name, department_id, semester, class, lecture_hours, submitted_by)" \
                       " VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (course_name, department_id, semester, student_class, lecture_hours, submitted_by)
            # Executed sql query to add elements to courses table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Data added to courses table successfully')
            response.status_code = 200
            logging.info('Data added to courses table successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for create operation on attendance_log table
@app.route('/api/create_attendance_log', methods=['POST'])
def create_attendance_log():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of attendance_log table in JSON format
        json = request.json
        student_id = json['student_id']
        course_id = json['course_id']
        present = json['present']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if student_id and course_id and submitted_by \
                and request.method == 'POST':
            # Sql query for create operation
            sqlQuery = "INSERT INTO attendance_log(student_id, course_id, present, submitted_by)" \
                       " VALUES(%s, %s, %s, %s)"
            bindData = (student_id, course_id, present, submitted_by)
            # Executed sql query to add elements to attendance_log table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Data added to attendance_log table successfully')
            response.status_code = 200
            logging.info('Data added to attendance_log table successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for create operation on departments table
@app.route('/api/create_departments', methods=['POST'])
def create_departments():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of departments table in JSON format
        json = request.json
        id = json['id']
        department_name = json['department_name']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if department_name and submitted_by and id \
                and request.method == 'POST':
            # Sql query for create operation
            sqlQuery = "INSERT INTO departments(id, department_name, submitted_by)" \
                       " VALUES(%s, %s, %s)"
            bindData = (id, department_name, submitted_by)
            # Executed sql query to add elements to departments table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Data added to departments table successfully')
            response.status_code = 200
            logging.info('Data added to departments table successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for create operation on students table
@app.route('/api/create_students', methods=['POST'])
def create_students():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of students table in JSON format
        json = request.json
        id = json['id']
        full_name = json['full_name']
        department_id = json['department_id']
        student_class = json['class']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if full_name and department_id and student_class and id and submitted_by \
                and request.method == 'POST':
            # Sql query for create operation
            sqlQuery = "INSERT INTO students(id, full_name, department_id, class, submitted_by)" \
                       " VALUES(%s, %s, %s, %s, %s)"
            bindData = (id, full_name, department_id, student_class, submitted_by)
            # Executed sql query to add elements to students table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Data added to students table successfully')
            response.status_code = 200
            logging.info('Data added to students table successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation on users table
@app.route('/api/read_users')
def read_users_detail():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read all the data from users table
        cursor.execute("SELECT * FROM users")
        # cursor object will fetch all the rows from the sql query
        usersRows = cursor.fetchall()
        # Response returned to the user in JSON format
        response = jsonify(usersRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation on courses table
@app.route('/api/read_courses')
def read_courses_detail():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read all the data from courses table
        cursor.execute("SELECT * FROM courses")
        # cursor object will fetch all the rows from the sql query
        coursesRows = cursor.fetchall()
        # Response returned to the user in JSON format
        response = jsonify(coursesRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation on attendance_log table
@app.route('/api/read_attendance_log')
def read_attendance_log_detail():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read all the data from courses table
        cursor.execute("SELECT * FROM attendance_log")
        # cursor object will fetch all the rows from the sql query
        attendancelogRows = cursor.fetchall()
        # Response returned to the user in JSON format
        response = jsonify(attendancelogRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation on departments table
@app.route('/api/read_departments')
def read_departments_detail():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read all the data from departments table
        cursor.execute("SELECT * FROM departments")
        # cursor object will fetch all the rows from the sql query
        departmentsRows = cursor.fetchall()
        # Response returned to the user in JSON format
        response = jsonify(departmentsRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation on students table
@app.route('/api/read_students')
def read_students_detail():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read all the data from departments table
        cursor.execute("SELECT * FROM students")
        # cursor object will fetch all the rows from the sql query
        studentsRows = cursor.fetchall()
        # Response returned to the user in JSON format
        response = jsonify(studentsRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation w.r.t id on users table
@app.route('/api/read_users/<int:id>')
def read_users(id):
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read the data from users table w.r.t id
        cursor.execute("SELECT * FROM users WHERE id =%s", id)
        # cursor object will fetch the single row
        usersRows = cursor.fetchone()
        # Response returned to the user in JSON format
        response = jsonify(usersRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation w.r.t id on courses table
@app.route('/api/read_courses/<int:id>')
def read_courses(id):
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read the data from courses table w.r.t id
        cursor.execute("SELECT * FROM courses WHERE id =%s", id)
        # cursor object will fetch the single row
        coursesRows = cursor.fetchone()
        # Response returned to the user in JSON format
        response = jsonify(coursesRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation w.r.t id on attendance_log table
@app.route('/api/read_attendance_log/<int:id>')
def read_attendance_log(id):
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read the data from attendance_log table w.r.t id
        cursor.execute("SELECT * FROM attendance_log WHERE id =%s", id)
        # cursor object will fetch the single row
        attendancelogRows = cursor.fetchone()
        # Response returned to the user in JSON format
        response = jsonify(attendancelogRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation w.r.t id on departments table
@app.route('/api/read_departments/<int:id>')
def read_departments(id):
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read the data from departments table w.r.t id
        cursor.execute("SELECT * FROM departments WHERE id =%s", id)
        # cursor object will fetch the single row
        departmentsRows = cursor.fetchone()
        # Response returned to the user in JSON format
        response = jsonify(departmentsRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for read operation w.r.t id on departments table
@app.route('/api/read_students/<int:id>')
def read_students(id):
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Executed sql query to read the data from departments table w.r.t id
        cursor.execute("SELECT * FROM students WHERE id =%s", id)
        # cursor object will fetch the single row
        studentsRows = cursor.fetchone()
        # Response returned to the user in JSON format
        response = jsonify(studentsRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for update operation on users table
@app.route('/api/update_users', methods=['PUT'])
def update_users():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of users table in JSON format
        json = request.json
        id = json['id']
        user_type = json['user_type']
        full_name = json['full_name']
        username = json['username']
        email = json['email']
        user_password = json['user_password']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if user_type and full_name and username and email and id and user_password and submitted_by \
                and request.method == 'PUT':
            # Sql query for update operation
            sqlQuery = "UPDATE users SET user_type=%s, full_name=%s, username=%s, email=%s, " \
                       "user_password=%s, submitted_by=%s WHERE id=%s"
            bindData = (user_type, full_name, username, email, user_password, submitted_by, id,)
            # Executed sql query to update elements to users table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Users table updated successfully')
            response.status_code = 200
            logging.info('Users table updated successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for update operation on courses table
@app.route('/api/update_courses', methods=['PUT'])
def update_courses():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of courses table in JSON format
        json = request.json
        id = json['id']
        course_name = json['course_name']
        department_id = json['department_id']
        semester = json['semester']
        student_class = json['class']
        lecture_hours = json['lecture_hours']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if course_name and department_id and semester and student_class and lecture_hours and submitted_by \
                and id and request.method == 'PUT':
            # Sql query for update operation
            sqlQuery = "UPDATE courses SET course_name=%s, department_id=%s, semester=%s, class=%s, " \
                       "lecture_hours=%s, submitted_by=%s WHERE id=%s"
            bindData = (course_name, department_id, semester, student_class, lecture_hours, submitted_by, id,)
            # Executed sql query to update elements to courses table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Courses table updated successfully')
            response.status_code = 200
            logging.info('Courses table updated successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for update operation on attendance_log table
@app.route('/api/update_attendance_log', methods=['PUT'])
def update_attendance_log():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of attendance_log table in JSON format
        json = request.json
        id = json['id']
        student_id = json['student_id']
        course_id = json['course_id']
        present = json['present']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if student_id and course_id and submitted_by \
                and id and request.method == 'PUT':
            # Sql query for update operation
            sqlQuery = "UPDATE attendance_log SET student_id=%s, course_id=%s, present=%s, " \
                       "submitted_by=%s WHERE id=%s"
            bindData = (student_id, course_id, present, submitted_by, id,)
            # Executed sql query to update elements to attendance_log table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Attendance_log table updated successfully')
            response.status_code = 200
            logging.info('Attendance_log table updated successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for update operation on departments table
@app.route('/api/update_departments', methods=['PUT'])
def update_departments():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of departments table in JSON format
        json = request.json
        id = json['id']
        department_name = json['department_name']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if department_name and submitted_by \
                and id and request.method == 'PUT':
            # Sql query for update operation
            sqlQuery = "UPDATE departments SET department_name=%s, submitted_by=%s WHERE id=%s"
            bindData = (department_name, submitted_by, id,)
            # Executed sql query to update elements to departments table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Departments table updated successfully')
            response.status_code = 200
            logging.info('Departments table updated successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Endpoint for update operation on students table
@app.route('/api/update_students', methods=['PUT'])
def update_students():
    # Connection established with mysql server
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        # Input elements of students table in JSON format
        json = request.json
        id = json['id']
        full_name = json['full_name']
        department_id = json['department_id']
        student_class = json['class']
        submitted_by = json['submitted_by']
        # Checking Null condition from JSON input and requested method in API
        if full_name and department_id and student_class and submitted_by \
                and id and request.method == 'PUT':
            # Sql query for update operation
            sqlQuery = "UPDATE students SET full_name=%s, department_id=%s, class=%s, " \
                       "submitted_by=%s WHERE id=%s"
            bindData = (full_name, department_id, student_class, submitted_by, id,)
            # Executed sql query to update elements to students table
            cursor.execute(sqlQuery, bindData)
            # Committed the transaction otherwise data will not save to server when session ends
            conn.commit()
            # Response returned after successful completion of transaction
            response = jsonify('Students table updated successfully')
            response.status_code = 200
            logging.info('Students table updated successfully')
            return response
        else:
            # Show Error message if record found missing
            return showMessage()
    except Exception as e:
        print(e)
        logging.error(e)
    finally:
        # MySql server connection closed
        cursor.close()
        conn.close()


# Decorator function for 404 error
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    logging.error(message)
    return response


if __name__ == "__main__":
    app.run()
