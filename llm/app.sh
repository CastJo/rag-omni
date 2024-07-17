CUDA_VISIBLE_DEVICES=0,1 python3 llm_server.py \
    --model_name_or_path /root/autodl-tmp/Qwen1.5-14B-Chat-AWQ \
    --template default \
    --infer_backend vllm \
    --vllm_maxlen 8192