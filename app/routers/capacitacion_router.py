from fastapi import APIRouter, HTTPException
from app.models.schemas import ConsultaRequest, ConsultaResponse
from app.services.rag_service import rag_service

router = APIRouter(prefix="/api/v1", tags=["Capacitación"])

@router.post("/consultar", response_model=ConsultaResponse)
async def consultar(request: ConsultaRequest):
    """
    Endpoint principal. Recibe la consulta del aprendiz y el tipo:
    - procedimiento: explica cómo hacer una tarea paso a paso
    - seguridad: entrega normas de seguridad antes de realizar la tarea
    - material: identifica y explica materiales o herramientas
    """
    try:
        if request.tipo == "procedimiento":
            respuesta = rag_service.consultar_procedimiento(request.consulta)
        elif request.tipo == "seguridad":
            respuesta = rag_service.consultar_seguridad(request.consulta)
        elif request.tipo == "material":
            respuesta = rag_service.consultar_material(request.consulta)
        else:
            raise HTTPException(status_code=400, detail="Tipo de consulta no válido.")

        return ConsultaResponse(
            consulta_original=request.consulta,
            tipo=request.tipo,
            respuesta=respuesta
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
