
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


## Requerimientos del Sistema - Segunda Fase
Esta sección describe los requerimientos funcionales y no funcionales implementados en la segunda fase del sistema de gestión de biblioteca, centrándose en la integración del árbol binario de búsqueda y la optimización de la administración de libros.

## 1. Requerimientos Funcionales
Estos requerimientos definen las funcionalidades específicas del sistema en esta fase.

## - Gestión de Libros con Árbol Binario de Búsqueda (BST)

- El sistema permite almacenar, buscar y eliminar libros utilizando un BST.

- Se garantiza que los libros se organicen de manera ordenada por título dentro del árbol.

- El BST facilita un recorrido en orden ascendente sin necesidad de ordenamiento adicional.

## - Búsqueda de Libros Eficiente

- Implementación de una ruta en FastAPI que permite consultar un libro por su título.

- La búsqueda se realiza directamente en el árbol binario, mejorando la velocidad de respuesta.

- Si el libro no existe, el sistema devuelve un mensaje indicando que "Libro no encontrado".

## - Eliminación de Libros

- Se desarrolla una función que elimina un libro tanto del BST como de la base de datos.

- Si el libro no existe, el sistema muestra un mensaje de error en la interfaz.

- Se maneja adecuadamente la eliminación de nodos con uno o dos hijos en el BST.

## - Devolución de Libros

- Se establece una interfaz donde el usuario ingresa su identificación y el ISBN del libro a devolver.

- Se valida que exista un préstamo activo antes de procesar la devolución.

- Al devolver el libro, se actualiza la base de datos y se confirma con un mensaje en la interfaz.

## - Interfaz Mejorada para Usuarios

- Se diseñan formularios para búsqueda de libros y devolución de préstamos con una estructura clara.

- Se añade validación en JavaScript para evitar envíos de formularios vacíos.

- Se optimizan los estilos en CSS para mejorar la accesibilidad y la experiencia de usuario.

## 2. Requerimientos No Funcionales
Estos requerimientos definen las características técnicas y operativas del sistema en la segunda fase.

-  Eficiencia en Búsqueda y Eliminación

- El BST garantiza un tiempo de búsqueda y eliminación óptimo con una complejidad de O(log n).

- La implementación minimiza el acceso directo a la base de datos, reduciendo costos computacionales.

## - Escalabilidad del Sistema

- El árbol binario permite manejar grandes volúmenes de libros sin afectar el rendimiento.

- Se deja abierta la posibilidad de mejorar la estructura con AVL o Red-Black Trees en futuras mejoras.

## - Integración con FastAPI y Base de Datos

- Se emplea FastAPI para gestionar rutas eficientes.

- La conexión con la base de datos se optimiza para evitar cargas innecesarias de datos.

- Se garantiza que la información de libros y préstamos esté sincronizada con el BST.

## - Manejo de Errores y Validación

- Se implementa un manejo de excepciones en la eliminación de libros, evitando errores inesperados.

- Se validan los formularios en la interfaz para evitar envíos incorrectos o incompletos.

## - Seguridad y Protección de Datos

- Se garantiza que las operaciones de eliminación y búsqueda sean protegidas contra accesos incorrectos.

- Se evita la exposición de datos sensibles en las respuestas de la API.

## NOTA: Se pueden visualizar las pruebas en el documento PDF PRUEBAS


## Creatividad y Alegoría: Don Simian, el Gestor de Biblioteca 🐒

El diseño de este proyecto se inspira en la inteligencia, curiosidad y dinamismo de los monos, convirtiéndolo en una experiencia visualmente atractiva e intuitiva. La paleta de colores empleada mezcla tonos cálidos como amarillo y naranja, simbolizando la energía y creatividad, con verdes y marrones que evocan la conexión natural y el crecimiento intelectual. Estos colores no solo embellecen la interfaz, sino que crean un ambiente amigable y acogedor.

En el corazón del sistema está **Don Simian**, un carismático mono gestor que representa el ingenio y la organización detrás de la gestión bibliotecaria. Con una actitud simpática y divertida, Don Simian guía a los usuarios durante el proceso de gestión de libros, usuarios y préstamos, asegurando que interactuar con el sistema sea sencillo y ameno.

Cada aspecto visual y narrativo del proyecto, desde los colores hasta las funcionalidades, refleja el espíritu juguetón pero eficiente de Don Simian. Esta integración creativa convierte al sistema en más que una simple herramienta: es una experiencia interactiva diseñada para ser funcional, cautivadora y agradable para los usuarios.

------------------------------------------------------------------
Requerimientos del Sistema gestion de  biblioteca de don simian - Tercera Fase
1. Requerimientos Funcionales
1.1. Gestión de Datos en SQLite

El sistema debe almacenar información sobre libros, usuarios y préstamos en una base de datos SQLite.

Debe permitir la creación, actualización, eliminación y consulta de registros en cada tabla.

Las consultas de libros y usuarios deben ejecutarse con filtros y criterios definidos para mejorar la eficiencia.

1.2. Implementación de Grafos

El sistema debe integrar una estructura de grafo dirigido para representar las relaciones entre usuarios y libros.

Se debe permitir la inserción de nodos (usuarios y libros) y aristas (préstamos).

Las operaciones de eliminación deben actualizar tanto la base de datos como el grafo de manera sincronizada.

Los usuarios deben poder buscar relaciones entre libros y usuarios de forma eficiente.

Se debe generar un análisis de popularidad basado en la estructura del grafo.

1.3. Búsqueda Avanzada en el Sistema

La interfaz debe permitir búsquedas de préstamos activos mediante consultas en el grafo.

Los resultados deben ser presentados en una interfaz clara y accesible.

Los usuarios deben poder acceder a recomendaciones basadas en relaciones dentro del grafo.

1.4. Administración de Préstamos y Devoluciones

Cuando un préstamo se registra, debe reflejarse en el grafo y en la base de datos.

Al realizar una devolución, se debe eliminar la conexión entre usuario y libro en ambas estructuras.

La interfaz debe notificar al usuario los cambios realizados en tiempo real.

2. Requerimientos No Funcionales
2.1. Rendimiento y Escalabilidad

El sistema debe realizar consultas en SQLite y en el grafo en menos de un segundo para garantizar eficiencia.

La estructura de datos utilizada debe permitir manejar grandes volúmenes de información sin pérdida de rendimiento.

2.2. Seguridad y Consistencia

Se deben implementar restricciones en la base de datos para evitar duplicidad de registros.

Los cambios en préstamos y devoluciones deben estar sincronizados correctamente para evitar inconsistencias en los datos.

2.3. Usabilidad e Interfaz

La interfaz debe ser intuitiva, con opciones claras para que los usuarios gestionen libros y préstamos.

La navegación debe seguir un diseño que facilite el acceso a las funciones principales sin necesidad de configuraciones avanzadas.

2.4. Mantenimiento y Expansión

La estructura del sistema debe permitir futuras actualizaciones, como la inclusión de análisis avanzados sobre tendencias de préstamos.

La documentación debe ser clara para facilitar el mantenimiento y la incorporación de mejoras en futuras versiones.


##Conclusión General
Este sistema bibliotecario ahora es rápido, robusto y fácil de usar, integrando lo mejor de estructuras de datos y modelos matemáticos para optimizar la gestión de préstamos. La incorporación de grafos ha transformado el proceso de consulta en una experiencia más eficiente, permitiendo mejorar la búsqueda y administración de usuarios dentro de la biblioteca.
Con esta versión final, el sistema no solo cumple con los objetivos académicos del proyecto, sino que también representa una solución tecnológica lista para ser ampliada en futuros desarrollos. Las siguientes mejoras podrían incluir sistemas de recomendación basados en patrones de préstamo e integración con visualización gráfica de los datos.



## Referencias bibliograficas
- Tiangolo, S. (2025). FastAPI: High performance, easy to learn, fast to code, ready for production. Recuperado de FastAPI.

- Szalontay, P. (2024). Building a Production-Ready Python FastAPI Project Template. Recuperado de GetLazy.ai.

- Bouchrika, I. (2025). 20 Best Library Management Software for 2025. Recuperado de Research.com.

- Sharma, S. (2023). 7 Best Open Source Library Management Software. Recuperado de It's FOSS.

- Forrester, R. (2025). Top 5 Library Management Software Solutions for 2025. Recuperado de Five.co.
