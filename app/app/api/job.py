from flask import request
from flask_restful import Resource
from ..services import JobServices
from .api_base import ApiBase


class JobRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Jobs, self.build_url(''))
        api.add_resource(Job, self.build_url('/<int:job_id>'))
        api.add_resource(CompanyToJob, self.build_url('/company/<int:company_id>'))


class Jobs(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = JobServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            result = JobServices.insert(request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class Job(Resource, ApiBase):

    @staticmethod
    def get(job_id):
        try:
            result = JobServices.get_by_id(job_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(job_id):
        try:
            JobServices.delete(job_id)
            result = 'Delete job\'s {} successfully'.format(job_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(job_id):
        try:
            result = JobServices.update(job_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class CompanyToJob(Resource, ApiBase):

    @staticmethod
    def get(company_id):
        try:
            result = JobServices.get_by_company(company_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)