from openai import OpenAI
import os

# OpenAI APIキーを設定
api_key = ""  # 取得したAPIキーをここに入力
os.environ['OPENAI_API_KEY'] = api_key

client = OpenAI()

# 事前プロンプトを設定
def generate_response(user_input):
    prompt = f"""
Please give me an example sentence for each English word I say and the Japanese translation of that sentence.
**Condition**
A sentence that usually consists of a single sentence and includes a subject and a predicate.
Entered English words:{user_input}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # または "gpt-4" モデルを指定
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message["content"].strip()

if __name__ == '__main__':
    # ユーザーの入力を受け取る
    user_input = input("入力してください: ")
    output = generate_response(user_input)
    print("出力:", output)
