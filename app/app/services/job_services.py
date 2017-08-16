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
        # Just select limit to 6 item
        jobs = Job.query.order_by(Job.id.desc()).limit(6)

        job_schema = JobSchema(many=True)
        results = job_schema.dump(jobs)

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

        result.data['skills'] = JobSkillServices.get_by_job_id(result.data['id'])
        result.data['company'] = CompanyServices.get_by_id(result.data['company_id'])
        result.data['benefits'] = JobBenefitServices.get_by_job_id(result.data['id'])

        return result.data

    @classmethod
    def get_by_company(cls, company_id):
        jobs = Job.query.filter_by(company_id=company_id)

        job_schema = JobSchema(many=True)

        results = job_schema.dump(jobs)

        for result in results.data:
            result['skill'] = JobSkillServices.get_by_job_id(result['id'])

        return results.data

    @classmethod
    def get_short_info_by_company(cls, company_id):
        jobs = Job.query.filter_by(company_id=company_id)

        job_schema = JobSchema(many=True, only=['id', 'name', 'description'])

        results = job_schema.dump(jobs)

        return results.data


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

        cls.update_job_count(company_id)

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

        cls.update_job_count(job_info['company_id'])

        db.session.commit()

        job_schema = JobSchema()
        result = job_schema.dump(job)

        return result.data

    @classmethod
    def delete(cls, job_id):
        job = Job.query.filter_by(id=job_id).first()

        company_id = job.company_id

        if job is None:
            raise Exception(ErrorDefine.JOB_NOT_FOUND)

        db.session.delete(job)
        db.session.commit()

        cls.update_job_count(company_id)

        return {}

    @classmethod
    def update_job_count(cls, company_id):
        company = CompanyServices.get_object_by_id(company_id)
        job_count = Job.query.filter_by(company_id=company_id).count()

        company.job_count = job_count

        db.session.commit()

