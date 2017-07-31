from ..models import CompanyType, db
from ..serializers import CompanyTypeSchema
from ..constant import ErrorDefine


class CompanyTypeServices:
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        company_type_schema = CompanyTypeSchema(many=True)
        all_company_type = CompanyType.query.all()
        result = company_type_schema.dump(all_company_type)
        return result.data

    @classmethod
    def get_by_id(cls, type_id):
        company_type = CompanyType.query.filter_by(id=type_id).first()

        if company_type is None:
            raise Exception(ErrorDefine.COMPANY_TYPE_NOT_FOUND)

        company_type_schema = CompanyTypeSchema()
        result = company_type_schema.dump(company_type)
        return result.data

    @classmethod
    def insert_type(cls, company_type_info):
        company_type_schema = CompanyTypeSchema()
        company_type = CompanyType()
        company_type.init_company_type(company_type_info['name'])

        db.session.add(company_type)
        db.session.commit()

        result = company_type_schema.dump(company_type)
        return result.data

    @classmethod
    def delete_type(cls, type_id):
        company_type = CompanyType.query.filter_by(id=type_id).first()\

        if company_type is None:
           raise Exception(ErrorDefine.COMPANY_TYPE_NOT_FOUND)

        db.session.delete(company_type)
        db.session.commit()

        return {}

    @classmethod
    def update_type(cls, type_id, type_info):
        company_type = CompanyType.query.filter_by(id=type_id).first()

        if company_type is None:
            raise Exception(ErrorDefine.COMPANY_TYPE_NOT_FOUND)

        company_type.name = type_info['name']

        db.session.commit()

        company_type_schema = CompanyTypeSchema()
        return company_type_schema.dump(company_type).data



