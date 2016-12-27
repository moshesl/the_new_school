import sqlite3

con = sqlite3.connect('tables.db3', isolation_level=None, check_same_thread=False)
con.row_factory = sqlite3.Row


class Student:
    def __init__(self, name, m_z, birthday, class_stu=1):
        self._name = None
        self.name = name
        self._m_z = None
        self.m_z = m_z
        self._birthday = None
        self.birthday = birthday
        self._class_stu = None
        self.class_stu = class_stu

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_stu):
        if type(name_stu) is str:
            self._name = name_stu
        else:
            raise ValueError

    @property
    def m_z(self):
        return self._m_z

    @m_z.setter
    def m_z(self, t_z):
        test = con.execute('SELECT * FROM students WHERE t_z = ?', (t_z,)).fetchone()
        if type(t_z) is int and len(str(t_z)) < 10 and test == None:
            self._m_z = t_z
        else:
            raise ValueError

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birth):
        if type(birth) is str and len(birth) <= 10:
            self._birthday = birth
        else:
            raise ValueError

    @property
    def class_stu(self):
        return self._class_stu

    @class_stu.setter
    def class_stu(self, class_s=1):
        if type(class_s) is int and 0 < class_s < 13:
            self._class_stu = class_s
        else:
            raise ValueError


# def check_year(inp):
#     if inp is int:
#         return int(inp)
#     if inp.isalpha():
#         return str(inp)
#     else:
#         f, l = inp.split("-")


# מסירה תלמיד מבית הספר ע"ע הקר
def remove_stu(num):
    stu_delete = get_stu(num)
    con.execute('DELETE FROM students WHERE id = ?', (num,))
    return stu_delete


# מעדכנת פרטי תלמיד,מקבלת 1 אי די שלו ו2 טפל עם העמודות לעדכון והעדכונים גופא
def update_stu(num, changes):
    a = {'num': num}
    upde = 'UPDATE students SET id=id'
    if 'name' in changes:
        upde += ', name=:name'
        a['name'] = changes['name']
    if 't_z' in changes:
        upde += ', t_z=:t_z'
        a['t_z'] = changes['t_z']
    if 'birthday' in changes:
        upde += ', birthday=:birthday'
        a['birthday'] = changes['birthday']
    if 'class' in changes:
        upde += ', class=:class'
        a['class'] = changes['class']
    upde += ' WHERE id =:num'
    con.execute(upde, a)
    return get_stu(num)


# מחזיר את כל הפרטים עבור תלמיד מסוים לפי האי די שלו
def get_stu(num):
    sele = con.execute('SELECT * FROM students WHERE id = ?', (num,))
    sele = sele.fetchone()
    if sele:
        return dict(sele)
    else:
        raise ValueError('There is no such student')


# מוסיף תלמידים לבית הספר,בתנאים הנדרשים
def add_stu(name, m_z, birthday, class_stu=1):
    new_ob = Student(name, m_z, birthday, class_stu)
    stud = con.execute('INSERT INTO students(name,t_z,birthday,class)VALUES (?,?,?,?)',
                       (new_ob.name, new_ob.m_z, new_ob.birthday, new_ob.class_stu))
    idd = stud.lastrowid
    return get_stu(idd)


# מחזיר שמות אי די וכיתה של כל ההתלמידים
def get_all_stu():
    l = []
    for stu in con.execute('SELECT id,name,class FROM students'):
        stu = dict(stu)
        l.append(stu)
    return l


# מחזיר רשימת שנים בהם למד התלמיד בבית הספר
def get_students_year(id_stu):
    sele = con.execute("""SELECT year FROM students_grade WHERE id_student = ?""",
                       (id_stu,)).fetchall()
    return list(set([i[0] for i in sele]))


# מחזיר רשימת מקצועות שלמד התלמיד בשנה זו
def subject_per_year(id_stu, year):
    sele = con.execute("""SELECT subject,id FROM subjects INNER JOIN
                        students_grade ON id_subject = subjects.id WHERE
                        id_student = ? AND year = ?""", (id_stu, year)).fetchall()
    if sele:
        return dict(sele)
    raise ValueError('No record for student:{} in year:{}'.format(id_stu, year))


# ממוצע ציונים של תלמיד פלוני בשנה אלמונית
def avg_all_grade(id_stu, year):
    sele = con.execute("""SELECT AVG(grade) FROM students_grade WHERE id_student = ? AND year = ? """
                , (id_stu, year)).fetchone()[0]
    return round(sele, 2)


# מקבלת 3 דברים ומחזרת טפלים של אי די של המבחן עם היום ןהשעה המדוייק שבו נעשה
def stu_subject(id_stu, id_sub, year):
    sele = con.execute("""SELECT tests.id,day FROM tests INNER JOIN
                          students_grade ON id = id_test WHERE
                         id_student = ? AND  tests.id_subject = ? AND tests.year = ?""",
                       (id_stu, id_sub, year)).fetchall()
    return dict(sele)


# הןספת מבחן לטבלה.מקבל אי די של מקצוע,שנה,ותאריך
def insert_test(id_sub, year, d):
    con.execute('INSERT INTO tests (id_subject,year,day) VALUES (?,?,?)', (id_sub, year, d))
    return tuple(con.execute('SELECT * FROM tests WHERE id_subject = ? AND year = ? AND day = ?',
                             (id_sub, year, d)).fetchone())


# ממוצע של מקצוע מסויים עבור תלמיד y בשנת x
def avg_stu_sub(id_sub, year, id_stu):
    dic = con.execute(
        'SELECT AVG(grade) FROM students_grade WHERE id_student = ? AND id_subject = ? AND year = ?',
        (id_stu, id_sub, year))
    return dic.fetchone()[0]


# מקבל id מבחן וid תלמיד ומחזיר את הציון עבור אותו מבחן מסוים
def specific_test_grade(id_test, id_stu):
    dic = con.execute('SELECT grade FROM students_grade WHERE id_test = ? AND id_student = ?',
                      (id_test, id_stu))
    return dic.fetchone()[0]


#עדכון ציון
def update_grade(id_test, id_stu,new_grade):
    con.execute('UPDATE students_grade SET grade = ? WHERE id_test = ? AND id_student = ?',(new_grade,id_test,id_stu))
    return specific_test_grade(id_test,id_stu)


#הוספת שורה לטבלת הציונים
def insert_student_grade(id_stu,id_sub,year,grade,c,id_test):
    con.execute("INSERT INTO students_grade VALUES (?,?,?,?,?,?)",(id_stu, id_sub, year, grade, c, id_test))
    return specific_test_grade(id_test,id_stu)


# כל המקצועות שלמד פלוני בכל שנותיו
def all_years_stu(id_stu):
    sele = con.execute("""SELECT subject FROM subjects INNER JOIN
                            students_grade ON id_subject = subjects.id WHERE
                            id_student = ?""", (id_stu,)).fetchall()
    if sele:
        return list(set([i[0] for i in sele]))
    raise ValueError('No record for student:{}'.format(id_stu))


# ממוצע כל ציוני אלמוני בכל שנותיו
def avg_all_avg_all_years(id_stu):
    sele = con.execute(
        """SELECT AVG(grade) FROM students_grade WHERE id_student = ? """
        , (id_stu,)).fetchone()[0]
    return round(sele, 2)


# ממוצע תלמיד במקצוע מסוים בכל שנותיו
def avg_stu_sub_all_years(id_sub, id_stu):
    dic = con.execute(
        'SELECT AVG(grade) FROM students_grade WHERE id_student = ? AND id_subject = ?',
        (id_stu, id_sub,))
    return round(dic.fetchone()[0], 2)


def subject_per_years(id_stu, years):
    sele = con.execute("""SELECT subject,year FROM subjects INNER JOIN
                        students_grade ON id_subject = subjects.id WHERE
                        id_student = ? AND year = ?""", (id_stu, years)).fetchall()
    if sele:
        return dict(sele)
    raise ValueError('No record for student:{} in year:{}'.format(id_stu, years))


def avg_all_grade_few_years(id_stu, years):
    a_g = 0
    counter = 0
    for year in years:
        counter += 1
        a_g += avg_all_grade(id_stu, year)
    return a_g/counter,2
    # lst = []
#     for i in years:
#         sele = con.execute(
#             """SELECT grade FROM students_grade WHERE id_student = ? AND year = ? """
#             , (id_stu, i)).fetchall()
#         for j in sele:
#             lst.append(tuple(j)[0])
#     return round(sum(lst)/len(lst),2)

def stu_subject_few_years(id_stu, id_sub, years):
    lst = []
    for i in years:
        sele = con.execute("""SELECT tests.id,day FROM tests INNER JOIN
                              students_grade ON id = id_test WHERE
                             id_student = ? AND  tests.id_subject = ? AND tests.year = ?""",
                           (id_stu, id_sub, i)).fetchall()
        for i in sele:
            lst.append(dict(i))
    return lst


# print(stu_subject(1,2,2009))
# print(subject_per_years(1,(2015, 2016)))
# print(avg_all_grade_few_years(1,(2015, 2016)))
