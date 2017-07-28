from flask_marshmallow import Marshmallow
from .. import app


ma = Marshmallow(app)

from .user_schema import UserSchema
from .company_schema import CompanySchema
