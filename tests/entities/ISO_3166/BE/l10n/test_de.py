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

from holidays.entities.ISO_3166.BE import BeHolidays
from tests.common import CommonCountryTests


class TestBeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BeHolidays, language="de")

    def test_de(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostern"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-05-27", "Freitag nach Christi Himmelfahrt"),
            ("2022-06-05", "Pfingsten"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-07-21", "Nationalfeiertag"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Waffenstillstand"),
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Bankschlusstag"),
        )
