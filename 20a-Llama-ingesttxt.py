from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = DirectoryLoader("./docs/", glob = "*.txt", loader_cls = TextLoader)
documents = loader.load()
#print(documents)
splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

texts = splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device': 'cpu'})

db = FAISS.from_documents(texts, embeddings)
db.save_local("faiss")
