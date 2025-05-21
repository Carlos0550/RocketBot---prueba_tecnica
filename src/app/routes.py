from flask import Blueprint, request, jsonify
from flasgger import swag_from
from .parser import parse_user_xml

main = Blueprint("main", __name__)
from .request_types import Usuario
from pydantic import ValidationError

@main.route("/parse-user", methods=["POST"])
@swag_from({
    'tags': ['Parser'],
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Archivo XML del usuario'
        }
    ],
    'responses': {
        200: {
            'description': 'JSON generado exitosamente'
        },
        400: {
            'description': 'Falta el archivo XML'
        },
        422: {
            'description': 'Error de validación'
        },
        500: {
            'description': 'Error inesperado'
        }
    }
})
def parse_user():
    if "file" not in request.files:
        return jsonify({"error": "No se envio ningun archivo."}), 400
    
    xml_file = request.files["file"]
    
    try:
        xml_bytes = xml_file.read()
        parsed_data = parse_user_xml(xml_bytes)
        
        validated_user = Usuario(**parsed_data)
       
        return jsonify(validated_user.model_dump()), 200
    except ValidationError as ve:
        mensajes = [error["msg"] for error in ve.errors()]
        return jsonify({'Error de validación': mensajes}), 422

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    