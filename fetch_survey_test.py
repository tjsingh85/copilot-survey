import unittest
import fetch_survey as fcs

class TestFetchCopilotSurvey(unittest.TestCase):

    def test_get_selected_option(self):
        options = "- [X] Answer1\n- [ ] Answer2"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')

    def test_get_selected_option_with_prefix_space(self):
        options = "- [ X] Answer1\n- [ ] Answer2"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_selected_option_with_suffix_space(self):
        options = "- [X ] Answer1\n- [ ] Answer2"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')

    def test_get_selected_option_with_spaces(self):
        options = "- [ X ] Answer1\n- [ ] Answer2"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_first_selected_options(self):
        options = "- [ X ] Answer1\n- [X] Answer2"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_second_selected_options(self):
        options = "- [ ] Answer1\n- [X] Answer2\n- [ ] Answer3"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'Answer2')

    def test_get_NA_for_no_selected_options(self):
        options = "- [ ] Answer1\n- [ ] Answer2\n- [ ] Answer3"
        result = fcs.get_selected_option(options)
        self.assertEqual(result, 'N/A')


if __name__ == '__main__':
    unittest.main()