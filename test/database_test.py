
# Standard library imports
import unittest

import os

# Local imports
from webasic.models.database import DataBase, SQLITE
from webasic.models.person import Person


class DataBaseTest(unittest.TestCase):
    db = None

    @classmethod
    def setUpClass(cls):
        if os.path.exists('test.sqlite'):
            try:
                os.remove('test.sqlite')
            except:
                pass
        DataBaseTest.db = DataBase(SQLITE, dbname='test.sqlite')
        DataBaseTest.db.create_db_tables()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('test.sqlite')
        except:
            pass

    # Test insert data base
    def test_insert_database_correct(self):

        dict_address = {'address': 'Test', 'city': 'Test', 'postal_code': 111, 'country': 'Test'}

        person_to_test = Person("PersonTest", "SurnameTest", 111, dict_address, 'test@test.com', 'www.test.es')

        result = DataBaseTest.db.person_insert(person_to_test)

        self.assertTrue(result)

        query_to_execute = '''SELECT Name, Surname FROM Person WHERE Name ="{}"'''.format(
            person_to_test.name)

        result = DataBaseTest.db.select_data(query_to_execute)

        first_result = result[0]
        self.assertEqual(first_result[0], "PersonTest")
        self.assertEqual(first_result[1], "SurnameTest")

    # Test insert data base

    def test_insert_database_incorrect(self):
        dict_address = {'address': 'Test', 'city': 'Test', 'postal_code': 111, 'country': 'Test'}

        person_to_test = Person("PersonTest", "SurnameTest", "a", dict_address, 'test@test.com', 'www.test.es')

        result = DataBaseTest.db.person_insert(person_to_test)

        self.assertIsNone(result)

    # Test update data base
    def test_update_database_correct(self):

        dict_address = {'address': 'Amazonas 2', 'city': 'Alcorcon', 'postal_code': 28922, 'country': 'spain'}

        person_to_find = Person("PersonTest", "SurnameTest", 111, dict_address, 'test@test.com', 'www.test.es')
        person = Person("NameTest", "SurnameTest", 222, dict_address, 'test@test.com', 'www.test.es')

        query_to_execute = '''SELECT Id, Name, Surname FROM Person WHERE Name ="{}"'''.format(
            person_to_find.name)

        result = DataBase.select_data(self.db, query_to_execute)

        record = result[0]
        person.identifier = record[0]

        result = DataBaseTest.db.person_update(person)

        self.assertTrue(result)

        query_to_execute = '''SELECT Name, Surname FROM Person WHERE Name ="{}"'''.format(person.name)

        result = DataBase.select_data(self.db, query_to_execute)

        first_result = result[0]
        self.assertEqual(first_result[0], "NameTest")
        self.assertEqual(first_result[1], "SurnameTest")

