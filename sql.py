import sqlite3
with sqlite3.connect("sample.db") as con:
    c = con.cursor()
    c.execute('drop table posts')
    c.execute("""create table posts(title text , description text)""")
    c.execute('insert into posts values("good" , "im good.")')
    c.execute('insert into posts values("fine", "im ok.")')
    c.execute('insert into posts values("bad", "im fine.")')