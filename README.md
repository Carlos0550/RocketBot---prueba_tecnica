# Prueba Técnica – Rocketbot

Este proyecto es una API REST construida con Flask que permite recibir un archivo `.xml`, parsearlo y devolverlo como JSON con una estructura predeterminada y validada mediante `pydantic`.

---

## Principales tecnologías usadas

* Python 3.10
* Flask
* lxml para parseo XML
* Pydantic para validar datos en el request
* Flasgger para documentación

---

## Instalación

1. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate 
```

2. Instalar dependencias:

```bash
cd src
pip install -r requirements.txt
```

---

## Ejecución del servidor

```bash
python run.py
```

El servidor se iniciará en:

```
http://localhost:5000
```

---

## Endpoint

### POST `/parse-user`

Permite enviar un archivo XML y obtener como respuesta un JSON validado.

* **Método:** `POST`
* **Formato:** `multipart/form-data`
* **Campo requerido:** `file` (el archivo XML)

---

## Errores documentados

* `400`: Falta el archivo XML
* `422`: Error de validacion (email inválido, fecha mal formateada, etc.)
* `500`: Error inesperado

---

## Documentación interactiva (Swagger UI)

Una vez corriendo el servidor, se puede acceder a:

```
http://localhost:5000/apidocs/
```