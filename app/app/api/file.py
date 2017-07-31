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


class File(Resource, ApiBase):

    @staticmethod
    def post():
        try:
            result = FileServices.upload_file('/users/avatar/1', request)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)