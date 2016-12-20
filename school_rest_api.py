import json
import school_module, temp_school_db_module
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'password'


@app.route('/')
def welcome_message():
    return jsonify('Welcome: Welcome to our school')


@app.route('/?username', methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')


@app.route('/students/',methods=['GET', 'POST'])
def all_the_students():
    # מחזיר שמות כל התלמידים ת"ז וכיתה
    if request.method == 'GET':
        lst = temp_school_db_module.get_all_stu()
        return jsonify(lst)
        # return jsonify(lst)
    # מוסיף תלמיד למערכת
    if request.method == 'POST':
        json_dict = json.loads(request.form)
        name = json_dict['name']
        t_z = json_dict['t_z']
        class_ = json_dict['class']
        birthday = json_dict['birthday']
        return school_module.add_student([name, t_z, class_, birthday])
    pass


# @app.route('/students/',methods=['POST'])
# def add_student(name, t_z, class_):
#     #     מוסיף תלמיד למסד נתונים ומחזיר את המילים WHELCOM
#     pass


@app.route('/students/<int:stu_id>/',methods=['GET', 'PUT'])
def get_student(stu_id):
    #     מחזיר את רשימת שנות לימודיו של אותו תלמיד
    if request.method == 'GET':
        lst = school_module.get_years_student(stu_id)
        return jsonify(lst)
    if request.method == 'PUT':
        pass
    pass


@app.route('/students/<int:stu_id>/', methods=['PUT'])
def update_student(stu_id):
    #     מעדכן את נתוניו של תלמיד מסויים
    pass


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subject(year):
    #   מחזיר רשימת מקצועות והID שלהם לאותה שנה
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_test():
    #  מחזיר רשימת מבחנים
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg(stu_id, year, sub_id):
    # ממוצע של תלמיד במקצוע מסויים
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['POST'])
def add_test(stu_id, year, sub_id):
    pass


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subjects(stu_id, year):
    # מחזיר רשימת מקצועות שאותו תלמיד למד
    pass


@app.route('/students/<int:stu_id>/<int:year>/all_sub_avg/', methods=['GET'])
def get_avg_of_year(stu_id, year):
    # ממוצע כללי של כל המקצועות
    pass


@app.route('/students/<int:stu_id>/<int:year>/tests/', methods=['GET'])
def get_subjects_tests(stu_id, year):
    # מחזיר רשימת מבחנים שאותו תלמיד נבחן
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg_by_sub(stu_id, year, sub_id):
    # מחזיר ממוצע לפי מקצוע
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['GET', 'POST'])
def stu_by_year_sub_test(stu_id, year, sub_id):
    # מחזיר מבחן ספציפי
    if request.methods == 'GET':
        pass
    if request.methods == 'POST':
        pass
    pass


# @app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=[])
# def post_test_by_sub(stu_id, year, sub_id, test_id):
#     # מוסיף מבחן ספציפי
#     pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['PUT'])
def get_subjects_test(stu_id, year, sub_id, test_id):
    # מעדכן מבחן ספציפי
    pass


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg_by_subject(stu_id, year):
    # מחזיר רשימת מקצועות שאותו תלמיד למד
    pass


@app.route('/students/<int:stu_id>/<ray_of_years>/', methods=['GET'])
def get_all_subjects_of_stu(stu_id):
    # מחזיר רשימת מקצועות וה ID שלהם לפי רישמת השנים בצורה כזאת: 2016,2015,2014
    pass


@app.route('/students/<int:stu_id>/all_years/', methods=['GET'])
def get_all_subjects(stu_id):
    #  צריך לתת פונקציה לקבלת כל המקצועות שאי פעם למד אותו תלמיד בלי פרמטרים לשנה מסויימת
    pass


@app.route('/students/<int:stu_id>/all_years/all_subs/', methods=['GET'])
def get_all_subs_avg(stu_id):
    # מחזיר ממוצע של כל המקצועות
    pass


@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['GET', 'POST'])
def subject_by_stu_all_years(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    if request.methods == 'GET':
        pass
    # ?
    if request.methods == 'POST':
        pass
    pass


@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['POST'])
def post_test_by_sub(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    pass

@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['PUT'])
def update_stu_by_sub(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    pass


@app.route('/teachers/')
def teacher():
    pass


if __name__ == '__main__':
    app.run(debug=True)