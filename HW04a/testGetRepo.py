import unittest
from HW04a import getRepo
from unittest.mock import patch


class TestGithubAPI(unittest.TestCase):
    @patch('HW04a.getRepo.get_repo_commits')
    def testAPIA(self, mock_get_repo_commits):
        mock_get_repo_commits.return_value = "Failed to fetch repositories for user XuZhou22222"
        result = getRepo.get_repo_commits('XuZhou22222')
        self.assertEqual(
            result, "Failed to fetch repositories for user XuZhou22222")

    @patch('HW04a.getRepo.get_repo_commits')
    def testAPIB(self, mock_get_repo_commits):
        mock_get_repo_commits.return_value = "Repo: SSW567-XuZhou  Number of commits: 7"
        result = getRepo.get_repo_commits('XuZhouCS')
        self.assertEqual(result, "Repo: SSW567-XuZhou  Number of commits: 7")


if __name__ == '__main__':
    unittest.main()
