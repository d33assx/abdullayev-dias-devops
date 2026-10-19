"""Simple checks for the student application."""
import os
import unittest

os.environ.update(STUDENT_NAME="Dias", STUDENT_SURNAME="Abdullayev",
                  STUDENT_GROUP="IT2-2313SE", STUDENT_ID="37240")
import app  # noqa: E402


class BannerTest(unittest.TestCase):
    def test_banner_contains_student_info(self):
        text = app.banner()
        for value in ("Dias", "Abdullayev", "IT2-2313SE", "37240"):
            self.assertIn(value, text)

    def test_banner_reports_success(self):
        self.assertIn("Application is running successfully!", app.banner())


if __name__ == "__main__":
    unittest.main()
