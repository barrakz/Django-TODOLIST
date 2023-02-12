# Ustawienie obrazu bazowego
FROM python:3.8-alpine

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików aplikacji do kontenera
COPY . /app

# Instalacja wymaganych pakietów
RUN pip install --no-cache-dir -r requirements.txt

# Uruchomienie aplikacji
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


