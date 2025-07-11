# TallerPractico01
# Taller Práctico 1 - Principios SOLID

## 🎓 Universidad de Valparaíso  
**Asignatura:** Metodología de Diseño  
**Alumno:** Lucas Orellana, 21.275.378-5
            Angel Pino, 26.110.472-5
---

## 📌 Descripción del sistema

Este proyecto simula un sistema de gestión de estudiantes y asignaturas para el Aula Virtual de la UV. Permite realizar las siguientes acciones:

- Crear, modificar, obtener y eliminar **alumnos** y **asignaturas**.
- Asignar asignaturas a los alumnos.
- Registrar y descargar **notas** de los alumnos por asignatura.
- Clasificar estudiantes por tipo (Titulados, Estudiantes, Magíster, Doctorado).
- Clasificar asignaturas por nivel (Pregrado, Magíster, Doctorado).

---

## ✅ Supuestos realizados

- Las asignaturas **no tienen prerrequisitos** y cualquier estudiante puede tomarlas, pero cada una se clasifica por un nivel académico.
- La base de datos se simula con diccionarios (`dict`) y operaciones `print()` como indica el enunciado.
- Un alumno puede tener múltiples asignaturas, pero no puede tener dos con el mismo código.
- El sistema es de prueba y no contiene validaciones avanzadas como control de errores, fechas ni formatos estrictos de RUT o fecha de nacimiento.

---

## 🧠 Principios SOLID aplicados

### 1.- Principio de Responsabilidad Única (SRP)**
- Cada clase tiene una única responsabilidad.
  - `Alumno` gestiona sus datos y asignaturas.
  - `RepositorioAlumnos` y `RepositorioAsignaturas` manejan la persistencia (simulada).
  - `Asignatura` solo modela la información de una asignatura.

---

### 2.- Principio Abierto/Cerrado (OCP)**
- El sistema puede extenderse agregando nuevos tipos de estudiantes sin modificar las clases existentes.
- Se usan subclases como `EstudianteDoctorado`, `EstudiantesAyudante`, etc., para añadir comportamientos específicos.

---

### 3.- Principio de Sustitución de Liskov (LSP)**
- Las subclases de `Alumno` pueden reemplazar a `Alumno` en cualquier parte del código sin afectar su funcionamiento.

---

### 4.- Principio de Segregación de Interfaces (ISP)**
- Aunque Python no tiene interfaces explícitas, las clases están bien divididas.
  - `Alumno` no está obligado a implementar funciones de base de datos.
  - Las funcionalidades están separadas por repositorios.

---

### 5.- Principio de Inversión de Dependencias (DIP)**
- El sistema depende de abstracciones simples (`dict`, funciones de repositorio).
- Si se quisiera usar una base de datos real, bastaría con cambiar la implementación del repositorio sin tocar el resto del código.

---

## ▶️ Instrucciones de ejecución

Este proyecto no requiere librerías externas.

Para ejecutarlo, simplemente corre el archivo:

```bash
python main.py
