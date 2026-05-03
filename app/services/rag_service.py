import os
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from app.prompts.templates import prompt_guia, prompt_seguridad, prompt_materiales

class RagService:
    def __init__(self):
        # Configuraciones
        CHROMA_PATH = os.getenv("CHROMA_DB", "./data/chroma")
        OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
        EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")

        # Inicializar IA y Base Vectorial
        self.llm = Ollama(model=OLLAMA_MODEL)
        self.embeddings = OllamaEmbeddings(model=EMBED_MODEL)
        self.vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=self.embeddings)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

        # Armar las cadenas para cada tipo de consulta
        self.chain_guia = create_retrieval_chain(
            self.retriever,
            create_stuff_documents_chain(self.llm, prompt_guia)
        )
        self.chain_seguridad = create_retrieval_chain(
            self.retriever,
            create_stuff_documents_chain(self.llm, prompt_seguridad)
        )
        self.chain_materiales = create_retrieval_chain(
            self.retriever,
            create_stuff_documents_chain(self.llm, prompt_materiales)
        )

    def consultar_procedimiento(self, consulta: str) -> str:
        """Prompt N°1: Explica cómo realizar un procedimiento técnico paso a paso."""
        response = self.chain_guia.invoke({"input": consulta})
        return response["answer"]

    def consultar_seguridad(self, tarea: str) -> str:
        """Prompt N°2: Entrega las normas de seguridad antes de realizar una tarea."""
        response = self.chain_seguridad.invoke({"input": tarea})
        return response["answer"]

    def consultar_material(self, consulta: str) -> str:
        """Prompt N°3: Identifica y explica materiales o herramientas del taller."""
        response = self.chain_materiales.invoke({"input": consulta})
        return response["answer"]

# Instancia global del servicio para usarla en toda la app
rag_service = RagService()
