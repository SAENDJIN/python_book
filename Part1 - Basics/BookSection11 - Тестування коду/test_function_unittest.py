import unittest
from function_for_test import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Тести для 'function_for_test.py'"""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formatted_names = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_names, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
