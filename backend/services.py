from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("vectorstore/constitution_index", embeddings)

def get_answer(question: str, k: int = 3):
    docs = vectorstore.similarity_search(question, k=k)
    return [doc.page_content for doc in docs]
