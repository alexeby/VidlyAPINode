from .exception.exception import InvalidTokenException, NonUniqueMappingException
from .object.person import Person
from .common.constants import Constants as c
import logging
from .common import file_utils
from .setup.mappings import Mappings as m

logger = logging.getLogger(__name__)


class Validate:
    def __init__(self, left_token_trim, right_token_trim, all_unique_persons):
        self.left_token_trim = left_token_trim
        self.right_token_trim = right_token_trim
        self.all_unique_persons = all_unique_persons

        self.current_person = Person()
        self.unique_person_keys = set()

    # Validate mappings
    @staticmethod
    def validate_mappings():
        mappings = m.MAPPINGS
        for i in range(len(mappings)):
            mapping = mappings.pop()
            if mapping in mappings:
                logger.error(f'"{mapping}" is not a unique mapping. Mappings are not case sensitive')
                raise NonUniqueMappingException(mapping)
        logger.info('Mapping validation complete. All mappings are unique.')
        return m.MAPPINGS

    def retrieve_unique_person_keys(self, token: str):
        if token.upper().startswith(c.person) or token.upper().startswith(c.address):
            pair = token.upper().replace(c.person, '').replace(c.address, '').split('.')
            key = pair[0]
            value = pair[1]
            if value not in m.MAPPINGS:
                raise InvalidTokenException(value)
            if self.all_unique_persons.upper() == 'TRUE':
                number_keys = len(self.unique_person_keys)
                self.unique_person_keys.add(str(number_keys))
            else:
                self.unique_person_keys.add(key)

    def parse_nested_tokens(self, s: str):
        right_token_index = 0
        left_token_index = 0
        iteration = 0

        for i in s:
            if i == self.left_token_trim:
                left_token_index = iteration
            if i == self.right_token_trim:
                right_token_index = iteration
                break
            iteration += 1
        if right_token_index == 0 and left_token_index == 0:
            return s

        token = s[left_token_index:right_token_index + 1]
        formatted_result = token.replace(self.left_token_trim, '').replace(self.right_token_trim, '')
        self.retrieve_unique_person_keys(formatted_result)
        replace = file_utils.get_token_value(formatted_result, self.current_person)
        s = s.replace(token, replace, 1)
        return self.parse_nested_tokens(s)

    def validate_file(self, original_file_dir: str):
        original_file_name = file_utils.get_file_name(original_file_dir)
        original_file_path = original_file_dir + original_file_name

        with open(original_file_path, 'r') as original_file:
            line_number = 1
            logger.info('Validating file.')
            for line in original_file:
                try:
                    self.parse_nested_tokens(line)
                except InvalidTokenException as ite:
                    logger.error(f'{ite.token} on line {line_number} is not a recognized token. Exiting program.')
                    logger.error(ite.additional_except)
                    return False
                line_number += 1
            logger.info('File passed validation.')
            original_file.close()
            return True
