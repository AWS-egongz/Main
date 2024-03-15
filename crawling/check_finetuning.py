import openai
import json
import time

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

json_data = read_json_file("api.json")
openai.api_key = json_data["open_ai_key"]
id = json_data["job_id"]

while openai.FineTuningJob.retrieve(id).fine_tuned_model==None:
    time.sleep(10)

json_data["fine_tuned_model"]=openai.FineTuningJob.retrieve(id).fine_tuned_model

with open("api.json", 'w') as json_file:
    json.dump(json_data, json_file, indent=4)  # indent를 사용하여 가독성을 높일 수 있음

print(json_data["fine_tuned_model"])
