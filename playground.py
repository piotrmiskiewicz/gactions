# /// script
# dependencies = [
#     "pygithub",
# ]
# ///


import argparse
import os
from github import Github


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Playground for testing githup API functionality.")
    parser.add_argument(
        "--pr",
        required=True,
        type=int,
        help="PR number",
    )
    parser.add_argument(
        "--organisation",
        required=True,
        type=str,
        help="github organisation.",
    )
    parser.add_argument(
        "--repository",
        required=True,
        type=str,
        help="github repository",
    )
    args = parser.parse_args()
    print(f"Received argument: {args}")

    token = os.getenv("GITHUB_TOKEN")

    gh = Github(token)
    repo = gh.get_repo(f"{args.organisation}/{args.repository}")
    pr = repo.get_pull(args.pr)
    print(f"PR title: {pr.title}")