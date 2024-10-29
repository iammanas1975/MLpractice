from llama_cpp import Llama

LLM = Llama(model_path = "./models/llama-2-7b-chat.Q4_K_M.gguf",n_ctx = 2048)

prompt = "Q: What is DevOps? A:"
output = LLM(prompt, max_tokens = 0)
print(output["choices"][0]["text"])
