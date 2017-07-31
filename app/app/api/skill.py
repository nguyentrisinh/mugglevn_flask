from flask import request
from flask_restful import Resource
from .api_base import ApiBase
from ..services import SkillServices


class SkillRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Skills, self.build_url(''))
        api.add_resource(Skill, self.build_url('/<int:skill_id>'))


class Skills(Resource, ApiBase):

    @staticmethod
    def get():
        try:
            result = SkillServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            skill = SkillServices.insert_skill(request.get_json(force=True))
            return ApiBase.as_success(skill)
        except Exception as ex:
            return ApiBase.as_error(ex)


class Skill(Resource, ApiBase):

    @staticmethod
    def get(skill_id):
        try:
            result = SkillServices.get_by_id(skill_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(skill_id):
        try:
            SkillServices.delete_skill(skill_id)
            return ApiBase.as_success('Delete skill\'s {} successfully'.format(skill_id))
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(skill_id):
        try:
            result = SkillServices.update_skill(skill_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

