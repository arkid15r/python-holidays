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

from holidays.entities.ISO_3166.MZ import MzHolidays
from tests.common import CommonCountryTests


class TestMzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MzHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "День всесвітнього братерства"),
            ("2023-01-02", "День всесвітнього братерства (вихідний)"),
            ("2023-02-03", "День героїв Мозамбіку"),
            ("2023-04-07", "День жінок Мозамбіку"),
            ("2023-05-01", "Міжнародний день трудящих"),
            ("2023-06-25", "День національної незалежності"),
            ("2023-06-26", "День національної незалежності (вихідний)"),
            ("2023-09-07", "День перемоги"),
            ("2023-09-25", "День Збройних сил національного визволення"),
            ("2023-10-04", "День миру та примирення"),
            ("2023-12-25", "День родини"),
        )
