from flask import request
from flask_restful import Resource
from ..models import Review
from .api_base import ApiBase
from ..services import ReviewServices


class ReviewRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Reviews, self.build_url(''))
        api.add_resource(Review, self.build_url('/<int:review_id>'))
        api.add_resource(CompanyReview, self.build_url('/company/<int:company_id>'))


class Reviews(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = ReviewServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            result = ReviewServices.insert(request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class Review(Resource, ApiBase):

    @staticmethod
    def get(review_id):
        try:
            result = ReviewServices.get_by_id(review_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(review_id):
        try:
            ReviewServices.delete(review_id)
            return ApiBase.as_success('delete review\'s {} successfully'.format(review_id))
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(review_id):
        try:
            result = ReviewServices.update(review_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class CompanyReview(Resource, ApiBase):

    @staticmethod
    def get(company_id):
        try:
            result = ReviewServices.get_by_company(company_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)
