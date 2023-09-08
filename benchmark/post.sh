# job_ids="430592,430593"
regex_ids=$(echo $job_ids | tr ',' '|')

echo got $job_ids
echo $regex_ids

while squeue -j $job_ids | grep -qE "$regex_ids"; do
    sleep 10
    echo "waiting for jobs to finish"
done

python benchmark/post_github_comment.py