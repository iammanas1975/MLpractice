#import openai and key
import os
import openai
openai.api_key = os.environ['OPENAI_API_KEY']
client = openai.OpenAI()

#helper function for inducing prompts and generating results for OpenAI library 0.27.0
def get_completion(prompt, model = "gpt-3.5-turbo"):
	messages = [{"role":"user", "content":prompt}]
	response = client.chat.completions.create(
		model = model,
		messages = messages,
		temperature = 0 #degree of randomness of model's output
	)
	return response.choices[0].message

#prompting
text = "i have a dream and a song to sing"
#text = f"""i went to the store, to pick up a chore, \
#the shopkeeper threw me out, and i went to a boxing bout.
#"""

#here the text goes into the prompt delimited by any tags, characters or character sequences
prompt = "translate the text delimited here by < > into Dutch <{trext}>"
#prompt = f"""translate the text delimited by < > into Dutch and convert to third person \
#<{text}>
#"""

response = get_completion(prompt)
print(response)


