import unittest
from city_functions import get_city_country


class CityTest(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_city_country('Santiago', 'Chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = get_city_country('Santiago', 'Chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
