import unittest

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



class TestLeapYear(unittest.TestCase):
    
    def test_leap_year_divisible_by_400(self):
        self.assertTrue(is_leap_year(2000))
    
    def test_leap_year_divisible_by_100_but_not_400(self):
        self.assertFalse(is_leap_year(1900))
    
    def test_leap_year_divisible_by_4_but_not_100(self):
        self.assertTrue(is_leap_year(2016))
    
    def test_not_leap_year_not_divisible_by_4(self):
        self.assertFalse(is_leap_year(2019))

if __name__ == '__main__':
    unittest.main()