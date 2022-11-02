import unittest

from function_test_ex import city_country, city_country_population


class CitiesTestCase(unittest.TestCase):
    """Test for 'city_country' """

    def test_city_country(self):
        """Тест на перевірку правильного стрінга"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()


class CitiesTestPopulationCase(unittest.TestCase):
    """Test for 'city_country_population' """

    def test_city_country_population(self):
        """Тест на перевірку правильного стрінга"""
        santiago_chile = city_country_population('santiago', 'chile', population=5000)
        self.assertEqual(santiago_chile, "Santiago, Chile - 5000")


if __name__ == '__main__':
    unittest.main()
