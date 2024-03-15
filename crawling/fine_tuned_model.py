import openai
import json

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

json_data = read_json_file("api.json")

openai.api_key = json_data["open_ai_key"]
model = json_data["fine_tuned_model"]
def chat_gpt(prompt, model=model, max_tokens=1024, max_context_tokens=4097, safety_margin=5):
    # Truncate the prompt content to fit within the model's context length
    truncated_prompt = truncate_text(prompt, max_context_tokens - max_tokens - safety_margin)

    response = openai.ChatCompletion.create(model=model,
                                            messages=[{"role": "system", "content": "컴퓨터과학과 게시판"}, {"role": "user", "content": truncated_prompt}])

    return response["choices"][0]["message"]["content"]

def truncate_text(text, max_tokens):
    tokens = text.split()
    if len(tokens) <= max_tokens:
        return text

    return ' '.join(tokens[:max_tokens])
    
print(chat_gpt("기초 교양 뭐 있어?"))