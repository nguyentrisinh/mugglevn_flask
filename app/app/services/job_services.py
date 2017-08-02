from ..models import db, Job
from ..serializers import JobSchema
from ..constant import ErrorDefine
from . import JobSkillServices, CompanyServices
from.job_benefit_services import JobBenefitServices


class JobServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        job = Job.query.all()

        job_schema = JobSchema(many=True)
        results = job_schema.dump(job)

        for result in results.data:
            result['skill'] = JobSkillServices.get_by_job_id(result['id'])
            result['company'] = CompanyServices.get_by_id(result['company_id'])
            result['benefit'] = JobBenefitServices.get_by_job_id(result['id'])

        return results.data

    @classmethod
    def get_by_id(cls, job_id):
        job = Job.query.filter_by(id=job_id).first()

        if job is None:
            raise Exception(ErrorDefine.JOB_NOT_FOUND)

        job_schema = JobSchema()

        result = job_schema.dump(job)

        result.data['skill'] = JobSkillServices.get_by_job_id(result.data['id'])
        result.data['company'] = CompanyServices.get_by_id(result.data['company_id'])
        result.data['benefit'] = JobBenefitServices.get_by_job_id(result.data['id'])

        return result.data

    @classmethod
    def insert(cls, job_info):

        name = job_info['name']
        expired_at = job_info['expired_at']
        is_full_time = job_info['is_full_time']
        company_id = job_info['company_id']
        description = job_info['description']

        job = Job()
        job.init_job(name, expired_at, is_full_time, company_id, description)

        db.session.add(job)
        db.session.commit()

        job_schema = JobSchema()
        result = job_schema.dump(job)

        return result.data

    @classmethod
    def update(cls, job_id, job_info):
        job = Job.query.filter_by(id=job_id).first()

        if job is None:
            raise Exception(ErrorDefine.JOB_NOT_FOUND)

        job.name = job_info['name']
        job.expired_at = job_info['expired_at']
        job.is_full_time = job_info['is_full_time']
        job.company_id = job_info['company_id']
        job.description = job_info['description']

        db.session.commit()

        job_schema = JobSchema()
        result = job_schema.dump(job)

        return result.data

    @classmethod
    def delete(cls, job_id):
        job = Job.query.filter_by(id=job_id).first()

        if job is None:
            raise Exception(ErrorDefine.JOB_NOT_FOUND)

        db.session.delete(job)
        db.session.commit()

        return {}
