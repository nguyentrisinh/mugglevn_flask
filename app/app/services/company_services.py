from sqlalchemy.exc import IntegrityError
from ..models import db, Company
from ..serializers import CompanySchema
from ..constant import ErrorDefine
from .file_services import FileServices


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
        except IntegrityError as err:
            return err
        except Exception as ex:
            return ex

    @classmethod
    def update_company(cls, company_id, company_info):
        try:
            company = Company.query.filter_by(id=company_id).first()

            if company is None:
                raise Exception(ErrorDefine.COMPANY_NOT_FOUND)

            company.name = company_info['name']
            company.slug = company_info['slug']
            company.website = company_info['website']
            company.size = company_info['size']
            company.rating = company_info['rating']
            company.bio = company_info['bio']
            company.overview = company_info['overview']
            company.email = company_info['email']
            company.address = company_info['address']
            company.google_map = company_info['google_map']
            company.job_count = company_info['job_count']
            company.review_count = company_info['review_count']
            company.type_id = company_info['type_id']

            db.session.commit()

            company_schema = CompanySchema()
            return company_schema.dump(company)
        except Exception as (ex):
            raise ex

    @classmethod
    def upload_avatar(cls, company_id, request):
        company = Company.query.filter_by(id=company_id).first()

        if company is None:
            raise Exception(ErrorDefine.COMPANY_NOT_FOUND)

        avatar_path = FileServices.upload_file('/companies/avatar/{}'.format(company_id), request)

        print avatar_path
        company.avatar = avatar_path['content']
        db.session.commit()

        company_schema = CompanySchema()
        result = company_schema.dump(company)

        return result.data


