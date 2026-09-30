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
            ("My IP is 192.168.1.1", "192.168.1.1"),
            ("Server at 8.8.8.8 today", "8.8.8.8"),
            ("IPv6 2001:0db8:85a3:0000:0000:8a2e:0370:7334",
             "2001:0db8:85a3:0000:0000:8a2e:0370:7334"),
            ("short 2001:db8::1", "2001:db8::1"),
        ]

        for text, expected_value in valid_cases:
            results = analyze_text(text, entity_list=['IP_ADDRESS'])
            self.assertEqual(len(results), 1)
            result = results[0]
            self.assertEqual(result.entity_type, 'IP_ADDRESS')
            self.assertEqual(text[result.start:result.end], expected_value)

        invalid_cases = [
            "bad 256.256.256.256",
            "bad 192.168.1",
            "bad 999.1.1.1",
            "bad 2001:db8:::1",
            "no ip here",
        ]

        for text in invalid_cases:
            self.assertEqual(analyze_text(text, entity_list=['IP_ADDRESS']), [])


if __name__ == '__main__':
    unittest.main()
