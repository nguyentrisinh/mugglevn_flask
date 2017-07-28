from . import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'created_at', 'updated_at',
                  'birth_date', 'email', 'university_name', 'major_name', 'faculty_name', 'address')

