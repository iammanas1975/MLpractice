from llamaapi import LlamaAPI
import json

llama = LlamaAPI('LL-Y0aIkdke2BSknalMqAraW8Gx0AfTorcIJ7EekgRbxpDWkvEqqY7vbP4riZPEQSU7')

# API Request JSON Cell
api_request_json = {
	"model": "llama-13b-chat",
	"messages": [
    		{"role": "system", "content": "You are an assistant that provides ideas for research proposals based on given research areas"},
    		{"role": "user", "content": "Hi, give me three doctorate research ideas related to business resilience, business sustainability and culture and their relation or impact with information technology"},
  	]
}

# Run llama
response = llama.run(api_request_json)
print(response.json())
