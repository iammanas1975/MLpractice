#This is reference only, not for actual execution unless libraries and environments are set
#install python library for openAI
pip install openai

#import openai and key
import openai
openai.api_key = 'sk-...'

#alternatively import and set the key as an environment variable
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

#helper function for inducing prompts and generating results for OpenAI library 0.27.0
def get_completion(prompt, model = "gpt-3.5-turbo"):
#in case you want to vary temperature, include it as a parameter here; def get_completion(..., temperature=0):
	messages = [{"role":"user", "content":prompt}]
	response = openai.ChatCompletion.create(
		model = model,
		messages = messages,
		temperature = 0 #degree of randomness of model's output
		#in case you want to vary temperature, refer to modified def above; here use: temperature=temperature
	)
	return response.choices[0].message["content"]

#same function as above for OpenAI library 1.0.0
client = openai.OpenAI()

def get_completion(prompt, model = "gpt-3.5-turbo"):
	messages = [{"role":"user", "content":prompt}]
	response = client.chat.completions.create(
		#same as above
	)
	return response.choices[0].message.content

#prompting
text = f"""
keep writing free form text here \
which would be reference to the actual prompt \
for generating the results.
"""

#here the text goes into the prompt delimited by any tags, characters or character sequences
prompt = f"""
Do something to text as above, here delimited by triple question marks \
optionally in some given format or as say as a sequence of steps \
???{text}???
"""

response = get_completion(prompt)
print(response)

#if you have asked to return result in HTML format, to load Python libs for displaying HTML
from IPython.display import display, HTML
display(HTML(response))

#summarizing reviews
review_1 = """
some product 1 review text
"""
review_2 = """
another product 2 review text
"""
review_3 = """
still another product 3 review text
"""
reviews = [review_1, review_2, review_3]
for i in range(len(reviews)):
	prompt = f"""
	summarize with given constraints the review delimited by <> \
	<{reviews[i]}>
"""
response = get_completion(prompt)
print(i, response,"\n")

#idea for building a custom chatbot
#define a different helper function where multiple messages in form of conversation comes as input
def get_completion_from_messages(messages, model = 'gpt-3.5-turbo", temperature = 0):
	response = openai.ChatCompletion.create(
		model = model,
		messages = messages,
		temperature = temperature
	)
	print(str(response.choices[0].message)) #in case you want to trace which role in message - see below - is generating response
	return response.choices[0].message["content"]

messages = [
{'role':'system','content':'You are an assistant that talks like Einstein.'},
{'role':'user','content':'tell me a joke'},
{'role':'assistant','content':'why did the chicken cross the road'},
{'role':'user','content':'I don\'t know'} ]

response = get_completion_from_messages(messages,temperature=1)
print(response)

#building an OrderBot for pizza ordering
def collect_messages(_):
	prompt = inp.value_input #get user input as prompts
	inp.value = ''
	context.append({'role':'user','content':f"{prompt}"}) #add user prompt to build up context
	response = get_completion_from_messages(context)      #generate response to context incl. previous prompts and responses
	context.append({'role':'assistant','content':'f"{response}"}) #add response to the context
	panels.append(						      #display the results in a GUI
		pn.Row('Users:', pn.pane.MarkDown(prompt, width=600)))
	panels.append(
		pn.Row('Assistant:', pn.pane.MarkDown(response, width=600, style={'background-color': '#F6F6F6'})))
	return pn.Column(*panels)

import panel as pn #GUI
pn.extension()

panels = [] #collect display

#define the initial context to start the conversation
context = [ {'role':'system','content',"""
you are an OrderBot, an automated service to collect orders from a pizza restaurant. \
you first greet the customer, then collect the order, \
and then ask if it is for pickup or delivery. \
you wait to collect the order, then summarize and check for a final time if the \
customer wants to add anything else. If for delivery, you ask for address. \
finally you collect the payment. Make sure to clarify all options, extras and \
sizes to uniquely identify the item from menu. \
you respond in short, very conversational friendly style. \
the menu includes \
cheese pizza 10.95, 9.25, 6.50 \
chicken pizza 12.95, 10.00, 7.00 \
fries 4.50, 3.50 \
salad 7.25 \
Toppings: \
extra cheese 2.00 \
mushrooms 1.50 \
sausage 3.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 2.50, 1.50, 1.00 \
"""} ]

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here...')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
	inp,
	pn.Row(button_conversation),
	pn.panel(interactive_conversation, loading_indicator=True, height=300)
)

dashboard

#to turn the order taken by OrderBot into JSON format
messages = context.copy()
messages.append(
{'role':'system','content':'create a JSON summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size 4) list of sides, include size\
 5) total price'},
)

response = get_completion_from_messages(messages, temperature=0)
print(response)

