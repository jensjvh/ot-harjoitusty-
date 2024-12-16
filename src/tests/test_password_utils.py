import unittest
from utils.password_utils import hash_password, verify_password


class TestPasswordUtils(unittest.TestCase):
    def setUp(self):
        self.password = "password123"
        self.hashed_password = hash_password(self.password)
    
    def test_hash_password(self):
        self.assertNotEqual(self.password, self.hashed_password)

    def test_verify_password(self):
        self.assertTrue(verify_password(self.hashed_password, self.password))

    def test_verify_password_incorrect(self):
        self.assertFalse(verify_password(self.hashed_password, "wrongpassword"))