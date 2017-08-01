from . import ma
from ..models import Review


class ReviewSchema(ma.Schema):
    class Meta:
        # fields = ('id', 'title', 'created_at', 'updated_at', 'what_user_like', 'what_user_dislike', 'rating',
        #           'author_id', 'company_id')
        model = Review
