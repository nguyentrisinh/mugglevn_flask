from flask_admin.contrib.sqla import ModelView


class BenefitView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'name')

    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('id', 'name')

    # Add filters for name and email columns
    column_filters = ('id', 'name')
