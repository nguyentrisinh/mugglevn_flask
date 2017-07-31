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
    def get_by_id(cls, benefit_id):
        benefit = Benefit.query.filter_by(id=benefit_id).first()

        if benefit is None:
            raise Exception(ErrorDefine.BENEFIT_NOT_FOUND)

        benefit_schema = BenefitSchema()
        result = benefit_schema.dump(benefit)
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

    @classmethod
    def delete(cls, benefit_id):
        benefit = Benefit.query.filter_by(id=benefit_id).first()

        if benefit is None:
            raise Exception(ErrorDefine.BENEFIT_NOT_FOUND)

        db.session.delete(benefit)
        db.session.commit()

        return {}
