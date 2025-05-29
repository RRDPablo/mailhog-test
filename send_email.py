import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_templates import get_order_confirmation_template

# 📦 Datos del cliente y del pedido
nombre_cliente = "Carlos"
producto = "Big Box Recargado"
cantidad = 2
precio_total = round(7.50 * cantidad, 2)

# 📧 Configuración del correo
from_address = "noreply@example.com"
to_address = "carlos@localhost"  # Usar MailHog: se verá en http://localhost:8025
subject = "🍗 Confirmación de tu pedido en KFC"

# 🧩 Obtener plantilla HTML con datos dinámicos
html_template = get_order_confirmation_template(
    nombre_cliente, producto, cantidad, precio_total
)

# ✉️ Construcción del mensaje MIME
msg = MIMEMultipart("alternative")
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

# 🔗 Adjuntar parte HTML
html_part = MIMEText(html_template, "html")
msg.attach(html_part)

# 📤 Enviar correo a través de MailHog (localhost:1025)
try:
    with smtplib.SMTP("localhost", 1025) as server:
        server.send_message(msg)
    print("📨 Correo enviado correctamente a MailHog.")
except Exception as e:
    print("❌ Error al enviar correo:", e)
