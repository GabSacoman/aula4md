from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
      def test_can_start_a_list_for_one_user(self):
        # Test that a user can start a list
        user = "John"
        list_item = "Buy milk"

        self.assertIn(list_item, user_list)
        self.assertEqual(len(user_list), 1)

        def test_multiple_users_can_start_lists_at_different_urls(self):
            # Test that multiple users can start lists at different URLs
            user1 = "John"
            user2 = "Jane"
            list_item1 = "Buy milk"
            list_item2 = "Walk the dog"

            self.assertIn(list_item1, user1_list)
            self.assertIn(list_item2, user2_list)
            self.assertEqual(len(user1_list), 1)
            self.assertEqual(len(user2_list), 1)