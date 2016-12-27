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
        json_dict = request.get_json()
        name = json_dict['name']
        t_z = json_dict['t_z']
        class_ = json_dict['class']
        birthday = json_dict['birthday']
        return jsonify(temp_school_db_module.add_stu(name, t_z, birthday, class_))


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


@app.route('/students/<int:stu_id>/<year>/', methods=['GET'])
def get_subjects_by_year(stu_id, year):
    #   מחזיר רשימת מקצועות והID שלהם לאותה שנה
    # year = temp_school_db_module.check_year(year)
    fetch = temp_school_db_module.subject_per_year(stu_id, year)
    return jsonify(fetch)


# @app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
# def get_avg_by_subject(stu_id, year):
#     # מחזיר רשימת מקצועות שאותו תלמיד למד
#     pass


@app.route('/students/<int:stu_id>/<year>/<int:sub_id>/', methods=['GET', 'POST'])
def get_test(stu_id, year, sub_id):
    #  מחזיר רשימת מבחנים
    if request.method == 'GET':
        return jsonify(temp_school_db_module.stu_subject(stu_id, sub_id, year))
    # מוסיף מבחן
    if request.method == 'POST':
        fech = request.get_json()
        day = fech['day']
        return jsonify(temp_school_db_module.insert_test(sub_id, year, day))


@app.route('/students/<int:stu_id>/<int:year>/all_sub_avg/', methods=['GET'])
def get_avg_of_year(stu_id, year):
    # ממוצע כללי של כל המקצועות
    return jsonify(temp_school_db_module.avg_all_grade(stu_id, year))

#
# @app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/avg/', methods=['GET'])
# def get_avg_by_sub(stu_id, year, sub_id):
#     # מחזיר ממוצע לפי מקצוע
#     return jsonify(temp_school_db_module.avg_stu_sub(sub_id, year, stu_id))


# @app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/', methods=['GET'])
# def stu_by_year_sub_test(stu_id, year, sub_id):
#     # מחזיר רשימת מבחנים של אותו מקצוע
#     return jsonify(temp_school_db_module.stu_subject(stu_id, year, sub_id))


# @app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['GET'])
# def stu_by_year_sub_test(stu_id, year, sub_id, test_id):
#     # מחזיר מבחן ספציפי
#     return jsonify(temp_school_db_module.specific_test_grade(test_id, stu_id))


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/<int:test_id>/', methods=['GET','PUT', 'POST'])
def updte_by_test_id(stu_id, year, sub_id, test_id):
    # מעדכן מבחן ספציפי
    if request.method == 'PUT':
        new_grade = request.get_json()['grade']
        return jsonify(temp_school_db_module.update_grade(test_id, stu_id, new_grade))
    #     מוסיף שורה לטבלת ציונים
    if request.method == 'POST':
        fech = request.get_json()
        class_ = fech['class']
        grade = fech['grade']
        return jsonify(temp_school_db_module.insert_student_grade(stu_id, sub_id, year, grade, class_, test_id))
    if request.method == 'GET':
        # מחזיר מבחן ספציפי
        return jsonify(
            temp_school_db_module.specific_test_grade(test_id, stu_id))


@app.route('/students/<int:stu_id>/<int:year>/<int:sub_id>/avg/', methods=['GET'])
def stu_by_year_sub_test(stu_id, year, sub_id):
    # מחזיר ממוצע של מקצוע מסויים
    return jsonify(temp_school_db_module.avg_stu_sub(sub_id, year, stu_id))


@app.route('/students/<int:stu_id>/<ray_of_years>/', methods=['GET'])
def get_all_subjects_of_stu(stu_id):
    # מחזיר רשימת מקצועות וה ID שלהם לפי רישמת השנים בצורה כזאת: 2016,2015,2014
    pass


@app.route('/students/<int:stu_id>/all_years/', methods=['GET'])
def get_all_subjects(stu_id):
    #  צריך לתת פונקציה לקבלת כל המקצועות שאי פעם למד אותו תלמיד בלי פרמטרים לשנה מסויימת
    return jsonify(temp_school_db_module.all_years_stu(stu_id))


@app.route('/students/<int:stu_id>/all_years/all_subs/', methods=['GET'])
def get_all_subs_avg(stu_id):
    # מחזיר ממוצע של כל המקצועות
    return jsonify(temp_school_db_module.avg_all_avg_all_years(stu_id))


@app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['GET', 'POST'])
def subject_by_stu_all_years(stu_id, sub_id):
    #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
    if request.methods == 'GET':
        return jsonify(temp_school_db_module.avg_stu_sub_all_years(sub_id, stu_id))
    # ?
    # if request.methods == 'POST':
    #     pass


@app.route('/students/<int:stu_id>/<specific_years>/avg/', methods=['GET'])
def get_avg_of_years(stu_id, specific_years):
    return jsonify(temp_school_db_module.avg_all_grade_few_years(stu_id, specific_years))


# @app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['POST'])
# def post_test_by_sub(stu_id, sub_id):
#     #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
#     pass

#
# @app.route('/students/<int:stu_id>/all_years/<int:sub_id>/', methods=['PUT'])
# def update_stu_by_sub(stu_id, sub_id):
#     #  מחזיר את הממוצע של מקצוע מסויים לאורך כל השנים
#     pass


@app.route('/teachers/')
def teacher():
    pass


if __name__ == '__main__':
    app.run(debug=True)