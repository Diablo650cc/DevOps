#!/bin/bash
# Limpieza de logs antiguos (>7 días)

LOG_DIR="/var/log"
DAYS=7

echo "Eliminando logs antiguos en $LOG_DIR con más de $DAYS días..."
find $LOG_DIR -name "*.log" -type f -mtime +$DAYS -delete

echo "Limpieza completada."