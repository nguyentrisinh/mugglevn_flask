from . import db


class JobSkill(db.Model):
    __tablename__ = 'job_skill'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))
    description = db.Column(db.Text)

    job = db.relationship("Job", foreign_keys=job_id)
    skill = db.relationship("Skill", foreign_keys=skill_id)

    # Test~~~~~~~~~~~~~~~~~~~~~~
    # job = db.relationship("Job", back_populates="skills")
    # skill = db.relationship("Skill", back_populates="jobs")


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return '{}-{}'.format(self.job.name, self.skill.name)
