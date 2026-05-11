import json
import random

def lambda_handler(event, context):
    messages = [
        "¡Bienvenido a DevOps!",
        "La automatización es clave.",
        "Infraestructura como código es poder.",
        "CloudWatch te está vigilando.",
        "Hoy es un gran día para desplegar.",
        "Pipeline CI/CD exitoso."
    ]
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'mensaje': random.choice(messages),
            'timestamp': context.get_remaining_time_in_millis()
        })
    }