job_ids=$(bash benchmark/benchmark.sh | grep "Job ID" | awk '{print $NF}' | paste -sd: -)
sbatch --dependency=afterany:$job_ids benchmark/post_github_comment.sbatch
