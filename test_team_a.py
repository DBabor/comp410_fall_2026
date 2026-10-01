"""Unit test file for team _a"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam__a(unittest.TestCase):
    """Test team _a PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""
        # --- POSITIVE TESTS (Should detect as US_BANK_NUMBER) ---

        # Valid 10-digit account number with context
        text_10deg = "My direct deposit bank account number is 1234567890"
        results_10deg = analyze_text(text_10deg, ['US_BANK_NUMBER'])
        self.assertEqual(len(results_10deg), 1)
        self.assertEqual(results_10deg[0].entity_type, 'US_BANK_NUMBER')

        # Valid 12-digit account number with routing/account context
        text_12deg = "Transfer funds to routing/account number 987654321012"
        results_12deg = analyze_text(text_12deg, ['US_BANK_NUMBER'])
        self.assertEqual(len(results_12deg), 1)
        self.assertEqual(results_12deg[0].entity_type, 'US_BANK_NUMBER')


        # --- NEGATIVE TESTS (Should NOT detect as US_BANK_NUMBER) ---

        # Plain text
        text_plain = "TEST normal text"
        results_plain = analyze_text(text_plain, ['US_BANK_NUMBER'])
        self.assertEqual(len(results_plain), 0)

        # Short number string
        text_short = "TEST short number 123"
        results_short = analyze_text(text_short, ['US_BANK_NUMBER'])
        self.assertEqual(len(results_short), 0)

        # Phone number not a bank account
        text_phone = "Call our customer service team at 800-555-0199"
        results_phone = analyze_text(text_phone, ['US_BANK_NUMBER'])
        self.assertEqual(len(results_phone), 0)

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
