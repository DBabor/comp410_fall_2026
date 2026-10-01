"""Unit test file for team _1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam__1(unittest.TestCase):
    """Test team _1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        """Test ES_NIE functionality"""

    def test_es_nif(self):
        """Test ES_NIF functionality"""

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""
        valid_cases = [
            ("Login failed for user from IP 203.0.113.42",
             "203.0.113.42", 0.95),
            ("Allow traffic from 198.51.100.0/24", "198.51.100.0/24", 0.6),
            ("Client connected via 2001:db8:85a3::8a2e:370:7334",
             "2001:db8:85a3::8a2e:370:7334", 0.6),
            ("ipv6 loopback is ::1", "::1", 0.95),
            ("Mapped address ::ffff:192.0.2.10", "::ffff:192.0.2.10", 0.6),
        ]

        for text, expected_value, expected_score in valid_cases:
            results = analyze_text(text, entity_list=['IP_ADDRESS'])
            self.assertEqual(len(results), 1)
            result = results[0]
            self.assertEqual(result.entity_type, 'IP_ADDRESS')
            self.assertEqual(text[result.start:result.end], expected_value)
            self.assertAlmostEqual(result.score, expected_score)

        invalid_cases = [
            "Octet out of range: 256.1.1.1",
            "Only three parts: 192.0.2",
            "Bad IPv6 2001:db8::1::2",
            "The meeting started at 12:30:45",
            "Visit example.com",
        ]

        for text in invalid_cases:
            self.assertEqual(analyze_text(text, entity_list=['IP_ADDRESS']), [])


if __name__ == '__main__':
    unittest.main()
