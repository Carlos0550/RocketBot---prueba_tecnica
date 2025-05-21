from lxml import etree
from .utils import handleGetText, handleSafeCast


def parse_user_xml(xml_bytes):
    root = etree.fromstring(xml_bytes)

    perfil = root.find("perfil")
    if perfil is None:
        raise ValueError("Falta la sección <perfil>")

    compras = root.find("historial_compras")
    if compras is None:
        raise ValueError("Falta <historial_compras>")

    ubicacion = root.find("ubicacion")
    if ubicacion is None:
        raise ValueError("Falta <ubicacion>")

    etiquetas = root.findall("etiquetas/etiqueta")

    return {
        "id": handleSafeCast(handleGetText(root, "id"), int, 0),
        "nombre": handleGetText(root, "nombre"),
        "activo": handleGetText(root, "activo", default="false") == "true",
        "fecha_registro": handleGetText(root, "fecha_registro"),
        "balance": handleSafeCast(handleGetText(root, "balance"), float, 0.0),
        "etiquetas": [e.text for e in etiquetas if e is not None and e.text],
        "perfil": {
            "edad": handleSafeCast(handleGetText(perfil, "edad"), int, 0),
            "email": handleGetText(perfil, "email"),
            "telefono": handleGetText(perfil, "telefono", required=False, default=None)
        },
        "historial_compras": [
            {
                "producto_id": handleGetText(c, "producto_id"),
                "cantidad": handleSafeCast(handleGetText(c, "cantidad"), int, 0),
                "precio_unitario": handleSafeCast(handleGetText(c, "precio_unitario"), float, 0.0),
            } for c in compras.findall("compra")
        ],
        "ubicacion": {
            "latitud": handleSafeCast(handleGetText(ubicacion, "latitud"), float, 0.0),
            "longitud": handleSafeCast(handleGetText(ubicacion, "longitud"), float, 0.0)
        },
        "notificaciones": handleGetText(root, "notificaciones", default="false") == "true"
    }