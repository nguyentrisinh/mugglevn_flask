from . import ma


class JobBenefitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'job_id', 'benefit_id', 'description', 'created_at', 'updated_at')
