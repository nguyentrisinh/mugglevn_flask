from ..models import db, JobSkill, Job, Skill
from ..serializers import JobSchema
from ..constant import ErrorDefine
from . import JobSkillServices, CompanyServices


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

        return result.data

