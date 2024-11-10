# test_vote_counter.py

import unittest
from unittest.mock import patch, mock_open
from vote_counter import count_votes  # Assuming starter version is in `vote_counter.py`

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Expected output after tallying votes
        mock_print.assert_any_call("Alice: 3200 votes")
        mock_print.assert_any_call("Bob: 3250 votes")
        self.assertEqual(mock_print.call_count, 2)

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simulate a CSV file with invalid votes data
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Expect Alice to be skipped due to invalid data, only Bob's votes should print correctly
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Alice: 2000 votes")
        self.assertEqual(mock_print.call_count, 2)

if __name__ == "__main__":
    unittest.main()

