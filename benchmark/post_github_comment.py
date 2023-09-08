import argparse
import math
import os
import shlex
import subprocess
import time
import uuid
from distutils.util import strtobool

from ghapi.all import GhApi
import json


def run_experiment(command: str):
    command_list = shlex.split(command)
    print(f"running {command}")
    
    # Use subprocess.PIPE to capture the output
    fd = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = fd.communicate()
    
    return_code = fd.returncode
    assert return_code == 0, f"Command failed with error: {errors.decode('utf-8')}"
    
    # Convert bytes to string and strip leading/trailing whitespaces
    return output.decode('utf-8').strip()

FOLDER_STRING = os.environ.get("FOLDER_STRING", "")
time.sleep(120) # wait for the benchmark to finish
run_experiment("bash benchmark/plot.sh")
folder = f"benchmark/trl/{FOLDER_STRING}"

# Create a GitHub API instance
github_context = json.loads(os.environ['GITHUB_CONTEXT'])
token = os.environ["PERSONAL_ACCESS_TOKEN_GITHUB"] # this needs to refreshed every 12 months
status_message = f"COSTA BOT: Here are the benchmark results"
body = status_message 
repo = github_context["repository"]
owner, repo = repo.split("/")
api = GhApi(owner=owner, repo=repo, token=token)


host_url = "https://huggingface.co/datasets/trl-internal-testing/example-images/resolve/main/images/benchmark/{FOLDER_STRING}"
# for each `.png` file in the folder, add it to the comment
for file in os.listdir(folder):
    if file.endswith(".png"):
        body += f"\n![{file}]({host_url}/{file})"

# Create a comment on the issue
api.issues.create_comment(issue_number=github_context["event"]["issue"]["number"], body=body)