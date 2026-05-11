#!/usr/bin/env python3
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('DevOpsUsers')

# Insertar
table.put_item(Item={'UserId': 'user001', 'Name': 'Ana López', 'Email': 'ana@example.com'})
print("Insertado: user001")

# Leer
item = table.get_item(Key={'UserId': 'user001'}).get('Item')
print(f"Leído: {item}")

# Actualizar
table.update_item(
    Key={'UserId': 'user001'},
    UpdateExpression="set Email=:e",
    ExpressionAttributeValues={':e': 'ana@devops.com'}
)
print("Actualizado: user001")

# Eliminar
table.delete_item(Key={'UserId': 'user001'})
print("Eliminado: user001")

print("Operaciones CRUD completadas.")