from . import ma


class BenefitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
