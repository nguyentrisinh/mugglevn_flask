from . import ma


class CompanyTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

