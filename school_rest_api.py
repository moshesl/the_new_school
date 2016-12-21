import json
import temp_school_db_module
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'password'


@app.route('/')
def welcome_message():
    return jsonify('Welcome: Welcome to our school')


# @app.route('/?username', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def login():
#     username = request.args.get('username')
#     password = request.args.get('password')


@app.route('/students/',methods=['GET', 'POST'])
def students():
    # מחזיר שמות כל התלמידים id וכיתה
    if request.method == 'GET':
        lst = temp_school_db_module.get_all_stu()
        return jsonify(lst)
    # מוסיף תלמיד למערכת
    if request.method == 'POST':
        json_dict = json.loads(request.form)
        name = json_dict['name']
        t_z = json_dict['t_z']
        class_ = json_dict['class']
        birthday = json_dict['birthday']
        return temp_school_db_module.add_stu(*(name, t_z, class_, birthday))


@app.route('/students/<int:stu_id>/',methods=['GET', 'DELETE'])
def student(stu_id):
    #     מחזיר את רשימת שנות לימודיו של אותו תלמיד
    if request.method == 'GET':
        lst = temp_school_db_module.get_students_year(stu_id)
        return jsonify(lst)
    # מסיר תלמיד
    if request.method == 'DELETE':
        return jsonify(temp_school_db_module.remove_stu(stu_id))


@app.route('/students/<int:stu_id>/', methods=['PUT'])
def update_student(stu_id):
    #     מעדכן את נתוניו של תלמיד מסויים
    json_dict = request.get_json()
    temp_school_db_module.update_stu(stu_id, json_dict)
    return jsonify('updated!')


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subjects_by_year(stu_id, year):
    #   מחזיר רשימת מקצועות והID שלהם לאותה שנה
    fetch = temp_school_db_module.subject_per_year(stu_id, year)
    return jsonify(fetch)


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/tests/', methods=['GET', 'POST'])
def get_test(stu_id, year, sub_id):
    #  מחזיר רשימת מבחנים
    if request.method == 'GET':
        return jsonify(temp_school_db_module.get_tests(stu_id, year, sub_id))
    # מוסיף מבחן
    if request.method == 'POST':
        tst_gr = request.form
        grade = tst_gr["grade"]
        class_ = tst_gr["class"]
        return temp_school_db_module.add_test(stu_id, sub_id, grade, year, class_)


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/avg/', methods=['GET'])
def get_avg(stu_id, year, sub_id):
    # ממוצע של תלמיד במקצוע מסויים
    return temp_school_db_module.get_avg(stu_id, year, sub_id)


@app.route('/students/<int:stu_id>/<int:year>/', methods=['GET'])
def get_subjects(stu_id, year):
    # מחזיר רשימת מקצועות שאותו תלמיד למד
    return jsonify(temp_school_db_module.subject_per_year(stu_id, year))


@app.route('/students/<int:stu_id>/<int:year>/all_sub_avg/', methods=['GET'])
def get_avg_of_year(stu_id, year):
    # ממוצע כללי של כל המקצועות
    return jsonify(temp_school_db_module.avg_all_grade(stu_id, year))


@app.route('/students/<int:stu_id>/<int:year>/tests/', methods=['GET'])
def get_subjects_tests(stu_id, year):
    # מחזיר רשימת מבחנים שאותו תלמיד נבחן
    return jsonify(temp_school_db_module.grade_per_year(stu_id, year))


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
def get_avg_by_sub(stu_id, year, sub_id):
    # מחזיר ממוצע לפי מקצוע
    return jsonify(temp_school_db_module.avg_sub(stu_id, year, sub_id))


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['GET'])
def stu_by_year_sub_test(stu_id, year, sub_id, test_id):
    # מחזיר מבחן ספציפי
    if request.methods == 'GET':
        return jsonify(temp_school_db_module.stu_by_year_sub_test(stu_id, year, sub_id, test_id))


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['PUT'])
def updte_by_test_id(stu_id, year, sub_id, test_id):
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