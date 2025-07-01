import unittest

import test_exercise

class TestGuess(unittest.TestCase):
    def test_input(self):
        result = test_exercise.guessing()
        self.assertEqual(result, 'you are a genius!')
