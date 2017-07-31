from flask import request
from flask_restful import Resource
from ..models import db, Benefit
from .api_base import ApiBase
from ..services import BenefitServices


class BenefitRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Benefits, self.build_url(''))


class Benefits(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = BenefitServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            result = BenefitServices.insert(request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)
