FROM python:3.11-slim

# Répertoire de travail dans le container
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-django

# Copier le reste du projet
COPY . /app/

# Exposer le port Django
EXPOSE 5000

# Par défaut, lancer les tests (modifiable dans Jenkins)
CMD ["sh", "-c", "python manage.py migrate && python manage.py test"]
