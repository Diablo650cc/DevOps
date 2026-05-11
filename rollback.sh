#!/bin/bash
# Rollback automático a versión anterior

APP_NAME="devops-app"
PREVIOUS_TAG="latest-stable"

echo "Revirtiendo a versión $PREVIOUS_TAG..."
docker stop $APP_NAME 2>/dev/null
docker rm $APP_NAME 2>/dev/null
docker run -d --name $APP_NAME -p 5000:5000 $APP_NAME:$PREVIOUS_TAG

echo "Rollback completado."