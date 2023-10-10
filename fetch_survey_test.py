import unittest
import fetch_survey as fs

class TestFetchCopilotSurvey(unittest.TestCase):

    def test_get_selected_option(self):
        options = "- [X] Answer1\n- [ ] Answer2"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')

    def test_get_selected_option_with_prefix_space(self):
        options = "- [ X] Answer1\n- [ ] Answer2"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_selected_option_with_suffix_space(self):
        options = "- [X ] Answer1\n- [ ] Answer2"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')

    def test_get_selected_option_with_spaces(self):
        options = "- [ X ] Answer1\n- [ ] Answer2"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_first_selected_options(self):
        options = "- [ X ] Answer1\n- [X] Answer2"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer1')
    
    def test_get_second_selected_options(self):
        options = "- [ ] Answer1\n- [X] Answer2\n- [ ] Answer3"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'Answer2')

    def test_get_NA_for_no_selected_options(self):
        options = "- [ ] Answer1\n- [ ] Answer2\n- [ ] Answer3"
        result = fs.get_selected_option(options)
        self.assertEqual(result, 'N/A')

    def test_get_answers(self):
        data = "***Question***\n- [X] Answer\n***"
        result = fs.get_answers(data)
        self.assertEqual(result, {'Question': 'Answer'})
    
    def test_get_NA_as_answer_when_nothing_is_selected(self):
        data = "***Question***\n- [ ] Answer\n***"
        result = fs.get_answers(data)
        self.assertEqual(result, {'Question': 'N/A'})

    def test_get_first_answer_if_mulitple_answers_are_selected(self):
        data = "***Question***\n- [X] Answer1\n- [X] Answer2***"
        result = fs.get_answers(data)
        self.assertEqual(result, {'Question': 'Answer1'})

if __name__ == '__main__':
    unittest.main()