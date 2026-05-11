#!/bin/bash
# Despliegue de aplicación Docker en EC2

APP_NAME="devops-app"
PORT=5000

echo "Deteniendo contenedor anterior si existe..."
docker stop $APP_NAME 2>/dev/null
docker rm $APP_NAME 2>/dev/null

echo "Construyendo imagen Docker..."
docker build -t $APP_NAME .

echo "Ejecutando contenedor..."
docker run -d --name $APP_NAME -p $PORT:5000 $APP_NAME

echo "Aplicación desplegada en puerto $PORT"