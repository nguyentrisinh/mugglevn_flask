from ..models import db, JobBenefit
from ..serializers import JobBenefitSchema
from ..constant import ErrorDefine
from . import BenefitServices


class JobBenefitServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        job_benefits = JobBenefit.query.all()

        job_benefit_schema = JobBenefitSchema(many=True, only=['id', 'job_id', 'benefit_id'])
        results = job_benefit_schema.dump(job_benefits)

        return results.data

    @classmethod
    def get_by_id(cls, job_benefit_id):
        job_benefit = JobBenefit.query.filter_by(id=job_benefit_id).first()

        if job_benefit is None:
            raise Exception(ErrorDefine.JOB_BENEFIT_NOT_FOUND)

        job_benefit_schema = JobBenefitSchema()

        result = job_benefit_schema.dump(job_benefit)

        result.data['benefit'] = BenefitServices.get_by_id(result.data['benefit_id'])

        return result.data

    @classmethod
    def get_by_job_id(cls, job_id):
        job_benefit = JobBenefit.query.filter_by(id=job_id)

        job_benefit_schema = JobBenefitSchema(many=True)

        results = job_benefit_schema.dump(job_benefit)

        for result in results.data:
            result['benefit'] = BenefitServices.get_by_id(result['benefit_id'])

        return results.data

    @classmethod
    def insert(cls, job_benefit_info):

        job_id = job_benefit_info['job_id']
        benefit_id = job_benefit_info['benefit_id']
        description = job_benefit_info['description']

        job_benefit = JobBenefit()
        job_benefit.init_job_benefit(job_id, benefit_id, description)

        db.session.add(job_benefit)
        db.session.commit()

        job_benefit_schema = JobBenefitSchema()
        result = job_benefit_schema.dump(job_benefit)
        result.data['benefit'] = BenefitServices.get_by_id(result.data['benefit_id'])

        return result.data

    @classmethod
    def delete(cls, job_benefit_id):
        job_benefit = JobBenefit.query.filter_by(id=job_benefit_id)

        if job_benefit is None:
            raise Exception(ErrorDefine.JOB_BENEFIT_NOT_FOUND)

        db.session.delete(job_benefit)
        db.session.commit()

        return {}

    @classmethod
    def update(cls, job_benefit_id, job_benefit_info):
        job_benefit = JobBenefit.query.filter_by(id=job_benefit_id).first()

        if job_benefit is None:
            raise Exception(ErrorDefine.JOB_BENEFIT_NOT_FOUND)

        job_benefit.job_id = job_benefit_info['job_id']
        job_benefit.benefit_id = job_benefit_info['benefit_id']
        job_benefit.description = job_benefit_info['description']

        db.session.commit()

        job_benefit_schema = JobBenefitSchema()

        result = job_benefit_schema.dump(job_benefit)

        return result.data
