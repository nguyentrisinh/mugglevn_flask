from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    page_size = 50
    # Show only name and email columns in list view
    column_list = ('id', 'username', 'password', 'first_name', 'last_name', 'created_at',
                   'updated_at', 'birth_date', 'email')

    # Enable search functionality - it will search for terms in
    # name and email fields
    column_searchable_list = ('username', 'email', 'first_name', 'last_name')

    # Add filters for name and email columns
    column_filters = ('username', 'email', 'first_name', 'last_name')
