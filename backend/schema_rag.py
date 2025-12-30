from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# ---- Embeddings (NEW, NON-DEPRECATED) ----
embeddings = OllamaEmbeddings(model="llama3")

# ---- Schema documents ----
SCHEMA_DOCS = [
    Document(
        page_content="Table customers: id (integer, primary key), name (text)"
    ),
    Document(
        page_content=(
            "Table orders: id (integer, primary key), "
            "customer_id (integer, foreign key -> customers.id), "
            "amount (float)"
        )
    ),
]

# ---- Vector store ----
vectorstore = FAISS.from_documents(SCHEMA_DOCS, embeddings)

def retrieve_schema(question: str) -> str:
    docs = vectorstore.similarity_search(question, k=2)
    return "\n".join(d.page_content for d in docs)
