import os
import xml.etree.ElementTree as ET

class JuegosViejos:
    def __init__(self, archivo):
        self.tree = ET.parse(archivo)
        self.root = self.tree.getroot()

    def obtener_plataformas(self):
        return self.root.find('ListaPlataformas')

    def obtener_juegos(self):
        return self.root.find('ListadoJuegos')

    def mostrar_contenido(self):
        for child in self.root:
            print(child.tag, child.attrib)
            for element in child:
                print(element.tag, element.text)
                
    print("*****************************")
    print("Nombre: Frander Oveldo Carreto Gómez")
    print("Sección: A")
    print("Curso: IPC2")
    print("Carné: 201901371")
    print("*****************************")

# Espera a que el usuario presione una tecla antes de continuar
input()

while True:
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Mostrar el menú
    print("*******************************************************************************")
    print("Bienvenido al menú principal, por favor seleccione una opción:")
    print("1. Carga de archivo XML")
    print("2. Devolver archivo XML ordenado")
    print("3. Salir")
    print("*******************************************************************************")
    # Leer la opción seleccionada
    opcion = input("Ingrese el número de la opción deseada: ")
    # Validar que la opción ingresada sea un número entero válido del 1 al 3
    if not opcion.isdigit() or int(opcion) not in range(1, 4):
        print("Opción inválida. Por favor ingrese un número del 1 al 3.")
        input("Presione cualquier tecla para continuar...")
        continue  
    # Realizar la acción correspondiente
    if opcion == "1":
        print("Seleccionaste la opcion de cargar archivo de XML")
        # Cargar el archivo XML
        juegos_viejos = JuegosViejos('archivo.xml')
        juegos_viejos.mostrar_contenido()
    elif opcion == "2":
        print("Seleccionaste la opción de devolver archivo XML ordenado")
        # Obtener la lista de juegos del archivo XML
        juegos_viejos = JuegosViejos('archivo.xml')
        juegos = juegos_viejos.obtener_juegos().findall('juego')
        # Ordenar los juegos por nombre
        juegos_ordenados = sorted(juegos, key=lambda juego: juego.find('nombre').text)
        # Crear un nuevo árbol XML con los juegos ordenados
        nuevo_arbol = ET.ElementTree(ET.Element('JuegosViejos'))
        lista_juegos = ET.SubElement(nuevo_arbol.getroot(), 'ListadoJuegos')
        for juego in juegos_ordenados:
            lista_juegos.append(juego)
        # Escribir el árbol XML en un archivo
        nuevo_arbol.write('juegos_ordenados.xml', encoding='utf-8', xml_declaration=True)
    elif opcion == "3":
        print("Gracias por usar nuestro programa. ¡Hasta luego!")
        break

    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mostrar mensaje de espera y esperar a que el usuario presione una tecla
    input("Presione cualquier tecla para continuar...")