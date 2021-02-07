import unittest
import math
import statistics

from PyTechnicalIndicators.Single import basic_indicators


# noinspection PyArgumentList
class TestBasicIndicators(unittest.TestCase):

    def setUp(self):
        self.prices = [100, 101, 102, 101, 103, 100]

    def test_log(self):
        log = basic_indicators.log(100)
        expected_log = math.log(100)
        self.assertEqual(log, expected_log)

    def test_log_failure(self):
        with self.assertRaises(Exception, msg='There needs to be a price to log'):
            basic_indicators.log()

    def test_log_diff(self):
        log_diff = basic_indicators.log_diff(104, 100)
        expected_diff = math.log(104) - math.log(100)
        self.assertEqual(log_diff, expected_diff)

    def test_log_diff_failure(self):
        with self.assertRaises(Exception, msg='There needs to be two prices to be able to do a diff'):
            basic_indicators.log_diff(100)

    def test_stdev(self):
        stdev = basic_indicators.stddev(self.prices)
        expected_stdev = statistics.stdev(self.prices)
        self.assertEqual(stdev, expected_stdev)

    def test_stdev_failure(self):
        with self.assertRaises(Exception, msg='There needs to be prices to be able to calculate a stddev'):
            basic_indicators.stddev()

    def test_mean(self):
        mean = basic_indicators.mean(self.prices)
        expected_mean = statistics.mean(self.prices)
        self.assertEqual(mean, expected_mean)

    def test_mean_failure(self):
        with self.assertRaises(Exception, msg='There needs to be prices to be able to calculate a mean'):
            basic_indicators.mean()

    def test_median(self):
        median = basic_indicators.median(self.prices)
        expected_median = statistics.median(self.prices)
        self.assertEqual(median, expected_median)

    def test_median_failure(self):
        with self.assertRaises(Exception, msg='There needs to be prices to be able to calculate a median'):
            basic_indicators.median()

    def test_variance(self):
        var = basic_indicators.variance(self.prices)
        expected_var = statistics.variance(self.prices)
        self.assertEqual(var, expected_var)

    def test_variance_failure(self):
        with self.assertRaises(Exception, msg='There needs to be prices to be able to calculate a variance'):
            basic_indicators.variance()


if __name__ == '__main__':
    unittest.main()
