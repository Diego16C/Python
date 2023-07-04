import sqlite3

# Clase base AAA
class AAA:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

    def insertar_datos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AAA (attr1, attr2, attr3) VALUES (?, ?, ?)",
                       (self.attr1, self.attr2, self.attr3))
        conn.commit()
        conn.close()

    @staticmethod
    def mostrar_datos():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM AAA")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

# Subclase 1 de AAA
class Subclase1(AAA):
    def __init__(self, attr1, attr2, attr3, attr4, attr5):
        super().__init__(attr1, attr2, attr3)
        self.attr4 = attr4
        self.attr5 = attr5

    def method1(self):
        print("Método 1 de Subclase1")

    def method4(self):
        print("Método 4 de Subclase1")

# Subclase 2 de AAA
class Subclase2(AAA):
    def __init__(self, attr1, attr2, attr3, attr6, attr7):
        super().__init__(attr1, attr2, attr3)
        self.attr6 = attr6
        self.attr7 = attr7

    def method2(self):
        print("Método 2 de Subclase2")

    def method5(self):
        print("Método 5 de Subclase2")

# Subclase 3 de AAA
class Subclase3(AAA):
    def __init__(self, attr1, attr2, attr3, attr8, attr9):
        super().__init__(attr1, attr2, attr3)
        self.attr8 = attr8
        self.attr9 = attr9

    def method3(self):
        print("Método 3 de Subclase3")

    def method6(self):
        print("Método 6 de Subclase3")

# Crear objetos de las subclases
objeto1 = Subclase1("valor1", "valor2", "valor3", "valor4", "valor5")
objeto2 = Subclase2("valor1", "valor2", "valor3", "valor6", "valor7")
objeto3 = Subclase3("valor1", "valor2", "valor3", "valor8", "valor9")

# Ejecutar método sobrescrito
objeto1.method1()
objeto2.method2()
objeto3.method3()

# Insertar datos en la tabla AAA
objeto1.insertar_datos()
objeto2.insertar_datos()
objeto3.insertar_datos()

# Mostrar datos de la tabla AAA
AAA.mostrar_datos()