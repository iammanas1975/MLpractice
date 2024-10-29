from langchain_community.document_loaders import PyPDFLoader #, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter #,CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain

#loader = PyPDFLoader('./docs/devops_quant1.pdf')
#documents = loader.load()
loaders = [PyPDFLoader('./docs/devops_quant1.pdf'), PyPDFLoader('./docs/devops_jsonQA.pdf')]
documents = []
for loader in loaders:
       documents.extend(loader.load())
#print(documents)
splitter = RecursiveCharacterTextSplitter(chunk_size = 5000, chunk_overlap = 50)
#splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)

texts = splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device': 'cpu'})

db = FAISS.from_documents(texts, embeddings)
db.save_local("faiss")
