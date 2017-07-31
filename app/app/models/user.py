from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    birth_date = db.Column(db.DateTime())
    email = db.Column(db.String(120), nullable=True)
    university_name = db.Column(db.String(120), nullable=True)
    major_name = db.Column(db.String(120), nullable=True)
    faculty_name = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)

    avatar = db.Column(db.String())

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def init_user(self, username, password, first_name, last_name,
                  birth_date, email, university_name, major_name, faculty_name, address, avatar):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.university_name = university_name
        self.major_name = major_name
        self.faculty_name = faculty_name
        self.address = address
        self.avatar = avatar

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_created_at(self):
        return self.created_at


