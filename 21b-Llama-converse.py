import sys
from langchain_community.llms import CTransformers
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain

llm = CTransformers(model = './models/llama-2-7b-chat.Q4_K_M.gguf', model_type = 'llama', config = {'max_new_tokens' : 2048, 'temperature' : 0.01, 'context_length' : 4096})

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device': 'cpu'})
db = FAISS.load_local("faiss", embeddings, allow_dangerous_deserialization = True)
retriever = db.as_retriever(search_kwargs = {'k': 2})

#qa_llm = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever, return_source_documents=True, chain_type_kwargs={'prompt': prompt})
qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, chain_type='stuff', retriever=retriever, return_source_documents=True, return_generated_question=True)

chat_history = []
while True:
        query = input('Prompt: ')
        if query.lower() in ("exit", "quit", "q"):
                print("Exiting...")
                sys.exit()
        result = qa_chain({'question': query, 'chat_history': chat_history})
        print('Answer: ' + result['answer'] + '\n')
        chat_history.append((query, result['answer']))
