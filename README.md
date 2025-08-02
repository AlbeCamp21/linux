# Introducción a Linux

## Comandos

**1.** `<programa> &>/dev/null & disown`:
- `&>/dev/null`: Hace que los outputs que bote el programa (por ejemplo `burpsuite`) no se muestren en el terminal.
- `&`: Para ejecutar en segundo plano.
- `disown`: Para que no dependa del terminal, en caso se cierre el terminal donde se lanzó el programa, este seguirá.
- `2>/dev/null`: En caso que no quieran ver los errores del programa, se puede usar este comando, reemplazándolo.

---

**2.** `<comando1>; <comando2>; ... `:
- Para ejecutar varios comandos a la vez, independientemente de si sean éxito (`0`) o fallo (diferente de `0`). Los resultados se muestran en un mismo output.
- A comparación con `&&`: Este ejecuta `comando2` en caso que `comando1` sea un éxito.
- A comparación con `||`: Este ejecuta `comando2` en caso que `comando1` sea un fallo.

---

**3.** `chgrp <grupo> <archivo o directorio>`:
- Parecido a `chmod`, el comando permite modificar que grupo tiene los permisos en un archivo o directorio.
- Recordar:
	- usuario (`u`), grupo (`g`) y otros (`o`).
	- read (`r`), write (`w`) y execute (`x`).
- En caso de `chmod`, se pueden modificar diversos permisos a la vez, por ejemplo: `chmod u-wx, g+x, o-rwx <directorio o archivo>`.

---

**4.** `chown <usuario> <archivo o directorio>`:
- Parecido a `chmod`, el comando permite modificar el propietario (user) en un archivo o directorio.
- Se puede abreviar el `chgrp` con este comando así: `chown <usuario>:<grupo> <archivo o directorio>`.
	- Esto hace que el user y el group de dicho archivo o directorio cambie a los declarados en el comando.

---

**5.** `useradd <nombre de nuevo usuario> -s <shell que usará> -d <directorio base>`:
 - Comando que sirve para crear un nuevo usuario, se le puede asignar la shell que usará este nuevo usuario como también su directorio de 'inicio'.
 - Para asignarle una contraseña a este nuevo usuario, se usa el siguiente comando: `passwd <nombre del usuario>`.
 - De la misma manera se puede crear nuevos grupos con el simple comando: `groupadd <nombre de nuevo grupo>`.

---

**6.** `usermod -a -G <nombre de grupo> <nombre de usuario>`:
 - Agrega un usuario a un determinado grupo.
 - Se puede confirmar esto ejecutando el siguiente comando: `cat /etc/group | grep <nombre de grupo>`

---

**7.** `chmod +t <directorio>`:
 - **Sticky Bit**: hace que importe más los permisos de los archivos dentro del directorio que los del directorio mismo.
 - Por ejemplo:
	 - Un directorio tiene permisos `777` (`drwxrwxrwx`).
	 - Dentro, hay un archivo con un permiso cualquiera (`.rx-r--r--`).
	 - Si bien no podemos eliminar el archivo directamente, se podría eliminar ya que se tiene permisos de escritura (`w`) en el directorio aplicando simplemente `rm <archivo>`.
	 - Agregando el comando del punto *7*, se podría evitar esto.

---

**8.** `lsattr` y `chattr`:
 - `lsattr`: nos permite listar los atributos asignados a un archivo.
 - `chattr`: nos permite modificar dichos atributos.
 - Por ejemplo, si queremos que un archivo no se pueda modificar o eliminar ni por el usuario root se usa este comando: `chattr +i <archivo>`.
 - Se puede ver más opciones consultar [acá](https://rm-rf.es/chattr-y-lsattr-visualizar-y-modificar-atributos-en-sistemas-de-ficheros-linux/).

---

**9.** `SUID` y `SGID`:
- `SUID`: nos permite ejecutar un archivo como si fuéramos el propietario, independientemente que usuario seamos (por ejemplo, si un archivo fue creado por *root*, entonces si dicho archivo tiene el permiso *SUID*, entonces al ejecutar dicho archivo, lo ejecutaríamos como *root*).
	- Solo funciona en binarios compilados, no en scripts.
	- Se asigna así: `chmod u+s <archivo>` o `chmod 4<permisos actuales en numero> <archivo>`.
	- Se pueden buscar archivos con permiso *SUID* así: `find / -type f -perm -4000 2>/dev/null`.
- `SGID`: de la misma manera que el `SUID`, pero enfocado a grupos.
		- Se asigna así: `chmod g+s <archivo>` o `chmod 2<permisos actuales en número> <archivo>`.
		- Se pueden buscar archivos con permiso *SGID* así: `find / -type f -perm -2000 2>/dev/null`.

---

**10.** `Capabilities`:
- Permiten asignar privilegios específicos a binarios sin darles todos los permisos de `root`.
- Dividen los permisos de `root` en partes más pequeñas (principio de privilegio mínimo).
- Se usan para mejorar la seguridad en el sistema.
- Se pueden listar los binarios con capabilities asignadas con: ``
