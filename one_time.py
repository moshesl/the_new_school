import sqlite3


def __string_to_create_tables(table_name, column, *columns):
    name = 'CREATE TABLE IF NOT EXISTS {}'.format(table_name)
    c = '(' + '{}'.format(column)
    if columns:
        for i in columns:
            c += ', {}'.format(i)
    return name + c + ')'


def create_tables(table_name, column, *columns):
    con = sqlite3.connect('tables.db')
    con.execute(__string_to_create_tables(table_name, column, *columns))
    con.commit()


create_tables('tests', 'id INTEGER PRIMARY KEY', 'id_subject', 'year INTEGER(4)',
              'day DATE')
# create_tables('teacher', 'id INTEGER PRIMARY KEY', 'name CHAR(30)', 't_z  INTEGER(9)',
#               'email CHAR(40)', 'password INTEGER(8)')
# create_tables('subjects', 'id INTEGER PRIMARY KEY', 'subject CHAR(18)')
# create_tables('teacher_subject', 'id_teacher INTEGER(3)', 'class INTEGER(2)',
#               'id_subject INTEGER(2)')
# create_tables('students_grade', 'id_student INTEGER(4)', 'id_subject INTEGER(2)',
#               'grade INTEGER(2)', 'year INTEGER(4)', 'class INTEGER(2)')
#

# con =  sqlite3.connect('tables.db')
# con.execute('')
# con.commit()
