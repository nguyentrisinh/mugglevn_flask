from . import ma


class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'slug', 'website', 'size', 'rating', 'bio', 'overview', 'email',
                  'address', 'google_map', 'job_count', 'review_count', 'created_at', 'updated_at', 'type_id')

