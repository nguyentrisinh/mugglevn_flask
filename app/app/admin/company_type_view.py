from flask_admin.contrib.sqla import ModelView


class CompanyTypeView(ModelView):
    page_size = 50

    # Show only name and email columns in list view
    column_list = ('id', 'name')