from .. import admin, db
from ..models import User, Company, CompanyType, Review, Skill, Benefit, Job, JobSkill
from .user_view import UserView
from .company_view import CompanyView
from .company_type_view import CompanyTypeView
from .review_view import ReviewView
from .skill_view import SkillView
from .benefit_view import BenefitView
from .job_view import JobView
from .job_skill_view import JobSkillView

admin.add_view(UserView(User, db.session))
admin.add_view(CompanyView(Company, db.session))
admin.add_view(CompanyTypeView(CompanyType, db.session))
admin.add_view(ReviewView(Review, db.session))
admin.add_view(SkillView(Skill, db.session))
admin.add_view(BenefitView(Benefit, db.session))
admin.add_view(JobView(Job, db.session))
admin.add_view(JobSkillView(JobSkill, db.session))

