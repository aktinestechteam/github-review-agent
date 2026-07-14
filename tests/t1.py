from github import Github
import os
from dotenv import load_dotenv

#Load Environment
load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

for repo in g.get_user().get_repos():
    print(repo.full_name)

