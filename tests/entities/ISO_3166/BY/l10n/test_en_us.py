#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.BY import ByHolidays
from tests.common import CommonCountryTests


class TestByHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ByHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-03-07", "Day off (substituted from 03/12/2022)"),
            ("2022-03-08", "Women's Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Day off (substituted from 05/14/2022)"),
            ("2022-05-03", "Radunitsa"),
            ("2022-05-09", "Victory Day"),
            ("2022-07-03", "Independence Day (Republic Day)"),
            ("2022-11-07", "October Revolution Day"),
            ("2022-12-25", "Catholic Christmas Day"),
        )
