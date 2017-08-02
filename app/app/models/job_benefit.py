from . import db


class JobBenefit(db.Model):
    __tablename__ = 'job_benefit'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    benefit_id = db.Column(db.Integer, db.ForeignKey('benefits.id'))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    job = db.relationship("Job", foreign_keys=job_id)
    benefit = db.relationship("Benefit", foreign_keys=benefit_id)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        if self.job is None:
            return '{}'.format(self.benefit.name)
        if self.benefit is None:
            return '{}'.format(self.job.name)
        return '{}-{}'.format(self.job.name, self.benefit.name)

    def init_job_benefit(self, job_id, benefit_id, description):
        self.job_id = job_id
        self.benefit_id = benefit_id
        self.description = description

