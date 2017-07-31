from flask import request
from flask_restful import Resource
from .api_base import ApiBase
from ..services import FileServices


class FileRoutes:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(File, self.build_url(''))
        # api.add_resource(Skill, self.build_url('/<int:skill_id>'))


class File(Resource, ApiBase):
    def __init__(self):
        pass

    @staticmethod
    def post():
        try:
            result = FileServices.upload_file(request)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)