from flask import Blueprint
from flask_restful import Api
from .user import UserRouters
from .company import CompanyRouters
from .company_type import CompanyTypeRoutes
from .skill import SkillRoutes
from .file import FileRoutes
from .benefit import BenefitRoutes
from .review import ReviewRoutes
from .job_skill import JobSkillRoutes
from .job import JobRoutes
from .job_benefit import JobBenefitRoutes

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

UserRouters(api, '/users')
CompanyRouters(api, '/companies')
CompanyTypeRoutes(api, '/company_types')
SkillRoutes(api, '/skills')
FileRoutes(api, '/files')
BenefitRoutes(api, '/benefits')
ReviewRoutes(api, '/reviews')
JobSkillRoutes(api, '/job_skills')
JobRoutes(api, '/jobs')
JobBenefitRoutes(api, '/job_benefits')
