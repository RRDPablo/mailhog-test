# 📬 Proyecto de Envío de Correos con MailHog y Python

Este proyecto muestra cómo enviar correos HTML con Python usando `smtplib` y verlos localmente a través de [MailHog](https://github.com/mailhog/MailHog).

## 🚀 Requisitos

- Tener instalado [Python](https://www.python.org/)
- Tener instalado [Docker](https://www.docker.com/)

## 🧪 Instrucciones rápidas

### 1. Clona el repositorio
git clone  https://github.com/RRDPablo/mailhog-test.git
cd mailhog-test

2. Inicia MailHog con Docker
Abre una terminal en la ruta del proyecto y ejecuta
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
Esto ejecuta MailHog en segundo plano e instala la imagen de MailHog si no la tienes descargada.

Accede a la interfaz web en: http://localhost:8025

3. Ejecuta el script de envío en el terminal
python send_email.py

4. Verifica el correo
Abre tu navegador y visita http://localhost:8025

Verás el correo enviado con la plantilla HTML personalizada.

📁 Archivos principales
send_email.py: Script principal que envía el correo.

email_templates.py: Plantilla HTML para el correo, personalizada con estilo de KFC.

📸 Vista previa
![image](https://github.com/user-attachments/assets/2f1d4ab4-4edd-47c7-9f5d-25bfedeb5343)
![image](https://github.com/user-attachments/assets/3e5637d4-efea-4ae8-a4a7-ced3a46d3980)

