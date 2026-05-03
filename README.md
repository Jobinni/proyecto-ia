# 🪵 Sistema Inteligente de Capacitación de Personal con IA y RAG

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-green?logo=chainlink)](https://python.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-LLaMA_3.1_8B-orange)](https://ollama.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-0.5-purple)](https://www.trychroma.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-teal?logo=fastapi)](https://fastapi.tiangolo.com/)

## 📋 Descripción del Proyecto

Este proyecto corresponde a una solución basada en Inteligencia Artificial, modelos LLM y técnicas RAG orientada a facilitar la capacitación del personal nuevo en una empresa de carpintería.

El sistema permite responder consultas técnicas del aprendiz en lenguaje natural, recuperar procedimientos internos del taller, normas de seguridad y fichas de materiales como base de conocimiento.

La solución utiliza un pipeline de Recuperación Aumentada por Generación (RAG) junto con un modelo LLM ejecutado localmente mediante Ollama.

---

# Problema que Resuelve

| Problema Detectado                                        | Solución Implementada                              |
| --------------------------------------------------------- | -------------------------------------------------- |
| Aprendices dependen de maestros para resolver dudas       | Asistente IA disponible en cualquier momento       |
| Procedimientos inconsistentes según quién enseñe         | Respuestas basadas en documentos validados         |
| Tiempo de aprendizaje prolongado                          | Guías paso a paso generadas automáticamente        |
| Riesgo de accidentes por desconocimiento de seguridad    | Normas de seguridad entregadas antes de cada tarea |
| Conocimiento institucional concentrado en pocas personas  | Centralización de manuales mediante RAG            |

---

# Arquitectura del Sistema

```text
┌──────────────────────────────┐
│     Aprendiz / Carpintero    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Frontend Web            │
│    React + Tailwind          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Backend API          │
│          FastAPI             │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
┌──────────────┐   ┌────────────────┐
│   Motor RAG  │   │ Base de Datos  │
│  LangChain   │   │    SQLite      │
└──────┬───────┘   └────────────────┘
       │
       ▼
┌──────────────────────────────┐
│        ChromaDB              │
│      Base Vectorial          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Documentos del Taller       │
│ - Manuales de procedimientos │
│ - Fichas de seguridad        │
│ - Fichas técnicas de madera  │
│ - Registros de proyectos     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      LLM Local               │
│   LLaMA 3.1 + Ollama         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Guía clara para el Aprendiz  │
└──────────────────────────────┘
```

---

# Flujo General del Pipeline RAG

1. El aprendiz ingresa una consulta técnica en lenguaje natural.
2. La consulta es convertida en embeddings.
3. ChromaDB busca los fragmentos más relevantes de los documentos del taller.
4. El contexto recuperado se inserta en el prompt correspondiente.
5. LLaMA 3.1 genera una respuesta clara y ordenada.
6. El aprendiz recibe instrucciones paso a paso o la norma de seguridad correspondiente.

---

# Tecnologías Utilizadas

| Tecnología       | Función                    |
| ---------------- | -------------------------- |
| Python 3.11      | Backend principal          |
| FastAPI          | API REST                   |
| React            | Frontend                   |
| LangChain        | Orquestación RAG           |
| ChromaDB         | Base vectorial             |
| Ollama           | Ejecución local de modelos |
| LLaMA 3.1        | Modelo LLM                 |
| nomic-embed-text | Embeddings                 |
| SQLite           | Base de datos              |
| Docker           | Contenedores               |

---

# Ejecución del Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/usuario/proyecto-carpinteria-ia.git
cd proyecto-carpinteria-ia
```

## 2. Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno

Linux/macOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Instalar Ollama

Descargar desde: https://ollama.com

## 5. Descargar modelos

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

## 6. Configurar variables de entorno

Crear archivo `.env`:

```env
OLLAMA_MODEL=llama3.1:8b
EMBED_MODEL=nomic-embed-text
CHROMA_DB=./data/chroma
SQLITE_DB=./data/database.db
```

## 7. Agregar documentos del taller

Coloca los documentos PDF en `data/documentos/`. Se recomienda incluir:
- Manuales de procedimientos de carpintería
- Fichas de seguridad por máquina (sierra, fresadora, cepillo, etc.)
- Fichas técnicas de materiales y acabados
- Registros de proyectos anteriores

## 8. Ejecutar indexación de documentos

```bash
python scripts/index_documents.py
```

## 9. Iniciar Backend

```bash
uvicorn app.main:app --reload
```

API disponible en: `http://localhost:8000`

## 10. Iniciar Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend disponible en: `http://localhost:3000`

---

# Estructura del Proyecto

```text
proyecto-carpinteria-ia/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── prompts/
│   └── models/
│
├── frontend/
│
├── data/
│   ├── documentos/        ← Coloca aquí los PDFs del taller
│   └── chroma/
│
├── scripts/
│   ├── index_documents.py
│   └── test_rag.py
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Ejemplos de Uso

```text
Aprendiz:
¿Cómo hago una unión a inglete correctamente?

Respuesta:
La unión a inglete consiste en cortar ambas piezas de madera en un ángulo de 45°
para que al unirlas formen una esquina de 90°. Sigue estos pasos:
1. Ajusta la sierra ingletadora a 45° antes de cortar.
2. Asegura la pieza con la mordaza antes de encender la máquina.
3. Aplica cola PVA en ambas superficies y presiona firmemente.
4. Usa sargentos por al menos 30 minutos hasta que seque.
Recuerda usar protección ocular y auditiva al operar la sierra.
```

---

# Beneficios Esperados

* Reducción del tiempo de aprendizaje del personal nuevo.
* Estandarización de procedimientos y normas de seguridad.
* Menor dependencia de los maestros carpinteros para consultas básicas.
* Preservación del conocimiento institucional del taller.
* Modernización del proceso de onboarding de nuevos trabajadores.
* Respuestas disponibles en cualquier momento dentro del taller.

---

# Referencias Técnicas

* LangChain Documentation
* Ollama Documentation
* ChromaDB Documentation
* FastAPI Documentation
* Lewis et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
