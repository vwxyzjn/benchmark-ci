python -m openrlbenchmark.rlops_multi_metrics \
    --filters '?we=costa-huang&wpn=cleanrl&ceik=env_id&cen=exp_name&metrics=charts/episodic_return' \
        "ppo$TAGS_STRING" \
    --env-ids CartPole-v1 \
    --check-empty-runs \
    --pc.ncols 2 \
    --pc.ncols-legend 1 \
    --output-filename benchmark/trl/$FOLDER_STRING/0compare \
    --scan-history

python benchmark/benchmark_upload.py \
    --folder_path="benchmark/trl/$FOLDER_STRING" \
    --path_in_repo="images/benchmark/$FOLDER_STRING" \
    --repo_id="trl-internal-testing/example-images" \
    --repo_type="dataset"
