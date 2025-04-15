#!/bin/bash

# Ativa o ambiente virtual
source /home/vagrant/djangoENV/bin/activate

# Entra no diretório do projeto
cd /vagrant

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000
