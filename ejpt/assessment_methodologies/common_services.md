# Common services

## FTP (File Transfer Protocol)
- **Concepto**: Protocolo para transferencia de archivos entre cliente y servidor. Muy usado en entornos antiguos y todavía presente en sistemas heredados.  
- **Puerto por defecto**: 21 (control) y 20 (datos en modo activo).  
- **Otros puertos**: Puede usar un rango de puertos altos (1024+) en modo pasivo.  
- **Relaciones en ciberseguridad**:  
  - FTP suele usarse con credenciales en texto plano, lo que permite ataques de sniffing.  
  - Usuarios obtenidos por enumeración de FTP pueden reutilizarse en **SSH** o **SMB**.  
  - En entornos Windows, FTP puede estar integrado en IIS. En Linux suele correr como `vsftpd` o `proftpd`.  
- **Comandos**:  
  - En Linux: `ftp <ip>`, `lftp <ip>`  
  - En Windows: `ftp <ip>`  

---

## SMB (Server Message Block)
- **Concepto**: Protocolo para compartir archivos, impresoras y recursos en redes Windows, aunque puede implementarse en Linux (Samba).  
- **Puerto por defecto**: 445 (SMB directo sobre TCP).  
- **Otros puertos**: 137 (NetBIOS name), 138 (NetBIOS datagram), 139 (NetBIOS session).  
- **Relaciones en ciberseguridad**:  
  - SMB permite enumerar usuarios, recursos compartidos y versiones de sistema.  
  - Credenciales obtenidas aquí pueden reutilizarse en **SSH** o **MySQL**.  
  - SMB expone muchas vulnerabilidades históricas (ej: EternalBlue).  
- **Comandos**:  
  - Linux: `smbclient -L //<ip> -U <user>` , `smbmap -H <ip>`, `smbclient //<ip>/<share>`  
  - Windows: `net use \\\\<ip>\\share`  

---

## Web server (HTTP/HTTPS)
- **Concepto**: Servicio que entrega contenido web. En Linux puede ser Apache o Nginx, en Windows IIS.  
- **Puerto por defecto**: 80 (HTTP), 443 (HTTPS con TLS).  
- **Otros puertos**: 8080, 8443, 8000, entre otros.  
- **Relaciones en ciberseguridad**:  
  - El servidor web puede exponer paneles de login que se relacionan con usuarios de **SSH** o **MySQL**.  
  - Vulnerabilidades web pueden dar acceso al sistema de archivos compartido por **SMB** o a credenciales para otros servicios.  
- **Comandos**:  
  - Linux/Windows: `curl http://<ip>` , `wget http://<ip>`  
  - Navegador: `http://<ip>:puerto`  

---

## MySQL
- **Concepto**: Sistema de gestión de bases de datos relacional. Muy usado en aplicaciones web.  
- **Puerto por defecto**: 3306.  
- **Otros puertos**: Puede configurarse en cualquier puerto TCP (a veces 3307 o personalizados).  
- **Relaciones en ciberseguridad**:  
  - Credenciales de MySQL suelen coincidir con usuarios de **SSH** o del sistema.  
  - Aplicaciones web mal configuradas pueden filtrar credenciales que luego se prueban en **FTP**, **SMB**, o **SSH**.  
- **Comandos**:  
  - Linux/Windows: `mysql -h <ip> -u <user> -p`  

---

## SSH (Secure Shell)
- **Concepto**: Protocolo para acceso remoto seguro y ejecución de comandos cifrados.  
- **Puerto por defecto**: 22.  
- **Otros puertos**: Puede configurarse en puertos no estándar (ej: 2222, 2200) para ocultación básica.  
- **Relaciones en ciberseguridad**:  
  - Usuarios enumerados en **SMB** o **SMTP** pueden probarse aquí.  
  - Contraseñas filtradas en **MySQL** o **FTP** suelen ser reutilizadas en SSH.  
  - SSH puede ser un punto de entrada persistente tras explotar un **web server**.  
- **Comandos**:  
  - Linux: `ssh <user>@<ip>`  
  - Windows (PowerShell): `ssh <user>@<ip>`  

---

## SMTP (Simple Mail Transfer Protocol)
- **Concepto**: Protocolo para envío de correos electrónicos.  
- **Puerto por defecto**: 25.  
- **Otros puertos**: 465 (SMTP con SSL), 587 (SMTP con TLS).  
- **Relaciones en ciberseguridad**:  
  - Permite enumerar usuarios válidos mediante comandos VRFY, EXPN o RCPT TO.  
  - Los usuarios extraídos aquí pueden usarse en **SSH** o **SMB**.  
  - Un servidor SMTP mal configurado puede actuar como open relay (abuso para spam).  
- **Comandos**:  
  - Linux/Windows: `telnet <ip> 25` , `nc <ip> 25`  
  - Ejemplo de conexión:  
    ```
    EHLO example.com
    MAIL FROM:<test@example.com>
    RCPT TO:<victim@example.com>
    ```  
