python -m openrlbenchmark.rlops_multi_metrics \
    --filters '?we=costa-huang&wpn=cleanrl&ceik=env_id&cen=exp_name&metrics=charts/episodic_return' \
        "ppo?tag=$TAG" \
    --env-ids CartPole-v1 \
    --no-check-empty-runs \
    --pc.ncols 2 \
    --pc.ncols-legend 1 \
    --output-filename benchmark/trl/$TAG/0compare \
    --scan-history

python benchmark/benchmark_upload.py \
    --folder_path="benchmark/trl/$TAG" \
    --path_in_repo="images/benchmark/$TAG" \
    --repo_id="trl-internal-testing/example-images" \
    --repo_type="dataset"