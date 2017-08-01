from ..models import db, Review
from ..serializers import ReviewSchema
from ..constant import ErrorDefine


class ReviewServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        reviews = Review.query.all()

        review_schema = ReviewSchema(many=True, only=['id', 'created_at',
                                                      'updated_at', 'rating', 'author_id', 'company_id'])

        result = review_schema.dump(reviews)

        return result.data

    @classmethod
    def get_by_id(cls, review_id):
        review = Review.query.filter_by(id=review_id).first()

        if review is None:
            raise Exception(ErrorDefine.REVIEW_NOT_FOUND)

        review_schema = ReviewSchema()

        result = review_schema.dump(review)

        return result.data

    @classmethod
    def insert(cls, review_info):

        title = review_info['title']
        what_user_like = review_info['what_user_like']
        what_user_dislike = review_info['what_user_dislike']
        rating = review_info['rating']
        author_id = review_info['author_id']
        company_id = review_info['company_id']

        review = Review()
        review.init_review(title, what_user_like, what_user_dislike, rating, author_id, company_id)

        db.session.add(review)
        db.session.commit()

        review_schema = ReviewSchema()
        result = review_schema.dump(review)

        return result.data

    @classmethod
    def delete(cls, review_id):
        review = Review.query.filter_by(id=review_id).first()

        if review is None:
            raise Exception(ErrorDefine.REVIEW_NOT_FOUND)

        db.session.delete(review)
        db.session.commit()

        return {}

    @classmethod
    def update(cls, review_id, review_info):
        review = Review.query.filter_by(id=review_id).first()

        if review is None:
            raise Exception(ErrorDefine.REVIEW_NOT_FOUND)

        review.rating = review_info['rating']
        review.what_user_like = review_info['what_user_like']
        review.what_user_dislike = review_info['what_user_dislike']

        db.session.commit()

        review_schema = ReviewSchema()
        result = review_schema.dump(review)

        return result.data

    @classmethod
    def get_by_company(cls, company_id):
        review = Review.query.filter_by(company_id=company_id)

        review_schema = ReviewSchema(many=True, only=['id', 'author_id', 'title', 'what_user_like', 'created_at',
                                                      'what_user_dislike', 'rating'])

        result = review_schema.dump(review)

        return result.data
