from flask import render_template, request
import requests
from flask import jsonify


from . import main
from .. import db
from ..models import User

@main.route('/',  methods=['GET', 'POST'])
def homepage():
    results = []
    if request.method == 'POST':
        # get url that the user has entered
        try:
            username = request.form['username']
            password = request.form['password']
            firstname = request.form['firstname']
            lastname = request.form ['lastname']


            user = User(username, password, firstname, lastname)
            db.session.add(user)
            db.session.commit()
            results.append(
                'Insert user "%s" successfully' %user.full_name()
            )
        except:
            print(user.full_name())
            results.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            results.append(
                user.full_name()
            )
    return render_template('index.html', results = results)


# Url test method for query database
@main.route('/query',  methods=['GET', 'POST'])
def query():
    results = []
    if request.method == 'POST':
        # try to query username using username
        try:
            username = request.form['username']
            user = User.get_user_by_username(username)
            print "123"
            if user is None:
                results.append("Can't find %s user" %username)
            else:
                print(user.full_name())
                results.append(user.full_name())
                results.append(user.username)
                results.append(user.password)
        except Exception as ex:
            print type(ex)
            print ex
            results.append(
                'Failed in query user! u '
            )

    return render_template('query.html', results=results)


# Url test method for query all user in database
@main.route('/query_all',  methods=['GET', 'POST'])
def query_all_user():
    results = []
    if request.method == 'POST':
        # try to query username using username
        try:
            users = User.get_all_user()
            # print jsonify(users=list(User.get_all_user()))
            if users is None:
                results.append('Can query all users in database')
            else:
                # print(users.full_name())
                for user in users:
                    results.append(user.full_name())
        except:
            results.append(
                "Failed in query user!"
            )

    return render_template('query_all_user.html', results=results)


@main.route('/delete', methods=['GET', 'POST'])
def delete():
    results = []
    if request.method == 'POST':
        # try to delete user using username
        result = User.delete_user_by_id(request.form['username'])
        results.append(result)
    return render_template('delete.html', results=results)


@main.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    results = []
    slug = ('/update/' + str(id) + '/')
    user = User.get_user_by_id(id)

    if request.method == 'POST':
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        results.append(User.update_user_by_id(id, password, firstname, lastname))

    return render_template('update.html', results=results, update_slug=slug, user=user)
