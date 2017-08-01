from . import ma


class JobSkillSchema(ma.Schema):
    class Meta:
        fields = ('id', 'job_id', 'skill_id', 'description', 'created_at', 'updated_at')