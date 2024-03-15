import openai
import json

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

json_data = read_json_file("api.json")

openai.api_key = json_data["open_ai_key"]
model = "gpt-3.5-turbo-0301"

# JSON 파일 경로 설정
json_file_path = 'new_data.json'

def chat_gpt(prompt, model="gpt-3.5-turbo", max_tokens=1024, max_context_tokens=4097, safety_margin=5):
    # Truncate the prompt content to fit within the model's context length
    truncated_prompt = truncate_text(prompt, max_context_tokens - max_tokens - safety_margin)

    response = openai.ChatCompletion.create(model=model,
                                            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": truncated_prompt}])

    return response["choices"][0]["message"]["content"]

def truncate_text(text, max_tokens):
    tokens = text.split()
    if len(tokens) <= max_tokens:
        return text

    return ' '.join(tokens[:max_tokens])

finetuning_data=[]

# JSON 파일을 한 줄씩 읽어 ChatGPT 3.5 API에 요청을 보내고 결과를 출력
with open(json_file_path, 'r') as file:
    for line in file:
        try:
            data = json.loads(line)
            prompt = str(data)+'위 데이터를 요약해서 prompt에는 질문에 대한걸 요약하고 completion에는 comments나 detail에 대한걸 요약해줘 출력형태는 다음과 같아. 출력형태 = {"prompt" : " ", "completion" : " "} 형태로 요약해줘'

            # 토큰 수 계산
            tokens = prompt.split()
            if len(tokens) > 4097:  # 만약 토큰 수가 4097을 초과하면 무시
                continue
            
            result_data=json.loads(chat_gpt(prompt))
            
            json_object = {
                "prompt": result_data["prompt"],
                "completion": result_data["completion"]
            }
            
            finetuning_data.append(json_object)
        except Exception as e:
            print(f"An error occurred: {e}")

with open("gpt_data.jsonl", 'w', encoding='UTF-8') as f:
    for data in finetuning_data:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')