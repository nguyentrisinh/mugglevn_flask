from ..models import db, JobSkill
from ..serializers import JobSkillSchema
from ..constant import ErrorDefine


class JobSkillServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        job_skills = JobSkill.query.all()
        job_skills_schema = JobSkillSchema(many=True)
        result = job_skills_schema.dump(job_skills)
        return result.data

    @classmethod
    def get_by_id(cls, job_skill_id):
        job_skill = JobSkill.query.filter_by(id=job_skill_id).first()

        if job_skill is None:
            raise Exception(ErrorDefine.JOB_SKILL_NOT_FOUND)

        job_skill_schema = JobSkillSchema()

        result = job_skill_schema.dump(job_skill)
        return result.data

    @classmethod
    def insert(cls, job_skill_info):
        job_skill = JobSkill()

        job_id = job_skill_info['job_id']
        skill_id = job_skill_info['skill_id']
        description = job_skill_info['description']

        job_skill.init_job_skill(job_id, skill_id, description)

        db.session.add(job_skill)
        db.session.commit()

        job_skill_schema = JobSkillSchema()
        result = job_skill_schema.dump(job_skill)
        return result.data

    @classmethod
    def delete(cls, job_skill_id):
        job_skill = JobSkill.query.filter_by(id=job_skill_id).first()

        if job_skill is None:
            raise Exception(ErrorDefine.JOB_SKILL_NOT_FOUND)

        db.session.delete(job_skill)
        db.session.commit()

        return None
