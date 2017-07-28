from flask import request
from sqlalchemy import exc
from flask_restful import Resource
from ..services import CompanyServices
from .api_base import ApiBase


class CompanyRouters:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Companies, self.build_url(''))
        api.add_resource(Company, self.build_url('/<int:company_id>'))


class Companies(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = CompanyServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            company = CompanyServices.insert_company(request.get_json(force=True))
            return ApiBase.as_success(company)
        except Exception as ex:
            return ApiBase.as_error(ex)


class Company(Resource, ApiBase):

    @staticmethod
    def get(company_id):
        try:
            result = CompanyServices.get_by_id(company_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(company_id):
        try:
            error = CompanyServices.delete_company(company_id)

            if error is not None:
                if type(error) is exc.IntegrityError:
                    raise exc.SQLAlchemyError(error.message)

                raise Exception(error.message)

            result = 'Delete company\'s {} successfully'.format(company_id)

            return ApiBase.as_success(result)

        except exc.SQLAlchemyError as err:
            return ApiBase.as_error(err)

        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(company_id):
        try:
            result = CompanyServices.update_company(company_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)
