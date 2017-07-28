from flask import request
from flask_restful import Resource
from ..services import CompanyTypeServices
from .api_base import ApiBase


class CompanyTypeRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(CompanyTypes, self.build_url(''))
        api.add_resource(CompanyType, self.build_url('/<int:type_id>'))


class CompanyTypes(Resource):

    @staticmethod
    def get():
        try:
            result = CompanyTypeServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            company_type = CompanyTypeServices.insert_type(request.get_json(force=True))
            return ApiBase.as_success(company_type)
        except Exception as ex:
            return ApiBase.as_error(ex)


class CompanyType(Resource):

    @staticmethod
    def delete(type_id):
        try:
             CompanyTypeServices.delete_type(type_id)
             result = 'Delete CompanyType\'s {} successfully'.format(type_id)
             return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(type_id):
        try:
            result = CompanyTypeServices.update_type(type_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)
