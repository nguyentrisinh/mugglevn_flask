from flask import Blueprint
from flask_restful import Api
from .user import UserRouters
from .company import CompanyRouters
from .company_type import CompanyTypeRoutes

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

UserRouters(api, '/users')
CompanyRouters(api, '/companies')
CompanyTypeRoutes(api, '/company_types')

