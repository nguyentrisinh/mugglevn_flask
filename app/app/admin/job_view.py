from flask_admin.contrib.sqla import ModelView


class JobView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'name', 'created_at', 'updated_at', 'is_full_time')
    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('name', 'is_full_time', 'id')

    # Add filters for name and email columns
    column_filters = ('name', 'created_at', 'updated_at', 'id')
