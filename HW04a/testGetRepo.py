import unittest
import getRepo


class TestGithubAPI(unittest.TestCase):
    def testAPIA(self):
        self.assertEqual(getRepo.get_repo_commits(
            'XuZhou22222'), "Failed to fetch repositories for user XuZhou22222")

    def testAPIB(self):
        self.assertEqual(getRepo.get_repo_commits(
            'XuZhouCS'), "Repo: SSW567-XuZhou  Number of commits: 7")


if __name__ == '__main__':
    unittest.main()
