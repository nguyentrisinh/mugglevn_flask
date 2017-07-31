from ..models import db, Skill
from ..serializers import SkillSchema
from ..constant import ErrorDefine


class SkillServices:

    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        skill_schema = SkillSchema(many=True)
        skills = Skill.query.all()
        result = skill_schema.dump(skills)
        return result.data

    @classmethod
    def get_by_id(cls, skill_id):
        skill = Skill.query.filter_by(id=skill_id).first()

        if skill is None:
            raise Exception(ErrorDefine.SKILL_NOT_FOUND)

        skill_schema = SkillSchema()
        result = skill_schema.dump(skill)

        return result.data

    @classmethod
    def insert_skill(cls, skill_info):
        name = skill_info['name']
        info = skill_info['info']

        skill = Skill()

        skill.init_skill(name, info)

        db.session.add(skill)
        db.session.commit()

        skill_schema = SkillSchema()

        return skill_schema.dump(skill).data



