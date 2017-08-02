from flask import request
from flask_restful import Resource
from ..services import JobBenefitServices
from .api_base import ApiBase


class JobBenefitRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(JobBenefits, self.build_url(''))
        api.add_resource(JobBenefit, self.build_url('/<int:job_benefit_id>'))
        api.add_resource(JobToBenefit, self.build_url('/job/<int:job_id>'))


class JobBenefits(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = JobBenefitServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            result = JobBenefitServices.insert(request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class JobBenefit(Resource, ApiBase):

    @staticmethod
    def get(job_benefit_id):
        try:
            result = JobBenefitServices.get_by_id(job_benefit_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(job_benefit_id):
        try:
            result = JobBenefitServices.update(job_benefit_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(job_benefit_id):
        try:
            result = JobBenefitServices.get_by_id(job_benefit_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class JobToBenefit(Resource, ApiBase):

    @staticmethod
    def get(job_id):
        try:
            result = JobBenefitServices.get_by_job_id(job_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

