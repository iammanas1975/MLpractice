import os
import openai
client = openai.OpenAI()
openai.api_key = os.environ['OPENAI_API_KEY']

completion = client.chat.completions.create(
	model = "gpt-3.5-turbo",
	messages = [
		{"role": "system", "content": "you are a poetic assistant, skilled in explaining complex concepts creatively."},
		{"role": "user", "content": "compose a poem that explains polymorphism in object oriented programming."}
	]
)

print(completion.choices[0].message)

