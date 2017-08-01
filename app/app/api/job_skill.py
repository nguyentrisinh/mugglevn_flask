from flask import request
from flask_restful import Resource
from ..services import JobSkillServices
from .api_base import ApiBase


class JobSkillRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(JobSkills, self.build_url(''))
        api.add_resource(JobSkill, self.build_url('/<int:job_skill_id>'))


class JobSkills(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = JobSkillServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            result = JobSkillServices.insert(request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class JobSkill(Resource, ApiBase):

    @staticmethod
    def get(job_skill_id):
        try:
            result = JobSkillServices.get_by_id(job_skill_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(job_skill_id):
        try:
            JobSkillServices.delete(job_skill_id)
            return ApiBase.as_success('Delete JobSkill\'s {} successfully'.format(job_skill_id))
        except Exception as ex:
            return ApiBase.as_error(ex)

