from . import ma
from ..models import Company


class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'slug', 'website', 'size', 'rating', 'bio', 'overview', 'email', 'avatar',
                  'address', 'google_map', 'job_count', 'review_count', 'created_at', 'updated_at', 'type_id', 'district')
