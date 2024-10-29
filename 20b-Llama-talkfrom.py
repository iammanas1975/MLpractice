import sys
from langchain_community.llms import CTransformers
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
#from langchain import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""

llm = CTransformers(model = './models/llama-2-7b-chat.Q4_K_M.gguf', model_type = 'llama', config = {'max_new_tokens' : 2048, 'temperature' : 0.01, 'context_length' : 4096})
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device': 'cpu'})
db = FAISS.load_local("faiss", embeddings, allow_dangerous_deserialization = True)

retriever = db.as_retriever(search_kwargs = {'k': 2})
prompt = PromptTemplate(template = template, input_variables = ['context', 'question'])
qa_llm = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever, return_source_documents=True, chain_type_kwargs={'prompt': prompt})

while True:
        prompt = input('Prompt: ')
        if prompt.lower() in ("exit", "quit", "q"):
                print("Exiting...")
                sys.exit()
        output = qa_llm({'query': prompt})
        print(output["result"])
