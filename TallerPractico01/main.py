# Principio de Responsabilidad Única (SRP)
class Alumno:
    def __init__(self, nombre, edad, rut, fecha_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas = {}
    
    def agregar_asignatura(self, asignatura):
        self.asignaturas[asignatura.codigo] = {'asignatura': asignatura, 'nota': None}
        print(f"Asignatura {asignatura.nombre} agregada al alumno {self.nombre}")

    def asignar_nota(self, codigo_asignatura, nota):
        if codigo_asignatura in self.asignaturas:
            self.asignaturas[codigo_asignatura]['nota'] = nota
            print(f"Nota {nota} asignada en {codigo_asignatura} para el alumno {self.nombre}")
        else:
            print("Asignatura no encontrada")

    def descargar_notas(self):
        print(f"Notas de {self.nombre}:")
        for info in self.asignaturas.values():
            asignatura = info['asignatura']
            nota = info['nota']
            print(f"{asignatura.nombre} ({asignatura.codigo}): {'Sin nota' if nota is None else nota}")


# Principio OCP + LSP
class Alumni(Alumno):
    def actividad(self):
        print(f"{self.nombre} es titulado. No estudia ni hace ayudantías.")


class EstudiantesNoAyudantes(Alumno):
    def actividad(self):
        print(f"{self.nombre} estudia.")


class EstudiantesAyudante(Alumno):
    def actividad(self):
        print(f"{self.nombre} estudia y hace ayudantías.")


class EstudianteMagister(Alumno):
    def actividad(self):
        print(f"{self.nombre} estudia y hace clases.")


class EstudianteDoctorado(Alumno):
    def actividad(self):
        print(f"{self.nombre} estudia, hace clases e investiga.")


# Asignaturas (con clasificación por nivel)
class Asignatura:
    def __init__(self, nombre, codigo, creditos, nivel):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nivel = nivel  # Pregrado, Magister, Doctorado


# Repositorio de Alumnos
class RepositorioAlumnos:
    def __init__(self):
        self.base = {}

    def agregar(self, alumno):
        self.base[alumno.rut] = alumno
        print(f"Alumno {alumno.nombre} agregado.")

    def obtener(self, rut):
        return self.base.get(rut, None)

    def eliminar(self, rut):
        if rut in self.base:
            del self.base[rut]
            print(f"Alumno con RUT {rut} eliminado.")
        else:
            print("Alumno no encontrado.")

    def modificar(self, rut, **kwargs):
        alumno = self.obtener(rut)
        if alumno:
            for key, value in kwargs.items():
                if hasattr(alumno, key):
                    setattr(alumno, key, value)
            print(f"Alumno {rut} modificado.")
        else:
            print("Alumno no encontrado.")


# Repositorio de Asignaturas
class RepositorioAsignaturas:
    def __init__(self):
        self.base = {}

    def agregar(self, asignatura):
        self.base[asignatura.codigo] = asignatura
        print(f"Asignatura {asignatura.nombre} agregada.")

    def obtener(self, codigo):
        return self.base.get(codigo, None)

    def eliminar(self, codigo):
        if codigo in self.base:
            del self.base[codigo]
            print(f"Asignatura con código {codigo} eliminada.")
        else:
            print("Asignatura no encontrada.")

    def modificar(self, codigo, **kwargs):
        asignatura = self.obtener(codigo)
        if asignatura:
            for key, value in kwargs.items():
                if hasattr(asignatura, key):
                    setattr(asignatura, key, value)
            print(f"Asignatura {codigo} modificada.")
        else:
            print("Asignatura no encontrada.")


# ====================
# ===== EJEMPLO ======
# ====================
if __name__ == "__main__":
    alumnos_repo = RepositorioAlumnos()
    asignaturas_repo = RepositorioAsignaturas()

    # Crear asignaturas
    asig1 = Asignatura("POO", "INF123", 5, "Pregrado")
    asig2 = Asignatura("Investigación Avanzada", "DOC456", 10, "Doctorado")
    asignaturas_repo.agregar(asig1)
    asignaturas_repo.agregar(asig2)

    # Crear alumno
    alumno1 = EstudianteDoctorado("Camila", 30, "12345678-9", "1993-04-15")
    alumnos_repo.agregar(alumno1)

    # Asignar asignaturas y notas
    alumno1.agregar_asignatura(asig1)
    alumno1.agregar_asignatura(asig2)
    alumno1.asignar_nota("INF123", 6.5)
    alumno1.asignar_nota("DOC456", 7.0)

    alumno1.descargar_notas()
    alumno1.actividad()




















        








        








        