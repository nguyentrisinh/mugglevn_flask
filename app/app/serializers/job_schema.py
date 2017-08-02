from . import ma


class JobSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'expired_at', 'description', 'created_at',
                  'updated_at', 'company_id', 'is_full_time')
