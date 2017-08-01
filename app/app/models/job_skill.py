from . import db


class JobSkill(db.Model):
    __tablename__ = 'job_skill'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    job = db.relationship("Job", foreign_keys=job_id)
    skill = db.relationship("Skill", foreign_keys=skill_id)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        if self.job is None:
            return '{}'.format(self.skill.name)
        if self.skill is None:
            return '{}'.format(self.job.name)
        return '{}-{}'.format(self.job.name, self.skill.name)

    def init_job_skill(self, job_id, skill_id, description):
        self.job_id = job_id
        self.skill_id = skill_id
        self.description = description

