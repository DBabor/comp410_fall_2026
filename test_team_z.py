"""Unit test file for team _z"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam__z(unittest.TestCase):
    """Test team _z PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""
        phone_numbers = [
            "+1 212-555-1234",
            "(415) 555-2671",
            "+44 20 7946 0958",
        ]
        for phone_number in phone_numbers:
            with self.subTest(phone_number=phone_number):
                text = f"Call me at {phone_number}."
                results = analyze_text(text, entity_list=['PHONE_NUMBER'])
                detected = [
                    text[result.start:result.end]
                    for result in results
                    if result.entity_type == 'PHONE_NUMBER'
                ]
                self.assertIn(phone_number, detected)

        for text in ["Call me when you arrive.", "The room number is 42."]:
            with self.subTest(text=text):
                results = analyze_text(text, entity_list=['PHONE_NUMBER'])
                self.assertFalse(any(
                    result.entity_type == 'PHONE_NUMBER' for result in results
                ))

    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
