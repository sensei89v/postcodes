import re

from .exceptions import ValidationError
from .uk_rules import (
    _check_first_position,
    _check_second_position,
    _check_third_position,
    _check_fourth_position,
    _check_final_two_letters,
    _check_only_one_double_position,
    _check_zero_district,
    _check_single_digit_district,
    _check_central_london
)
from .uk_special_cases import (
    COMMON_SPECIAL_POST_CODES,
    CAYMAN_ISLANDS_POST_CODES,
    MONSERRAT_POST_CODES,
    BRITISH_VIRGIN_POST_CODES,
    BERMUDA_POST_CODES
)


class PostCodeWorker:
    def validate(self, post_code):
        raise NotImplemented


class EnglandPostCodeWorker(PostCodeWorker):
    _BASIC_POST_CODE = re.compile('^([A-Z]{1,2})([0-9][A-Z0-9]?) ?([0-9])([A-Z]{2})$')
    _GAP = re.compile("\\s+")

    SPECIAL_POST_CODES = COMMON_SPECIAL_POST_CODES | CAYMAN_ISLANDS_POST_CODES | MONSERRAT_POST_CODES | BRITISH_VIRGIN_POST_CODES | BERMUDA_POST_CODES

    RULE_LIST = [
        _check_first_position,
        _check_second_position,
        _check_third_position,
        _check_fourth_position,
        _check_final_two_letters,
        _check_only_one_double_position,
        _check_zero_district,
        _check_single_digit_district,
        _check_central_london,
    ]

    def __init__(self, use_special_cases):
        super().__init__()
        self.use_special_cases = use_special_cases

    def _check_special_cases(self, post_code):
        return post_code in self.SPECIAL_POST_CODES

    def _check_common_cases(self, area, district, sector, unit):
        for rule_fn in self.RULE_LIST:
            if not rule_fn(area, district, sector, unit):
                return False

        return True

    def validate(self, post_code):
        if not isinstance(post_code, str):
            raise ValidationError()

        prepared_post_code = post_code.strip().upper()
        prepared_post_code = self._GAP.sub(' ', prepared_post_code)

        if self.use_special_cases:
            if self._check_special_cases(prepared_post_code):
                return prepared_post_code

        result = self._BASIC_POST_CODE.findall(prepared_post_code)

        if not result:
            raise ValidationError()

        area, district, sector, unit = result[0]
        if self._check_common_cases(area, district, sector, unit):
            return prepared_post_code
        else:
            raise ValidationError()
