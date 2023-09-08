#!/bin/bash
#SBATCH --job-name=trl
#SBATCH --partition=production-cluster
#SBATCH --ntasks=1
#SBATCH --output=slurm/logs/%x_%j.out

srun post_github_comment.py
