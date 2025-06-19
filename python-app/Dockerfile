FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

# 🔧 Actualizar repositorios e instalar wkhtmltopdf con sus dependencias
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    libxrender1 \
    libxext6 \
    libfontconfig1 \
    && apt-get clean

# 📦 Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copiar el resto del código
COPY . .

# 💤 Mantener contenedor vivo para pruebas (puedes cambiarlo a python send_email.py)
CMD ["tail", "-f", "/dev/null"]
