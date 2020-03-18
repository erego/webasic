# Core imports
import sqlite3
import os

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
# Global Variables
SQLITE = 'sqlite'

# Table Names
PERSONS = 'Person'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "database", "webasic_db.db")


class DataBase:

    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(PERSONS, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('Name', String),
                      Column('Surname', String),
                      Column('Phone', Integer),
                      Column('Address', String),
                      Column('City', String),
                      Column('Postal_code', Integer),
                      Column('Country', String),
                      Column('Mail', String),
                      Column('URL', String),
                      )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return None

        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                return None

        return True

    def select_data(self, query=''):
        query = query if query != '' else "SELECT * FROM Person;"
        lst_result = []
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    lst_result.append(row)
                result.close()
        return tuple(lst_result)

    def person_insert(self, person):
        """
        Insert person registry into person datatable
        :param person: Person object
        :return: True if success, None otherwise
        """

        query_to_execute = '''INSERT INTO Person(Name, Surname, Phone, Address, City, Postal_code, Country, Mail, URL )
                                    VALUES('{}', '{}', {}, '{}', '{}', {}, '{}', '{}', '{}')'''.format(
            person.name, person.surname, person.phone, person.address['address'],
            person.address['city'], person.address['postal_code'],
            person.address['country'], person.mail, person.url)

        result = self.execute_query(query_to_execute)

        return result

    def person_update(self, person):
        """
        Update person registry from person datatable
        :param person: Person object
        :return:
        """

        query_to_execute = '''UPDATE Person SET Name='{}', Surname='{}', Phone='{}', Address='{}', City='{}', Postal_code='{}', Country='{}', Mail='{}', URL='{}'
                            WHERE Id ="{}"'''.format(person.name, person.surname, person.phone,
                                                     person.address['address'],
                                                     person.address['city'], person.address['postal_code'],
                                                     person.address['country'], person.mail, person.url, person.identifier)

        result = self.execute_query(query_to_execute)

        return result

    def person_list(self, filter_sql):

        """
        Return a list of people who match the filter conditions
        :param filter_sql: filter for sql query
        :return: result of query
        """
        sql_select = "SELECT * FROM Person WHERE 1=1"
        if filter_sql.name is not None and filter_sql.name != "":
            sql_select += " AND Name='" + filter_sql.name + "'"

        if filter_sql.surname is not None and filter_sql.surname != "":
            sql_select += " AND Surname=" + filter_sql.surname + "'"

        result = self.select_data(sql_select)

        return result

    def person_table_delete(self):

        query_to_execute = '''DELETE FROM Person '''

        self.execute_query(query_to_execute)

    def person_delete(self, id_person):

        query_to_execute = '''DELETE FROM Person WHERE Id = {}'''.format(id_person)
        self.execute_query(query_to_execute)

    def person_select(self, id_person):

        sql_select = '''SELECT * FROM Person WHERE Id = {}'''.format(id_person)

        result = self.select_data(sql_select)

        return result
