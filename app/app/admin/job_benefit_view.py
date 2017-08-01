from flask_admin.contrib.sqla import ModelView


class JobBenefitView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'job_id', 'benefit_id', 'description')
    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('job_id', 'benefit_id', 'id')

    # Add filters for name and email columns
    column_filters = ('job_id', 'benefit_id', 'id')
