
# Local imports
from webasic.models.database import DataBase, SQLITE

DB = DataBase(SQLITE, dbname='webasic/database/webasic_db.db')


class Person:
    """
    Class person which binds with Database table
    """

    def __init__(self, name, surname, phone, address, mail, url=None, identifier=-1):
        self._identifier = identifier
        self._name = name
        self._surname = surname
        self._phone = phone
        self._address = address
        self._mail = mail
        self._url = url

    @property
    def identifier(self):
        """
        Get the identifier of person
        :return:
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier

    @property
    def name(self):
        """
        Get the name of person
        :return:
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        """
        Get the surname of person
        :return:
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def phone(self):
        """
        Get the phone of person
        :return:
        """

        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address(self):
        """
        Get the address of person
        :return:
        """

        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def mail(self):
        """
        Get the mail of person
        :return:
        """

        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def url(self):
        """
        Get the url of person
        :return:
        """
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def __str__(self):
        clase = type(self).__name__

        msg = "{0} de name {1} and surname {2}"
        return msg.format(clase, self.name, self.surname)


class Filter(Person):
    """
    Class to define filters from data base
    """

    def __init__(self, name=None, surname=None, phone=None, address=None, mail=None, url=None, identifier=-1):
        self._identifier = identifier
        self._name = name
        self._surname = surname
        self._phone = phone
        self._address = address
        self._mail = mail
        self._url = url

    def person_list_filter(self):

        lst_person = DB.person_list(self)
        return lst_person

    def __str__(self):
        class_name = type(self).__name__

        msg = "{0} of name {1} and surname {2}"
        return msg.format(class_name, self.name, self.surname)
