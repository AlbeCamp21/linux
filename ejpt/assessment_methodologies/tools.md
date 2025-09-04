# Herramientas

### `dig`  
Herramienta de línea de comandos para realizar consultas DNS.  
- Permite consultar registros como **A, AAAA, MX, NS, TXT, SOA, CNAME**.  
- Soporta consultas a **servidores DNS específicos** con `@servidor`.  
- Puede mostrar resultados en formato resumido (`+short`) o detallado.  
- Permite medir tiempos de respuesta y depurar problemas de DNS.  
- También se usa para probar **transferencias de zona (AXFR)** y detectar configuraciones inseguras.  

### `dnsdumpster.com`  
Servicio en línea para **reconocimiento DNS** de un dominio.  
- Identifica registros (A, MX, NS, TXT).  
- Descubre **subdominios** y hosts relacionados.  
- Genera posibles **mapas de red** visuales.  
- Ayuda en la enumeración inicial de infraestructura de un objetivo.  

### `dnsenum`  
Herramienta en Perl para **enumeración DNS** automatizada.  
- Obtiene registros DNS (A, MX, NS, TXT).  
- Intenta realizar **transferencias de zona (AXFR)**.  
- Usa diccionarios para descubrir **subdominios ocultos**.  
- Puede buscar rangos de IP relacionados con el dominio.  
- Integra búsquedas inversas para encontrar hosts asociados.  

### `dnsrecon`  
Herramienta avanzada de **reconocimiento DNS** en Python.  
- Enumera registros comunes y especiales (A, AAAA, MX, SOA, PTR, TXT).  
- Realiza **zonetransfer tests (AXFR)** para encontrar fugas de datos.  
- Permite **fuerza bruta de subdominios** con diccionarios.  
- Realiza consultas inversas para identificar hosts por IP.  
- Exporta resultados en múltiples formatos (CSV, JSON, XML).  

### `fierce`  
Herramienta en Perl enfocada en **descubrir hosts y subdominios**.  
- Localiza subdominios mediante **wordlists**.  
- Detecta configuraciones incorrectas de DNS (AXFR).  
- Busca **rangos de IP asociados** a un dominio.  
- Intenta localizar hosts internos expuestos.  
- Muy usada en la fase de **reconocimiento pasivo y activo** en pentesting.  

### `netcraft.com`  
Servicio en línea de **reconocimiento de infraestructura web**.  
- Identifica el **sistema operativo** del servidor.  
- Detecta **tecnologías** usadas (CMS, frameworks, servidores).  
- Obtiene datos de **hosting y proveedor de servicios**.  
- Muestra información sobre **certificados SSL/TLS**.  
- Puede dar detalles históricos del dominio (tecnologías pasadas, hosting previo).  

### `sublist3r`  
Herramienta en Python para **enumerar subdominios**.  
- Usa motores de búsqueda (Google, Bing, Yahoo, Baidu, Ask).  
- Integra fuentes públicas como VirusTotal y Netcraft.  
- Puede trabajar con wordlists para fuerza bruta.  
- Resultados exportables en archivos de texto.  
- Ideal para descubrir subdominios rápidamente usando **OSINT**.  

### `theHarvester`  
Herramienta de recolección de información mediante **OSINT**.  
- Obtiene **correos electrónicos** relacionados con el dominio.  
- Extrae nombres de empleados desde fuentes públicas.  
- Descubre subdominios, hosts y puertos abiertos.  
- Se integra con buscadores, PGP servers, y redes sociales.  
- Muy útil en la fase de **footprinting** de un objetivo.  

### `wafw00f`  
Herramienta para detectar **Web Application Firewalls (WAF)**.  
- Identifica si un sitio web tiene un WAF activo.  
- Reconoce el **tipo y fabricante** del WAF (Cloudflare, F5, Akamai, etc.).  
- Permite ajustar ataques posteriores según el firewall encontrado.  
- Útil para planear pruebas de penetración web más efectivas.  

### `whatis`  
Herramienta de Linux para **documentación rápida de comandos**.  
- Muestra una breve descripción de un comando.  
- Sirve como acceso rápido al **manual del sistema**.  
- Ejemplo: `whatis ls` devuelve “ls (1) - list directory contents”.  

### `whois`  
Herramienta que consulta la base de datos de registros de dominios.  
- Obtiene información sobre el **propietario** de un dominio.  
- Muestra **fechas de creación y expiración**.  
- Indica servidores DNS asociados y hosting.  
- Puede revelar datos de contacto (si no están ocultos con privacidad).  
- También sirve para investigar **rangos de IP** y ASN.  
