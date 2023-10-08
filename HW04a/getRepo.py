import requests
import json

BASE_URL = "https://api.github.com/users/"
COMMIT_URL = "https://api.github.com/repos/"


def fetch_repos(username, session):
    repo_url = BASE_URL + f'{username}/repos'
    response = session.get(repo_url)
    response.raise_for_status()
    return response.json()


def fetch_commits(username, repo_name, session):
    commits_url = COMMIT_URL + f'{username}/{repo_name}/commits'
    response = session.get(commits_url)
    response.raise_for_status()
    return response.json()


def get_repo_commits(username):
    with requests.Session() as session:
        try:
            repos = fetch_repos(username, session)
        except requests.RequestException:
            return "Failed to fetch repositories for user " + username

        commits_data = []
        for repo in repos:
            try:
                repo_name = repo['name']
                commits = fetch_commits(username, repo_name, session)
                commits_data.append(
                    f'Repo: {repo_name}  Number of commits: {len(commits)}')
            except requests.RequestException:
                return f"Failed to fetch the commits for repository {repo_name}"

    return commits_data


def main():
    user = input("Please enter Github username: ")
    result = get_repo_commits(user)
    for line in result:
        print(line)


if __name__ == '__main__':
    main()
