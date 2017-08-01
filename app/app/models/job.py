from . import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    expired_at = db.Column(db.DateTime())
    is_full_time = db.Column(db.Boolean)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    description = db.Column(db.Text)

    # skills = db.relationship('JobSkill', backref='job',
    #                          lazy='dynamic')
    skills = db.relationship('JobSkill', back_populates='job',
                             lazy='dynamic', cascade="all, delete-orphan")

    # Test~~~~~~~~~~~~~~~~~~~
    # skills = db.relationship("JobSkill", back_populates="skill")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

