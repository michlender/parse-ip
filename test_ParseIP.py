#!/usr/bin/env python2

import unittest
from ParseIP import parse_IP

class TestParseIP(unittest.TestCase):

    def test_to_from(self):
        string = 'FROM 172.16.0.0  TO  172.31.255.255'
        expect = "172.16.0.0-172.31.255.255\n"
        got = parse_IP(string)
        self.assertEqual(expect, got)

    def test_multiple_to_from(self):
        string = "FROM 127.0.0.0 TO 127.0.0.0 FROM 127.0.0.3 TO 127.0.0.4"
        expect = "127.0.0.0-127.0.0.0\n127.0.0.3-127.0.0.4\n"
        got = parse_IP(string)
        self.assertEqual(expect, got)

    def test_multiple_symbol(self):
        string = "127.0.0.0 ~ 127.0.0.1 , 127.0.0.3 ~ 127.0.0.4"
        expect = "127.0.0.0-127.0.0.1\n127.0.0.3-127.0.0.4\n"
        got = parse_IP(string, delimiter='~')
        self.assertEqual(expect, got)

    def test_spaces_mult_to_from(self):
        string = "FROM 127.0.0.1 TO   127.0.0.2    0.0.0.3 FROM 0.0.0.4 TO 0.0.0.5"
        expect = "127.0.0.1-127.0.0.2\n0.0.0.3\n0.0.0.4-0.0.0.5\n"
        got = parse_IP(string)
        self.assertEqual(expect, got)

    def test_emmy_given(self):
        string = "FROM 172.16.0.0   TO   172.31.255.255 FROM 175.16.0.0 TO   175.17.255.255 175.18.4.4  175.18.4.8  FROM 177.16.0.0 TO   192.135.11.255"
        expect = "172.16.0.0-172.31.255.255\n175.16.0.0-175.17.255.255\n175.18.4.4\n175.18.4.8\n177.16.0.0-192.135.11.255\n"
        got = parse_IP(string)
        self.assertEqual(expect, got)

    def test_multiple_tilde_no_space(self):
        string = "127.0.0.0 ~ 127.0.0.1 , 127.0.0.3 ~ 127.0.0.4"
        expect = "127.0.0.0-127.0.0.1\n127.0.0.3-127.0.0.4\n"
        got = parse_IP(string, delimiter='~')
        self.assertEqual(expect, got)

    def test_to_from_no_space(self):
        string = 'FROM172.16.0.0TO172.31.255.255'
        expect = "172.16.0.0-172.31.255.255\n"
        got = parse_IP(string)
        self.assertEqual(expect, got)



if __name__ == '__main__':
    unittest.main()
