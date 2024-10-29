from llama_cpp import Llama

model_path = "./models/llama-2-7b-chat.Q2_K.gguf"
model = Llama(model_path = model_path)

system_message = "You are a helpful assistant"
user_message = "Generate a list of five mountains in Himalayas"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

max_tokens = 200

output = model(prompt, max_tokens = max_tokens, echo = True)
print(output)
