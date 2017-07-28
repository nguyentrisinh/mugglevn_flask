from sqlalchemy.exc import IntegrityError
from ..models import db, Company
from ..serializers import CompanySchema
from ..constant import ErrorDefine


class CompanyServices:
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        company_schema = CompanySchema(many=True, only=['id', 'name', 'type_id'])
        all_companies = Company.query.all()
        result = company_schema.dump(all_companies)
        return result.data

    @classmethod
    def get_by_id(cls, company_id):
        company_schema = CompanySchema()

        company = Company.query.filter_by(id=company_id).first()

        if company is None:
            raise Exception(ErrorDefine.COMPANY_NOT_FOUND)

        result = company_schema.dump(company)

        return result.data

    @classmethod
    def insert_company(cls, company_info):
        company_schema = CompanySchema()

        name = company_info['name']
        slug = company_info['slug']
        website = company_info['website']
        size = company_info['size']
        rating = company_info['rating']
        bio = company_info['bio']
        overview = company_info['overview']
        email = company_info['email']
        type_id = company_info['type_id']
        address = company_info['address']
        google_map = company_info['google_map']
        job_count = company_info['job_count']
        review_count = company_info['review_count']

        company = Company()
        company.init_company(name, slug, website, size, rating, bio, overview, email, type_id,
                             address, google_map, job_count, review_count)

        db.session.add(company)
        db.session.commit()

        result = company_schema.dump(company)

        return result.data

    @classmethod
    def delete_company(cls, company_id):
        try:
            company = Company.query.filter_by(id=company_id).first()

            if company is None:
                raise Exception(ErrorDefine.COMPANY_NOT_FOUND)

            db.session.delete(company)
            db.session.commit()

            return None
        except Exception as ex:
            return ex


