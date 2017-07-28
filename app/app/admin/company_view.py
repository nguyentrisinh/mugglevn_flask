from flask_admin.contrib.sqla import ModelView


class CompanyView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'name', 'slug', 'size', 'rating', 'job_count', 'review_count', 'created_at', 'updated_at',
                   'type', 'type_id')
    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('name', 'email', 'id')

    # Add filters for name and email columns
    column_filters = ('name', 'size', 'rating', 'job_count', 'review_count', 'created_at', 'updated_at', 'type')
