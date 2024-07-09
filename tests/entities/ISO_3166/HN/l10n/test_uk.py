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

from holidays.entities.ISO_3166.HN import HnHolidays
from tests.common import CommonCountryTests


class TestHnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HnHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер; День Америки"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Велика субота"),
            ("2022-05-01", "День праці"),
            ("2022-09-15", "День незалежності"),
            ("2022-10-05", "Тиждень Морасана"),
            ("2022-10-06", "Тиждень Морасана"),
            ("2022-10-07", "Тиждень Морасана"),
            ("2022-12-25", "Різдво Христове"),
        )
