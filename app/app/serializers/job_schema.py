from . import ma
from . import SkillSchema
# expired_at = db.Column(db.DateTime())
#     is_full_time = db.Column(db.Boolean)
#     company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
#     description = db.Column(db.Text)
#
#     skills = db.relationship('JobSkill', back_populates='job',
#                              lazy='dynamic', cascade='all, delete-orphan')
#     benefits = db.relationship('JobBenefit', back_populates='job',
#                                lazy='dynamic', cascade='all, delete-orphan')


class JobSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'expired_at', 'description', 'created_at',
                  'updated_at', 'company_id', 'is_full_time')

        # skills = fields.Nested(SkillSchema, many=True)

    # skills = ma.Nested(SkillSchema, many=True)
