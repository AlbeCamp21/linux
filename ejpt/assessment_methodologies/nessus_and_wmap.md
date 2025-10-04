# Nessus y Wmap

# 1. Resumen rápido
- **Nessus**: escáner de vulnerabilidades (Tenable). Fuerte en detección de CVE, configuraciones inseguras, escaneos autenticados. Interfaz web rica y generación de reportes.
- **Wmap**: workflow/plugin de **Metasploit Framework** para mapeo/escaneo de aplicaciones web usando módulos auxiliares HTTP de Metasploit. Facilita pasar de enumeración a explotación en el mismo entorno.

---

# 2. Nessus

## ¿Qué es?
Nessus es un escáner de vulnerabilidades comercial/desarrollado por Tenable. Detecta vulnerabilidades conocidas, errores de configuración y software desactualizado en hosts y servicios.

## Para qué sirve
- Identificar vulnerabilidades (CVE) en hosts, servicios y aplicaciones.
- Detectar configuraciones inseguras y ausencia de parches.
- Priorizar mitigaciones basadas en severidad/impacto.
- Generar reportes para compliance y remediación.
- Hacer escaneos autenticados (credentialed scans) para auditoría profunda.

## Instalación básica (resumen)
1. Descargar paquete para tu SO (Tenable proporciona `.deb`, `.rpm`, instaladores).
2. Instalar el paquete.
3. Iniciar servicio (ej. `systemctl start nessusd` o script provisto).
4. Acceder por navegador: `https://<host>:8834` y activar/registrar según edición.

## Flujo de uso (Interfaz web — recomendado)
1. Accede a `https://<host>:8834`.
2. Crea cuenta administrador y activa licencia o usa key de Essentials.
3. New Scan → elegir plantilla (Basic Network Scan, Web Application Tests, Credentialed Patch Audit, etc.).
4. Configura targets (IPs, rangos, FQDNs).
5. Configura credenciales si vas a hacer credentialed scans (SSH, SMB, Windows, SNMP, etc.).
6. Ejecuta el escaneo y revisa resultados por severidad.
7. Exporta reportes (PDF, CSV, HTML, Nessus DB).

## Plantillas y opciones importantes
- **Basic Network Scan**: identificación de puertos y servicios.
- **Advanced Scan**: mayor control de plugins, tiempoouts, credenciales y políticas.
- **Web Application Tests**: pruebas específicas a aplicaciones web.
- **Credentialed Scans**: uso de credenciales para analizar configuraciones internas y parches.
- **Policy Editor**: seleccionar/omitir plugins, ajustar thresholds, tuning de tiempos.

## Interpretación de resultados
- Severidades típicas: **Critical / High / Medium / Low / Informational**.
- Cada hallazgo indica: descripción, CVE(s), evidencia, pasos de mitigación y referencias.
- Prioriza por CVSS, exposición (internet-facing), criticalidad del activo y exploits públicos.

## Integraciones
- Exportar a XML/CSV/HTML; muchos SIEM/PLATAFORMAS aceptan esos formatos.
- Importación a herramientas de gestión de vulnerabilidades o explotación (p. ej. Metasploit en ciertas versiones).
- Integración con plataformas de orquestación/CMDB para remediación.

## Ejemplos de comandos (según instalación)
```bash
# Actualizar plugins (según versión/instalación)
nessuscli update

# Manejo de usuarios (según versión)
nessuscli adduser nombre_usuario
nessuscli rmuser nombre_usuario

# Iniciar servicio (ejemplo systemd)
sudo systemctl start nessusd
sudo systemctl status nessusd
```

El uso principal de Nessus se hace desde la interfaz web; los comandos CLI varían por versión.

## Consideraciones y buenas prácticas

- Ejecutar solo en entornos con permiso explícito.
- Preferir escaneos credentialed para mayor precisión y menos falsos positivos.
- No programar escaneos pesados en ventanas críticas sin coordinación.
- Mantener plugins/DB actualizados.
- Revisar manualmente hallazgos críticos antes de tomar acciones automáticas.

# 3. Wmap (dentro de Metasploit)

## ¿Qué es?

Wmap es (o fue) un plugin/flujo de Metasploit para mapear aplicaciones web. Agrupa y orquesta módulos auxiliares HTTP de Metasploit para reconocimiento y mapeo web, registrando resultados en la base de datos de msfconsole.

## Para qué sirve

- Descubrir rutas, formularios, parámetros y tecnologías web.
- Detectar CMS, versiones y puntos potenciales de explotación.
- Automatizar múltiples comprobaciones dentro del framework Metasploit.
- Pasar de reconocimiento a explotación usando módulos disponibles en msfconsole.

## Uso básico dentro de `msfconsole`

```bash
# iniciar msfconsole
msfconsole

# cargar wmap (si está disponible)
load wmap

# añadir un sitio
wmap_sites -a http://<url>

# listar sitios añadidos
wmap_sites -l

# ejecutar escaneo (tests configurados)
wmap_run -t

# listar vulnerabilidades detectadas por wmap
wmap_vulns -l

# listar archivos/rutas detectadas
wmap_files -l
wmap_hosts -l
```

> Nota: la disponibilidad del plugin `wmap` depende de la versión de Metasploit. Si no existe, usa módulos auxiliares individuales.