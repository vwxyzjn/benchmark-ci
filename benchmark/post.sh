# job_ids="430592,430593"
regex_ids=$(echo $job_ids | tr ',' '|')
echo $regex_ids

while squeue -j $job_ids | grep -qE "$regex_ids"; do
    echo "waiting for jobs to finish"
    sleep 10
done

python benchmark/post_github_comment.py