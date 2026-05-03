import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_DB", "./data/chroma")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")

def probar_busqueda():
    print("Conectando a la base de datos vectorial...")
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    # Pruebas representativas de cada tipo de consulta del informe
    consultas = [
        ("procedimiento", "¿Cómo se hace una unión a inglete correctamente?"),
        ("seguridad",     "¿Qué protección necesito para usar la sierra circular?"),
        ("material",      "¿Para qué sirve la cola PVA y cuándo se usa?"),
    ]

    for tipo, query in consultas:
        print(f"\n{'='*55}")
        print(f"Tipo: {tipo.upper()}")
        print(f"Consulta: '{query}'")
        print(f"{'='*55}")

        resultados = vector_store.similarity_search(query, k=2)

        if not resultados:
            print("No se encontraron resultados. ¿Seguro que indexaste los documentos?")
            continue

        for i, doc in enumerate(resultados):
            print(f"\nFragmento {i+1} (Fuente: {doc.metadata.get('source', 'Desconocida')}):")
            print(doc.page_content)

if __name__ == "__main__":
    probar_busqueda()
