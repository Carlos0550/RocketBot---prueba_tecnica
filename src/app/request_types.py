from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class Perfil(BaseModel):
    edad: int = Field(gt=0)
    email: EmailStr
    telefono: Optional[str] = None

class Compra(BaseModel):
    producto_id: str
    cantidad: int
    precio_unitario: float

class Ubicacion(BaseModel):
    latitud: float
    longitud: float

class Usuario(BaseModel):
    id: int
    nombre: str
    activo: bool
    fecha_registro: datetime
    balance: float
    etiquetas: List[str]
    perfil: Perfil
    historial_compras: List[Compra]
    ubicacion: Ubicacion
    notificaciones: bool
