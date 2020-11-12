import unittest

from url_scraper import request_to_url, extract_html_tags

class TestRequestToUrl(unittest.TestCase):
    def test_request_with_no_url(self):
        result = request_to_url()
        self.assertIsNone(result)

    def test_request_to_invalid_url(self):
        url = 'http://www.pretend_server.org'
        result = request_to_url(url)
        self.assertIsNone(result)

    def test_request_was_successfull(self):
        url = 'https://www.python.org/'
        result = request_to_url(url)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

class TestExtractHtmlTags(unittest.TestCase):
    def setUp(self):
        url = 'https://www.python.org/'
        self.raw_data = request_to_url(url)

    def test_string_data_is_mandatory(self):
        result_dict = extract_html_tags()
        self.assertIsNone(result_dict)

    def test_get_elements_in_web_page(self):
        result_dict = extract_html_tags(self.raw_data)
        self.assertIsNotNone(result_dict)
        self.assertIsInstance(result_dict.get('total_elements'), int)
        self.assertIsInstance(result_dict.get('top_five'), dict)


if __name__ == '__main__':
    unittest.main()