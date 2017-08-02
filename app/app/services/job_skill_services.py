from ..models import db, JobSkill, Job, Skill
from ..serializers import JobSkillSchema
from ..constant import ErrorDefine
from . import SkillServices


class JobSkillServices:

    def __init__(self):
        pass

    @classmethod
    def check_condition(cls, job_skill_info):
        job = Job.query.filter_by(id=job_skill_info['job_id']).first()

        if job is None:
            raise Exception(ErrorDefine.JOB_NOT_FOUND)

        skill = Skill.query.filter_by(id=job_skill_info['skill_id']).first()
        if skill is None:
            raise Exception(ErrorDefine.SKILL_NOT_FOUND)

        return True

    @classmethod
    def get_all(cls):
        job_skills = JobSkill.query.all()
        job_skills_schema = JobSkillSchema(many=True)
        results = job_skills_schema.dump(job_skills)

        for result in results.data:
            result['skill'] = SkillServices.get_by_id(result['skill_id'])

        return results.data

    @classmethod
    def get_by_id(cls, job_skill_id):
        job_skill = JobSkill.query.filter_by(id=job_skill_id).first()

        if job_skill is None:
            raise Exception(ErrorDefine.JOB_SKILL_NOT_FOUND)

        job_skill_schema = JobSkillSchema()

        result = job_skill_schema.dump(job_skill)
        result.data['skill'] = SkillServices.get_by_id(result.data['skill_id'])

        return result.data

    @classmethod
    def get_by_job_id(cls, job_id):
        # job_skill = JobSkill.query.filter_by(job_id=job_id)

        # job_skill = JobSkill.query.join(Skill).filter_by(job_id=job_id)
        job_skill = JobSkill.query.filter_by(job_id=job_id)
        job_skill_schema = JobSkillSchema(many=True, only=['skill_id', 'description'])

        results = job_skill_schema.dump(job_skill)

        for result in results.data:
            result['skill'] = SkillServices.get_by_id(result['skill_id'])

        return results.data

    @classmethod
    def insert(cls, job_skill_info):
        job_skill = JobSkill()

        if cls.check_condition(job_skill_info) is not True:
            return None

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
    def update(cls, job_skill_id, job_skill_info):
        job_skill = JobSkill.query.filter_by(id=job_skill_id).first()

        if job_skill is None:
            raise Exception(ErrorDefine.JOB_SKILL_NOT_FOUND)

        if cls.check_condition(job_skill_info) is not True:
            return None

        job_skill.job_id = job_skill_info['job_id']
        job_skill.skill_id = job_skill_info['skill_id']
        job_skill.description = job_skill_info['description']

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
