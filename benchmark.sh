python benchmark/benchmark.py \
    --command "poetry run python test_ci/ppo.py --total-timesteps 10000 --track" \
    --num-seeds 5 \
    --start-seed 1 \
    --workers 10 \
    --slurm-nodes 1 \
    --slurm-gpus-per-task 1 \
    --slurm-ntasks 1 \
    --slurm-total-cpus 12 \
    --slurm-template-path benchmark/trl.slurm_template
