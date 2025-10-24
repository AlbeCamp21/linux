### `payload identifiers`

**Qué es (definición):** nombre único que identifica un payload dentro de Metasploit (o herramientas similares). Describe plataforma, familia/función y a veces arquitectura/transport.  

**Estructura típica:**  
```
<platform>[/<arch>]/<family>[/<variant_or_transport>]
```

**Interpretación (ejemplos):**
- `windows/meterpreter/reverse_tcp`  
  - Platform: `windows`  
  - Family: `meterpreter` (payload avanzado con capacidades de post-explotación)  
  - Transport: `reverse_tcp` (la víctima inicia la conexión de retorno hacia el listener)
- `windows/x64/meterpreter/reverse_tcp` → misma idea pero explícita la arquitectura x64.  
- `linux/x86/shell_reverse_tcp` → shell reverso para Linux x86.

**Staged vs Stageless (breve):**
- *Staged*: pequeño *stager* que descarga/negocia un stage más grande (menor tamaño inicial, suele verse como tráfico adicional).  
- *Stageless*: binario autosuficiente que no descarga etapas extras (más grande, menos dependencias de red).  

**Por qué importa (desde defensa):**
- En logs/pcaps verás patrones distintos (descarga del stage, conexiones intermedias). Las reglas de detección pueden buscar stagers conocidos o secuencias de red/parent processes sospechosos.

**Ejemplo conceptual (no operativo):**
- Al ver `windows/meterpreter/reverse_tcp` en documentación o en un fichero `-p`, sabes que el payload está diseñado para Windows y que intentará una conexión de retorno TCP hacia un host/puerto configurado.

---

### `exploit/multi/handler` (multi/handler en msfconsole)

**Qué es:** módulo de Metasploit que actúa como **handler o listener**: su función es **esperar y aceptar** conexiones entrantes de payloads tipo *reverse*. No explota vulnerabilidades por sí mismo.  

**Rol en un laboratorio (concepto):**
- El payload generado (identificado por su *payload identifier* y parametrizado con LHOST/LPORT) **se conecta** al host/puerto donde el handler está escuchando; el handler negocia la sesión y presenta una consola/sesión al operador.  

**Puntos técnicos sencillos:**
- Debe coincidir el **tipo de payload** entre el binario y el handler (p. ej. Meterpreter x64 vs x86).  
- Deben coincidir parámetros de red (la IP/puerto a los que la víctima intenta conectar deben estar accesibles y el handler debe estar escuchando en esa combinación).  
- El handler puede operar en modo *background job* para aceptar múltiples sesiones o en primer plano para interactuar inmediatamente; desde el punto de vista defensivo, su actividad se manifiesta como un proceso escuchando y como conexiones entrantes desde la víctima hacia el listener.  

**Detección/defensa (qué buscar):**
- Listeners sospechosos en tu red: hosts que reciben conexiones recurrentes en puertos no habituales desde endpoints que no deberían comunicarse.  
- Procesos que abren sockets salientes desde máquinas de usuario hacia IPs desconocidas.  
- Correlación parent/child en logs: ¿qué proceso originó la conexión (PowerShell, cmd, servicio)? Esto ayuda a distinguir automatización legítima de actividad de post-explotación.  

**Ejemplo conceptual (no comandos):**  
- Si en tus logs ves un binario con comportamiento de `meterpreter stager` (tráfico corto seguido de tráfico persistente) y, simultáneamente, un host interno inicia conexiones a una IP externa en un puerto raro que no figura en la política de red, sospecha de un listener/handler remoto aceptando sesiones.
