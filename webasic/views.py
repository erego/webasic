
# Third-party imports
from flask import render_template, request

# Local imports
from webasic import app
from webasic.models.person import Person, Filter
from webasic.models.database import DataBase, SQLITE

DB = DataBase(SQLITE, dbname='webasic/database/webasic_db.db')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/person_list', methods=['GET', 'POST'])
def person_list():
    filter_sql = Filter()
    if request.method == 'POST':
        filter_sql.name = request.form['name']
        filter_sql.surname = request.form['surname']

    lst_person = filter_sql.person_list_filter()

    return render_template('person/list.html', lst_person=lst_person)


@app.route('/person_new')
def person_new():
    return render_template('person/new.html')


@app.route('/person_update/<int:id_user>')
def person_update(id_user):

    record_person = DB.person_select(id_user)

    return render_template('person/update.html', data_person=record_person[0])


@app.route('/update_person', methods=['POST'])
def update_person():
    dict_address = {'address': request.form['address'], 'city': request.form['city'], 'postal_code': request.form['postal_code'], 'country': request.form['country']}

    person_to_update = Person(request.form['name'], request.form['surname'], request.form['phone'], dict_address,
                              request.form['mail'], request.form['url'], request.form['id'])

    DB.person_update(person_to_update)
    filter_sql = Filter()

    lst_person = filter_sql.person_list_filter()

    return render_template('person/list.html', lst_person=lst_person)


@app.route('/add_person', methods=['POST'])
def add_person():

    dict_address = {'address': request.form['address'], 'city': request.form['city'],
                    'postal_code': request.form['postal_code'], 'country': request.form['country']}

    person_to_add = Person(request.form['name'], request.form['surname'], request.form['phone'], dict_address, request.form['mail'], request.form['url'])
    DB.person_insert(person_to_add)
    return render_template('person/new.html')


@app.route('/delete_person/<int:id_user>', methods=['GET'])
def delete_person(id_user):

    DB.person_delete(id_user)
    filter_sql = Filter()

    lst_person = filter_sql.person_list_filter()

    return render_template('person/list.html', lst_person=lst_person)





