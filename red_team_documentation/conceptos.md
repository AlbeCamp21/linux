# Conceptos

1. **C2 Server**
   - Servidor utilizado para controlar de forma remota sistemas comprometidos.
   - Permite enviar comandos y recibir información desde las máquinas infectadas.
   - Es una pieza clave en campañas de malware y ataques dirigidos.
   - Suele comunicarse mediante protocolos como HTTP, HTTPS, o DNS para evadir detección.
   - Ejemplo: Un atacante usa un servidor C2 para ordenar a un ransomware que cifre archivos en varios equipos.

---

2. **Payload Server**
   - Servidor donde se alojan los archivos maliciosos que se descargarán en el sistema objetivo.
   - Puede contener scripts, ejecutables o exploits que realizan la carga útil del ataque.
   - Normalmente es temporal y se cambia para evitar rastreo.
   - Ejemplo: Un servidor que almacena un archivo “malware.exe” que se descarga cuando la víctima hace clic en un enlace.

---

3. **Redirector Server**
   - Servidor intermediario que redirige el tráfico entre la víctima y el C2 o payload server.
   - Ayuda a ocultar la ubicación real del servidor principal.
   - Puede usarse para filtrar, registrar o manipular el tráfico.
   - Ejemplo: La víctima se conecta a un servidor en otro país, pero este solo redirige la conexión al C2 real en una ubicación oculta.

---

4. **De-Militarized Zone Network (DMZ Network)**
   - Red intermedia que conecta sistemas accesibles desde internet, sin exponer la red interna.
   - Alberga servidores que brindan servicios públicos como correo, web o DNS.
   - Protege la red privada de accesos directos desde redes no confiables.
   - Ejemplo: Una empresa coloca su servidor web en la DMZ para que clientes externos accedan sin comprometer la red interna.

---

5. **Militarized Zone Network (MZ Network)**
   - Segmento de red altamente seguro donde se almacenan datos críticos de la organización.
   - Tiene las restricciones de acceso más estrictas del entorno.
   - Desde aquí se gestionan operaciones y recursos esenciales.
   - Ejemplo: El área donde se guardan las bases de datos financieras y solo personal autorizado puede acceder físicamente y lógicamente.

---

6. **Tactics, Techniques and Procedures (TTPs)**
   - Forma en que un atacante planifica y ejecuta sus operaciones.
   - “Tácticas”: objetivos generales de la acción.
   - “Técnicas”: métodos concretos para alcanzar esos objetivos.
   - “Procedimientos”: pasos detallados que sigue el atacante.
   - Ejemplo: Táctica → Persistencia; Técnica → Crear una tarea programada; Procedimiento → Configurar una tarea en Windows que ejecute malware cada vez que se inicia sesión.

---

7. **Bastion-Host (Jump Server)**
   - Servidor especialmente endurecido y expuesto a internet para proteger la red interna.
   - Se ubica normalmente en la DMZ para controlar el tráfico entrante y saliente.
   - Solo ejecuta servicios estrictamente necesarios para reducir la superficie de ataque.
   - Suele ser el único punto de acceso permitido desde el exterior hacia la red interna.
   - Ejemplo: Un servidor SSH configurado con autenticación por clave pública, ubicado en la DMZ, que permite a administradores conectarse de forma segura y luego acceder a servidores internos.
