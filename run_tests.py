import unittest
import HtmlTestRunner

# Discover and load all tests from test files
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add test files to the test suite
suite.addTests(loader.discover(start_dir='.', pattern='test_*.py'))

# Run the test suite and generate an HTML report
runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_name='TestReport', combine_reports=True)
runner.run(suite)
