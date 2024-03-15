import json

# 새로운 JSONL 파일의 이름
new_file_name = "gpt_3.5_turbo_format.jsonl"
gpt_data=[]
# 기존 JSONL 파일 읽기
with open("gpt_data.jsonl", 'r', encoding='UTF-8') as f:
    for line in f:
        gpt_data.append(json.loads(line))

with open(new_file_name, 'w') as json_file:
    for entry in gpt_data:
        json_object = {"messages": [{"role": "system", "content": "컴퓨터과학과 게시판"}, {"role": "user", "content": entry["prompt"]}, {"role": "assistant", "content": entry["completion"]}]}
        json_file.write(json.dumps(json_object, ensure_ascii=False) + '\n')