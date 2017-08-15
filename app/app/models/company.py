from . import db


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    slug = db.Column(db.String(120))
    website = db.Column(db.String(250))
    size = db.Column(db.Integer)
    rating = db.Column(db.Float, default=4.0, nullable=False)
    bio = db.Column(db.Text)
    overview = db.Column(db.Text)
    email = db.Column(db.String(120))
    address = db.Column(db.String(512))
    google_map = db.Column(db.String(512))
    job_count = db.Column(db.Integer)
    review_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    avatar = db.Column(db.String(512))
    district = db.Column(db.String(125))
    type_id = db.Column(db.Integer, db.ForeignKey('company_type.id'))

    type = db.relationship("CompanyType", foreign_keys=type_id)
    jobs = db.relationship('Job', backref='company',
                           lazy='dynamic')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def init_company(self, name, slug, website, size, rating, bio, overview, email, type_id,
                     address, google_map, job_count, review_count):
        self.name = name
        self.slug = slug
        self.website = website
        self.size = size
        self.rating = rating
        self.bio = bio
        self.overview = overview
        self.email = email
        self.address = address
        self.google_map = google_map
        self.job_count = job_count
        self.review_count = review_count
        self.type_id = type_id

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<id {}>'.format(self.id)
