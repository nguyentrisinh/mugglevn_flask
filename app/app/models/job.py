from . import db

# name = models.CharField(max_length=255)
# created_by = models.CharField(max_length=255)
# how_to_apply = models.TextField(default='', blank=True)
# skills = models.ManyToManyField(
#     'jobsite.Skill',
#     related_name='skills',
#     through='jobsite.JobSkill',
#     through_fields=('job', 'skill'),
#     blank=True, default=None)
# benefits = models.ManyToManyField(
#     'jobsite.Benefit',
#     through='jobsite.JobBenefit',
#     through_fields=('job', 'benefit'),
#     blank=True, default=None)


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())
    expired_at = db.Column(db.DateTime())
    is_full_time = db.Column(db.Boolean)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    description = db.Column(db.Text)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

