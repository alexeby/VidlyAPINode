from unittest import TestCase
from file_duplicator.common.data_handler import process
from file_duplicator.object.object_mapper import ObjectMapper
from file_duplicator.api_handler import get_api_data

api_result = get_api_data('https://randomuser.me/api/?nat=us&results=1')
person = ObjectMapper(api_result[0]).map_person()


class TestPersonValue(TestCase):
    def test_first_name(self):
        result = process('Person.FirstName', person, None)
        self.assertIsNot(result, '')

    def test_middle_name(self):
        result = process('Person.MiddleName', person, None)
        self.assertIsNot(result, '')

    def test_last_name(self):
        result = process('Person.LastName', person, None)
        self.assertIsNot(result, '')

    def test_full_name(self):
        result = process('Person.FullName', person, None)
        self.assertIsNot(result, '')

    def test_title(self):
        result = process('Person.Title', person, None)
        self.assertIsNot(result, '')

    def test_tax_id(self):
        result = process('Person.TaxId', person, None)
        self.assertIsNot(result, '')

    def test_birth_date(self):
        result = process('Person.BirthDate', person, None)
        self.assertIsNot(result, '')

    def test_age(self):
        result = process('Person.Age', person, None)
        self.assertIsNot(result, '')

    def test_gender(self):
        result = process('Person.Gender', person, None)
        self.assertIsNot(result, '')

    def test_username(self):
        result = process('Person.Username', person, None)
        self.assertIsNot(result, '')

    def test_password(self):
        result = process('Person.Password', person, None)
        self.assertIsNot(result, '')


class TestContactValue(TestCase):
    def test_street(self):
        result = process('Address.Street', person, None)
        self.assertIsNot(result, '')

    def test_ciy(self):
        result = process('Address.City', person, None)
        self.assertIsNot(result, '')

    def test_state(self):
        result = process('Address.State', person, None)
        self.assertIsNot(result, '')

    def test_postal_code(self):
        result = process('Address.PostalCode', person, None)
        self.assertIsNot(result, '')

    def test_zip(self):
        result = process('Address.Zip', person, None)
        self.assertIsNot(result, '')

    def test_country(self):
        result = process('Address.Country', person, None)
        self.assertIsNot(result, '')

    def test_home_phone(self):
        result = process('Address.HomePhone', person, None)
        self.assertIsNot(result, '')

    def test_mobile_phone(self):
        result = process('Address.MobilePhone', person, None)
        self.assertIsNot(result, '')

    def test_email(self):
        result = process('Address.Email', person, None)
        self.assertIsNot(result, '')

    def test_latitude(self):
        result = process('Address.Latitude', person, None)
        self.assertIsNot(result, '')

    def test_longitude(self):
        result = process('Address.Longitude', person, None)
        self.assertIsNot(result, '')


