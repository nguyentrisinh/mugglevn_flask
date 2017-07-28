from flask_admin.contrib.sqla import ModelView


class ReviewView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'title', 'rating', 'created_at', 'updated_at', 'author', 'author_id', 'company', 'company_id')

    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('title', 'rating', 'author_id', 'company_id')

    # Add filters for name and email columns
    column_filters = ('rating', 'title', 'author', 'company')
