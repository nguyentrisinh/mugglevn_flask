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

    skills = db.relationship('JobSkill', back_populates='job',
                             lazy='dynamic', cascade='all, delete-orphan')
    benefits = db.relationship('JobBenefit', back_populates='job',
                               lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

    def init_job(self, name, expired_at, is_full_time, company_id, description):
        self.name = name
        self.expired_at = expired_at
        self.is_full_time = is_full_time
        self.company_id = company_id
        self.description = description

