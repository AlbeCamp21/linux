# Herramientas

### `dig`  
Herramienta de línea de comandos para realizar consultas DNS.  
- Permite consultar registros como **A, AAAA, MX, NS, TXT, SOA, CNAME**.  
- Soporta consultas a **servidores DNS específicos** con `@servidor`.  
- Puede mostrar resultados en formato resumido (`+short`) o detallado.  
- Permite medir tiempos de respuesta y depurar problemas de DNS.  
- También se usa para probar **transferencias de zona (AXFR)** y detectar configuraciones inseguras.  

### `dirb`  
Herramienta para **fuerza bruta de directorios y archivos web**.  
- Busca rutas ocultas en servidores web usando **wordlists**.  
- Permite probar varias extensiones de archivos (`-X .php,.bak,.zip`) para encontrar backups o scripts.  
- Útil para detectar **directorios no indexados** o archivos sensibles.  
- Soporta escaneo recursivo para descubrir rutas profundas.  
- Ideal para enumeración de contenido en pruebas de penetración web.  

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

### `httrack`  
Herramienta para **descargar o hacer mirror de sitios web**.  
- Crea una copia local completa de un sitio accesible públicamente.  
- Descarga páginas HTML, imágenes, scripts y archivos referenciados.  
- Permite inspeccionar archivos **no visibles en la navegación normal**.  
- Útil para análisis offline o descubrimiento de archivos ocultos.  
- Puede ser configurada para seguir enlaces recursivamente y respetar reglas de robots.txt.  

### `netcraft.com`  
Servicio en línea de **reconocimiento de infraestructura web**.  
- Identifica el **sistema operativo** del servidor.  
- Detecta **tecnologías** usadas (CMS, frameworks, servidores).  
- Obtiene datos de **hosting y proveedor de servicios**.  
- Muestra información sobre **certificados SSL/TLS**.  
- Puede dar detalles históricos del dominio (tecnologías pasadas, hosting previo).  

### `netdiscover`  
Herramienta de descubrimiento de red basada en ARP.  
- Detecta **hosts activos en la red local** sin necesidad de ping.  
- Útil en redes donde el **ICMP está bloqueado**.  
- Permite identificar **direcciones IP, MAC y fabricantes** de los dispositivos.  
- Puede ejecutarse en modo pasivo (escucha ARP) o activo (envía ARP requests).  
- Ideal para auditorías rápidas de redes WiFi o LAN.  

### `nmap`  
Herramienta avanzada de **escaneo de red y seguridad**.  
- Permite descubrir **hosts activos** en un rango de IP.  
- Detecta **puertos abiertos, servicios y versiones** en ejecución.  
- Puede identificar el **sistema operativo y tipo de dispositivo**.  
- Incluye scripts (NSE – Nmap Scripting Engine) para **detección de vulnerabilidades**.  
- Soporta múltiples tipos de escaneo: TCP SYN, UDP, ICMP, entre otros.  
- La opción `-Pn` **omite el ping inicial** y fuerza el escaneo de puertos incluso si el host no responde a ICMP (útil en Windows o redes que bloquean ping).  

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
