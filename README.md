## Actividad 2 - Proyecto: Sistema de gestión de biblioteca

Nombre
Salome Ramirez Sanchez

Cuarto Semestre


Corporación Universitaria Iberoamericana

Estructuras de Datos

Docente (William Ruiz)

Fecha (26 de Marzo del 2025)

Bogotá D.C


## Introducción
El presente proyecto, titulado "Sistema de Gestión de Biblioteca de Don Simian", ha sido desarrollado con el propósito de optimizar la administración de recursos bibliográficos a través de un sistema eficiente, creativo y fácil de usar. Este sistema integra la gestión de libros, usuarios y préstamos, permitiendo a los administradores llevar un control detallado sobre el inventario de libros, el registro de usuarios y el seguimiento de préstamos activos.

Implementado con tecnologías como FastAPI para el backend, SQLAlchemy para la gestión de bases de datos relacionales, y una interfaz en HTML con apoyo de CSS y JavaScript, el proyecto asegura una interacción fluida entre los componentes. La base de datos está estructurada de manera robusta para garantizar la integridad de las relaciones entre libros, usuarios y préstamos mediante el uso de claves foráneas y restricciones.

Además, el sistema incluye funcionalidades completas de CRUD (Crear, Leer, Actualizar y Eliminar) para cada uno de los módulos principales e implementacion efectiva de estructuras de datos lineales:

- **Libros**: Administración del catálogo, validación de datos únicos como ISBN y edición de información clave.

- **Usuarios**: Gestión del registro y actualización de datos personales con validación para evitar duplicados.

- **Préstamos**: Control de relaciones entre libros y usuarios mediante referencias en la base de datos, con opciones para registrar, modificar y eliminar préstamos.

Este informe detalla los procesos técnicos, las decisiones de diseño, las tecnologías utilizadas y las funcionalidades del sistema, brindando una visión completa del desarrollo y su impacto en lo que es la gestión bibliotecaria.



## Requerimientos Funcionales

1. **Gestión de Libros**
   - Permitir registrar nuevos libros con datos como título, autor, ISBN, editorial y año de publicación.
   - Validar que el ISBN sea único para evitar duplicados.
   - Posibilitar la edición y eliminación de registros de libros existentes.
   - Mostrar una lista completa de libros registrados.

2. **Gestión de Usuarios**
   - Permitir registrar nuevos usuarios con datos como nombre y número de identificación.
   - Validar que el nombre no se duplique en los registros existentes.
   - Posibilitar la edición del nombre y la identificación de un usuario existente.
   - Permitir la eliminación de usuarios.

3. **Gestión de Préstamos**
   - Registrar préstamos vinculando usuarios y libros mediante claves foráneas (usuario_id y libro_id).
   - Validar que tanto el usuario como el libro existan antes de crear un préstamo.
   - Mostrar la lista de préstamos activos, con detalles del usuario y el libro involucrado.
   - Posibilitar la edición y eliminación de préstamos existentes.

4. **Interfaz de Usuario**
   - Proporcionar formularios para realizar operaciones como crear, editar y eliminar registros (libros, usuarios, préstamos).
   - Mostrar mensajes dinámicos como confirmaciones, errores y alertas en la interfaz.
   - Agregar modales interactivos para editar registros desde la tabla de visualización.

---

## Requerimientos No Funcionales

1. **Usabilidad**
   - La interfaz debe ser intuitiva y fácil de usar, incluso para usuarios con conocimientos básicos de informática.
   - Los botones y formularios deben estar claramente etiquetados y accesibles.

2. **Escalabilidad**
   - El sistema debe ser capaz de manejar un número creciente de libros, usuarios y préstamos sin pérdida de rendimiento.

3. **Seguridad**
   - Implementar validaciones de datos para evitar duplicados y garantizar la integridad de las relaciones entre tablas.
   - Proteger la conexión a la base de datos mediante credenciales seguras.
   - Manejar los errores de manera segura para evitar que información sensible sea expuesta.

4. **Compatibilidad**
   - La interfaz debe ser compatible con los navegadores más comunes como Chrome, Firefox y Edge.
   - El sistema debe funcionar en distintos tamaños de pantalla (responsivo).

5. **Rendimiento**
   - Las operaciones de consulta, inserción, actualización y eliminación deben ejecutarse rápidamente, incluso con bases de datos extensas.

6. **Mantenibilidad**
   - El código debe estar organizado y documentado para facilitar futuras modificaciones o expansiones.
   - Las dependencias y configuraciones deben ser actualizadas regularmente.


## NOTA: Se pueden visualizar las pruebas en el documento PDF PRUEBAS


## Creatividad y Alegoría: Don Simian, el Gestor de Biblioteca 🐒

El diseño de este proyecto se inspira en la inteligencia, curiosidad y dinamismo de los monos, convirtiéndolo en una experiencia visualmente atractiva e intuitiva. La paleta de colores empleada mezcla tonos cálidos como amarillo y naranja, simbolizando la energía y creatividad, con verdes y marrones que evocan la conexión natural y el crecimiento intelectual. Estos colores no solo embellecen la interfaz, sino que crean un ambiente amigable y acogedor.

En el corazón del sistema está **Don Simian**, un carismático mono gestor que representa el ingenio y la organización detrás de la gestión bibliotecaria. Con una actitud simpática y divertida, Don Simian guía a los usuarios durante el proceso de gestión de libros, usuarios y préstamos, asegurando que interactuar con el sistema sea sencillo y ameno.

Cada aspecto visual y narrativo del proyecto, desde los colores hasta las funcionalidades, refleja el espíritu juguetón pero eficiente de Don Simian. Esta integración creativa convierte al sistema en más que una simple herramienta: es una experiencia interactiva diseñada para ser funcional, cautivadora y agradable para los usuarios.


## Conclusión

El "Sistema de Gestión de Biblioteca de Don Simian" representa una solución eficiente y moderna para administrar los recursos bibliográficos de manera estructurada. Este proyecto integra funcionalidades clave como la gestión de libros, usuarios y préstamos, proporcionando una interfaz intuitiva y herramientas robustas para garantizar la integridad de los datos.

El uso de tecnologías como **FastAPI**, **SQLAlchemy** y una interfaz basada en **HTML**, **CSS** y **JavaScript** asegura un sistema dinámico, escalable y fácil de mantener. Además, las relaciones entre tablas en la base de datos refuerzan la consistencia de la información almacenada.

Este sistema no solo simplifica las operaciones diarias de una biblioteca, sino que también fomenta una experiencia de usuario agradable gracias a una interfaz amigable y mensajes claros que guían al administrador en cada paso. Con una base sólida, este proyecto está preparado para escalar y adaptarse a futuras necesidades, siendo una herramienta invaluable para cualquier entorno bibliotecario.  
