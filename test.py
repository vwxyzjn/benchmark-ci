import os
from pathlib import Path
from ghapi.all import GhApi
import json
from rich.pretty import pprint
github_context = json.loads(os.environ['GITHUB_CONTEXT'])
pprint(github_context)


status_message = f": Here are the benchmark results"
body = status_message 

# Create a GitHub API instance
api = GhApi()

# Create a comment on the issue
api.issues.create_comment(issue_number=github_context["github.event.issue.number"], body=body)