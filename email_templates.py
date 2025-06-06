def get_order_confirmation_template(nombre_cliente, producto, cantidad, precio_total):
    return f"""
    <html>
      <body style="background-color: #f9f9f9; font-family: Arial, sans-serif; padding: 40px;">
        <div style="
          max-width: 600px;
          margin: 0 auto;
          background-color: #ffffff;
          border-radius: 8px;
          box-shadow: 0 0 10px rgba(0,0,0,0.1);
          padding: 30px;
          text-align: center;
        ">
          <img src="https://1000marcas.net/wp-content/uploads/2020/01/KFC-logo.png"
               alt="Logo KFC"
               width="150"
               style="margin-bottom: 20px;" />

          <h2 style="color: #D9230F;">¡Hola {nombre_cliente}!</h2>

          <p style="font-size: 16px; color: #333;">Gracias por tu compra en <strong>KFC</strong>. Aquí tienes el resumen de tu pedido:</p>

          <div style="text-align: left; margin: 20px auto;">
            <ul style="list-style: none; padding: 0; font-size: 15px; color: #444;">
              <li><strong>🍗 Producto:</strong> {producto}</li>
              <li><strong>🔢 Cantidad:</strong> {cantidad}</li>
              <li><strong>💲 Precio total:</strong> ${precio_total}</li>
            </ul>
          </div>

          <p style="font-size: 15px; color: #333;">Tu pedido será preparado con amor y estará listo muy pronto 😋</p>

          <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;" />

          <p style="color: gray; font-size: 12px;">Este correo es solo para fines de demostración con MailHog.<br />Gracias por elegir KFC 🍟</p>
        </div>
      </body>
    </html>
    """
