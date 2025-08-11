## **Kerberos Authetication Process**

- Ticket Granting Ticket (TGT): Boleto utilizado específicamente para autenticación.
- Ticket Granting Service (TGS): Boleto utilizado específicamente para autorización.

```mermaid
sequenceDiagram
    participant Domain User
    participant DC
    participant Database Server

    Domain User->>DC: 1. Envía nombre de usuario y hora actual (encriptado)
    DC->>Domain User: 2. Verifica credenciales
    DC->>Domain User: 3. Emite TGT
    Domain User->>Domain User: 4. Almacena TGT en memoria
    Domain User->>DC: 5. Solicita TGS
    DC->>Domain User: 6. Emite TGS
    Domain User->>Database Server: 7. Usa TGS para autenticación/autorización
    Database Server->>DC: 8. Validaciones opcionales con DC
```

## **Kerberos Delegation Process**

- User (Usuario) → El cliente que solicita acceso a un recurso.
- DC (Domain Controller) → Servidor que autentica y emite tickets (TGT/TGS).
- AppServer (Servidor de Aplicaciones) → Servicio que recibe el TGS y delega acceso.
- DBServer (Servidor de BD) → Recurso final accedido en nombre del usuario.

```mermaid
sequenceDiagram
    participant User
    participant DC
    participant AppServer
    participant DBServer

    User->>DC: 1. Solicita TGT (envía credenciales)
    DC->>User: 2. Proporciona TGT
    User->>DC: 3. Solicita TGS para AppServer
    DC->>User: 4. Proporciona TGS para AppServer
    User->>AppServer: 5. Envía TGT y TGS
    AppServer->>DC: 6. Usa TGT del usuario para solicitar TGS para DBServer
    DC->>AppServer: 7. Proporciona TGS para DBServer
    AppServer->>DBServer: 8. Accede al DB como el usuario (usando TGS)
    loop Accesos posteriores
        AppServer->>DBServer: 9. Continúa accediendo como el usuario
    end
```

### **Types of Kerberos Delegation**

1. **Delegación Sin Restricciones (Unconstrained Delegation)**
   - Permite que el Servidor de Aplicaciones use las credenciales del usuario para acceder a cualquier servicio en cualquier servidor del dominio.
   - Está habilitada por defecto en los Controladores de Dominio.
   - Puede representar un riesgo de seguridad si el servidor es comprometido, ya que permite movimiento lateral sin restricciones.
   - Ejemplo: Un servidor de aplicaciones que, al autenticar a un usuario, puede acceder libremente a servicios de base de datos, archivos y otros en toda la red usando las credenciales delegadas del usuario.

2. **Delegación Restringida (Constrained Delegation)**
   - Permite que el Servidor de Aplicaciones use las credenciales del usuario solo para acceder a servicios específicos en servidores específicos.
   - Limita el alcance de la delegación, mejorando la seguridad al restringir qué servicios pueden ser accedidos.
   - Requiere configuración explícita para definir los servicios permitidos.
   - Ejemplo: Un servidor de aplicaciones configurado para usar las credenciales del usuario solo para acceder a un servidor de base de datos particular, evitando acceso a otros servicios del dominio.

