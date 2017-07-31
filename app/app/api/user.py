from flask import request
from flask_restful import Resource
from ..services import UserServices
from .api_base import ApiBase


class UserRouters:
    prefix = ''

    def build_url(self, url):
        return '{}{}'.format(self.prefix, url)

    def __init__(self, api, prefix):
        self.prefix = prefix

        api.add_resource(Users, self.build_url(''))
        api.add_resource(UsersById, self.build_url('/<int:user_id>'))
        api.add_resource(UsersAvatar, self.build_url('/avatar/<int:user_id>'))


class Users(Resource, ApiBase):
    @staticmethod
    def get():
        try:
            result = UserServices.get_all()
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def post():
        try:
            user = UserServices.insert_user(request.get_json(force=True))
            return ApiBase.as_success(user)
        except Exception as ex:
            return ApiBase.as_error(ex)


class UsersById(Resource, ApiBase):
    @staticmethod
    def get(user_id):
        try:
            result = UserServices.get_by_id(user_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def put(user_id):
        try:
            result = UserServices.update_user(user_id, request.get_json(force=True))
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)

    @staticmethod
    def delete(user_id):
        try:
            UserServices.delete_user(user_id)
            result = 'Delete {} successfully'.format(user_id)
            return ApiBase.as_success(result)
        except Exception as ex:
            return ApiBase.as_error(ex)


class UsersAvatar(Resource, ApiBase):

    @staticmethod
    def post(user_id):
        try:
            result = UserServices.upload_avatar(user_id, request)
            return ApiBase.as_success(result)
        except Exception as ex:
            ApiBase.as_error(ex)


