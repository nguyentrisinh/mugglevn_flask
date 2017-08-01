from flask_marshmallow import Marshmallow
from .. import app


ma = Marshmallow(app)

from .user_schema import UserSchema
from .company_schema import CompanySchema
from .company_type_schema import CompanyTypeSchema
from .skill_schema import SkillSchema
from .benefit_schema import BenefitSchema
from .review_schema import ReviewSchema
