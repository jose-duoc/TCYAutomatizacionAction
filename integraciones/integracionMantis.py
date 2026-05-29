import requests

TOKEN = ""
BASE_URL = "https://mantistcy.cl/mantis/api/rest/issues"

def obtener_proyectos_mantis():
    headers = {"Authorization":TOKEN}
    response = requests.get(BASE_URL,headers=headers)
    print(response.status_code)
    print(response.text)
def enviar_resultado_mantis(resumen,descripcion,detalle):
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "summary":resumen,
        "description": descripcion,
        "project":{
            "name":"grupo1 - Reyes - Toledo - Zuñiga - Mella - Rodriguez - Contreras"
        },
        "category":{
            "name":"Caja Negra"
        },
        "custom_fields":[
            {
                "field":{
                    "name":"Resultado Esperado"
                },
                "value":"La página principal debe cargar correctamente"
            },
            {
                "field":{
                    "name":"Tipo Prueba"
                },
                "value":"Funcional "
            },
            {
                "field":{"name":"Resultado Obtenido"},
                "value":detalle
            }
        ]
    }
    response = requests.post(BASE_URL,json=payload,headers=headers)
    return response.status_code,response.text