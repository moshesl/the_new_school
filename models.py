from app import db


class BlogPost(db.Model):

    __tablename__ = "posts"


    id = db.Coulmn(db.Integer, primary_key=True)
    title = db.Coulmn(db.String, primary_key=False)
    description = db.Coulmn(db.String, primary_key=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title = {} description = {}'.format(self.title, self.
                                                     description)

