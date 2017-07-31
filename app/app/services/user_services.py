from ..models import User, db
from ..serializers import UserSchema
from ..constant import ErrorDefine
from .file_services import FileServices


class UserServices:
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        users_schema = UserSchema(many=True, only=['id', 'username', 'first_name'])
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return result.data

    @classmethod
    def get_by_id(cls, user_id):
        user_schema = UserSchema()
        user = User.query.filter_by(id=user_id).first()

        if user is None:
            raise Exception(ErrorDefine.USER_NOT_FOUND)

        result = user_schema.dump(user)

        return result.data

    @classmethod
    def insert_user(cls, user_info):
        user_schema = UserSchema()

        username = user_info['username']
        password = user_info['password']
        first_name = user_info['first_name']
        last_name = user_info['last_name']
        birth_date = user_info['birth_date']
        email = user_info['email']
        university_name = user_info['university_name']
        major_name = user_info['major_name']
        faculty_name = user_info['faculty_name']
        address = user_info['address']
        avatar = user_info['avatar']

        user = User()
        user.init_user(username, password, first_name, last_name,
                       birth_date, email, university_name, major_name, faculty_name, address, avatar)

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)

        return result.data

    @classmethod
    def update_user(cls, user_id, user_info):
        user_schema = UserSchema()

        user = User.query.filter_by(id=user_id).first()

        if user is None:
            raise Exception(ErrorDefine.USER_NOT_FOUND)

        user.password = user_info['password']
        user.first_name = user_info['first_name']
        user.last_name = user_info['last_name']
        user.avatar = user_info['avatar']
        db.session.commit()

        result = user_schema.dump(user)

        return result.data

    @classmethod
    def delete_user(cls, user_id):
        user = User.query.filter_by(id=user_id).first()

        if user is None:
            raise Exception(ErrorDefine.USER_NOT_FOUND)

        db.session.delete(user)
        db.session.commit()

        return {}


    @classmethod
    def upload_avatar(cls, user_id, request):
        user = User.query.filter_by(id=user_id).first()

        if user is None:
            raise Exception(ErrorDefine.USER_NOT_FOUND)

        avatar_path = FileServices.upload_file('/users/avatar/{}'.format(user_id), request)

        user.avatar = avatar_path['content']
        db.session.commit()

        user_schema = UserSchema()
        result = user_schema.dump(user)

        return result.data
