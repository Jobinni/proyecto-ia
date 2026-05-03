from pydantic import BaseModel
from typing import Literal

# Lo que el aprendiz envía a la API
class ConsultaRequest(BaseModel):
    consulta: str
    tipo: Literal["procedimiento", "seguridad", "material"] = "procedimiento"

# Lo que la API le responde al aprendiz
class ConsultaResponse(BaseModel):
    consulta_original: str
    tipo: str
    respuesta: str
