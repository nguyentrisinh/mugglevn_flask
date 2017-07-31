from ..models import db, Benefit
from ..serializers import BenefitSchema
from ..constant import ErrorDefine


class BenefitServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        benefits = Benefit.query.all()

        benefit_schema = BenefitSchema(many=True)

        result = benefit_schema.dump(benefits)

        return result.data

    @classmethod
    def insert(cls, benefit_info):
        benefit = Benefit()
        benefit.init_benefit(benefit_info['name'])

        db.session.add(benefit)
        db.session.commit()

        benefit_schema = BenefitSchema()

        result = benefit_schema.dump(benefit)
        return result.data
