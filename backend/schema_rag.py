from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

_vectorstore = None


def _get_vectorstore():
    global _vectorstore

    if _vectorstore is not None:
        return _vectorstore

    embeddings = OllamaEmbeddings(model="llama3")

    schema_docs = [
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

    _vectorstore = FAISS.from_documents(schema_docs, embeddings)
    return _vectorstore


def retrieve_schema(question: str) -> str:
    try:
        vectorstore = _get_vectorstore()
        docs = vectorstore.similarity_search(question, k=2)
        return "\n".join(d.page_content for d in docs)
    except Exception:
        # Safe fallback for CI / prod / low-memory systems
        return ""
