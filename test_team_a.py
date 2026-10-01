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
        # Positive test: Normal HTTPS URL with query para
        text_query = "User logged in with https://auth.domain.com/login?token=abc123secret"
        results_query = analyze_text(text_query, ['URL'])
        self.assertEqual(len(results_query), 1)
        self.assertEqual(results_query[0].entity_type, 'URL')

        # Positive test: HTTP URL with non-standard port
        text_port = "Access the dashboard at http://localhost:8080/metrics"
        results_port = analyze_text(text_port, ['URL'])
        self.assertEqual(len(results_port), 1)
        self.assertEqual(results_port[0].entity_type, 'URL')

        # Positive test: FTP scheme
        text_ftp = "Download the archive from ftp://files.internal.net/pub/data.zip"
        results_ftp = analyze_text(text_ftp, ['URL'])
        self.assertEqual(len(results_ftp), 1)
        self.assertEqual(results_ftp[0].entity_type, 'URL')

        # Negative tesst: Text without web links
        text_neg = "Testing Text"
        results_neg = analyze_text(text_neg, ['URL'])
        self.assertEqual(len(results_neg), 0)

        # Negative test: Domain mention without a scheme protocol (e.g., standard text)
        text_neg_domain = "Test Text #2"
        results_neg_domain = analyze_text(text_neg_domain, ['URL'])
        self.assertEqual(len(results_neg_domain), 0)

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
