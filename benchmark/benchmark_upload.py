from huggingface_hub import HfApi
from typing import List
from dataclasses import dataclass, field
import time
import tyro


@dataclass
class Args:
    tags: List[str] = field(default_factory=lambda: ["no-tag-1-gb906f3d"])
    folder_path: str = "benchmark/trl"
    path_in_repo: str = "images/benchmark"
    repo_id: str = "trl-internal-testing/example-images"
    repo_type: str = "dataset"

args = tyro.cli(Args)
api = HfApi()

api.upload_folder(
    folder_path=args.folder_path,
    path_in_repo=args.path_in_repo,
    repo_id=args.repo_id,
    repo_type=args.repo_type,
)
