#!/bin/bash
# Instalación de paquetes esenciales en Cloud9/Ubuntu

echo "Actualizando paquetes..."
sudo apt update -y

echo "Instalando git, vim, docker, python3, pip..."
sudo apt install -y git vim docker.io python3 python3-pip

echo "Instalando boto3 y awscli..."
pip3 install boto3 awscli --user

echo "Iniciando servicio Docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Agregando usuario al grupo docker..."
sudo usermod -aG docker $USER

echo "Instalación completada. Reinicia la sesión para usar Docker sin sudo."