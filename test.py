import os
from pathlib import Path
from ghapi.all import GhApi
import json

github_context = json.loads(os.environ['GITHUB_CONTEXT'])



status_message = f": Here are the benchmark results"
body = status_message 

repo = github_context["repository"]
owner, repo = repo.split("/") 
# Create a GitHub API instance
api = GhApi(owner=owner, repo=repo, token=github_context["token"])

# Create a comment on the issue
api.issues.create_comment(issue_number=github_context["event"]["issue"]["number"], body=body)
