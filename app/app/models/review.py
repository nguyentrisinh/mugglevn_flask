from . import db


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    what_user_like = db.Column(db.Text)
    what_user_dislike = db.Column(db.Text)
    rating = db.Column(db.Float)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    author = db.relationship('User', foreign_keys=author_id)
    company = db.relationship('Company', foreign_keys=company_id)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.title

    def init_review(self, title, what_user_like, what_user_dislike, rating, author_id, company_id):
        self.title = title
        self.what_user_like = what_user_like
        self.what_user_dislike = what_user_dislike
        self.rating = rating
        self.author_id = author_id
        self.company_id = company_id
