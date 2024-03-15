import openai
import json

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

json_data = read_json_file("api.json")

openai.api_key = json_data["open_ai_key"]

training_response=openai.File.create(
    file=open("gpt_3.5_turbo_format.jsonl","rb"),
    purpose="fine-tune"
)

json_data["file_id"]=training_response["id"]

with open("api.json", 'w') as json_file:
    json.dump(json_data, json_file, indent=4)  # indent를 사용하여 가독성을 높일 수 있음
