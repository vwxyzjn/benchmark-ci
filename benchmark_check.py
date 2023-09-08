from collections import defaultdict
from typing import List
import wandb
from rich.pretty import pprint
from dataclasses import dataclass, field
import time
api = wandb.Api()
import tyro


@dataclass
class Args:
    tags: List[str] = field(default_factory=lambda: ["no-tag-1-gb906f3d"])
    num_expected: int = 5
    wait_time: int = 60

args = tyro.cli(Args)
runs = api.runs(
    "costa-huang/cleanrl",
    filters={
        "$and": [
            {"tags": {"$in": args.tags}},
        ]
    }
)
states = defaultdict(list)
all_finished = False
while not all_finished:
    for run in runs:
        if run.state == "running":
            print(f"Skipping running run: {run}")
            continue
        states[run.state].append(run.url)
    if len(states["finished"]) + len(states["failed"]) + len(states["killed"]) + len(states["crashed"]) == args.num_expected:
        all_finished = True
    print(states)

print("all finished")
