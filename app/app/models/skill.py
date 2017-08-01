from . import db


class Skill(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    info = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    # jobs = db.relationship('JobSkill', backref='skills',
    #                        lazy='dynamic')

    jobs = db.relationship('JobSkill', back_populates='skill',
                           lazy='dynamic')

    # Test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # jobs = db.relationship("JobSkill", back_populates="job")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

    def init_skill(self, name, info):
        self.name = name
        self.info = info
