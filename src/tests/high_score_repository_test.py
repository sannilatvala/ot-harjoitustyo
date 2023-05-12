import os
import sqlite3
import unittest
from repositories.high_score_repository import HighScoreRepository
from database.initialize_database import create_tables


class TestHighScoreRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, "highscorestest.db")
        self.connection = sqlite3.connect(filepath)
        self.high_score_repository = HighScoreRepository()
        self.high_score_repository._connection = self.connection
        create_tables(self.connection)
        self.high_score_repository.delete_all()
        self.user = "user"
        self.score = 10

    def test_find_by_username(self):
        self.high_score_repository._connection = self.connection
        self.high_score_repository.create_user(self.user)

        user_highscores = self.high_score_repository.find_by_username(
            self.user)

        self.assertEqual(len(user_highscores), 2)
        self.assertEqual(user_highscores, (self.user, 0))

    def test_create_user(self):
        self.high_score_repository._connection = self.connection
        username = self.high_score_repository.create_user(self.user)
        self.assertEqual(username, self.user)
        username = self.high_score_repository.create_user(self.user)
        self.assertIsNone(username)

    def test_update_highscore(self):
        self.high_score_repository._connection = self.connection
        self.high_score_repository.create_user(self.user)
        score = self.high_score_repository.update_highscore(
            self.score, self.user)
        self.assertEqual(score, self.score)
        score = self.high_score_repository.update_highscore(5, self.user)
        self.assertEqual(score, self.score)

    def test_find_highest_highscores(self):
        self.high_score_repository._connection = self.connection
        self.high_score_repository.create_user(self.user)
        highscores = self.high_score_repository.find_highest_highscores()
        self.assertEqual(highscores, [(self.user, 0)])

    def test_check_if_username_exist(self):
        self.high_score_repository._connection = self.connection
        self.assertTrue(
            self.high_score_repository.check_if_username_exist(self.user))
        self.high_score_repository.create_user(self.user)
        self.assertFalse(
            self.high_score_repository.check_if_username_exist(self.user))
