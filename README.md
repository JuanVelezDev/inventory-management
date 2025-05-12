# 📦 Inventory Manager en Python

Este es un programa simple de consola en Python para gestionar productos en un inventario. Es ideal para practicar los fundamentos de programación: **variables, listas, diccionarios, operadores lógicos, operadores relacionales, condicionales, funciones y manejo de errores**.

---

## 📌 Funcionalidades

- 📥 Agregar un producto
- 🔍 Buscar producto por nombre
- 🔄 Actualizar el precio de un producto
- ❌ Eliminar un producto
- 💰 Calcular el valor total del inventario
- 📋 Mostrar todos los productos
- 🚪 Salir del programa

---

## 🧠 Fundamentos de Programación Utilizados

| Concepto                 | Aplicación en el código                                      |
|--------------------------|--------------------------------------------------------------|
| Variables                | `name`, `price`, `quantity`, etc.                            |
| Diccionarios             | `inventory = {}`                                             |
| Tuplas                   | `(precio, cantidad)` como valor del diccionario              |
| Condicionales            | `if`, `else`, `elif`                                         |
| Operadores relacionales  | `in`, `==`                                                   |
| Operadores lógicos       | implícitos en condiciones (`and`, `or`)                      |
| Funciones                | Definidas con `def`                                          |
| Bucles                   | `while True`                                                 |
| Manejo de errores        | `try-except` en entradas de usuario                         |
| Funciones lambda         | `lambda item: item[0] * item[1]`                             |
| Funciones de orden superior | `map()`, `sum()`                                        |
| Entrada del usuario      | `input()` con validación                                     |

---

## # 📦 Inventory Management Program (Python)

Este programa es un sistema básico de gestión de inventario escrito en Python, ideal para practicar los fundamentos de programación: **variables, condicionales, operadores, diccionarios, funciones y manejo de errores**.

---

## 🧠 1. Diccionario de Inventario
```python
inventory = {}

    Se crea un diccionario vacío llamado inventory.

    Cada clave (key) será el nombre del producto.

    Cada valor (value) será una tupla con (precio, cantidad).

🧩 2. Función: Agregar Producto

def add_product(name, price, quantity):
    if name in inventory:
        print("Product already exists.")
    else:
        inventory[name] = (price, quantity)
        print(f"Product '{name}' added successfully.")

    Verifica si el producto existe usando in.

    Si no está, lo agrega con una tupla (precio, cantidad).

🔍 3. Función: Buscar Producto

def search_product(name):
    if name in inventory:
        price, quantity = inventory[name]
        print(f"Product: {name}")
        print(f"Price: ${price}")
        print(f"Quantity: {quantity}")
    else:
        print("Product not found.")

    Muestra precio y cantidad si el producto existe.

🔄 4. Función: Actualizar Precio

def update_price(name, new_price):
    if name in inventory:
        _, quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f"Price of '{name}' updated successfully.")
    else:
        print("Product not found.")

    Reemplaza solo el precio, conservando la cantidad.

❌ 5. Función: Eliminar Producto

def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' deleted successfully.")
    else:
        print("Product not found.")

    Elimina el producto del diccionario.

💰 6. Función: Calcular Valor Total

def calculate_total_value():
    total_value = sum(map(lambda item: item[0] * item[1], inventory.values()))
    print(f"Total inventory value: ${total_value}")

    Usa lambda, map y sum para multiplicar y sumar:

        precio * cantidad para cada producto.

🛡️ 7. Funciones: Entrada Segura
Float:

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

Int:

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

    Validan que el usuario escriba un número correcto.

🧭 8. Menú Principal

def main():
    while True:
        print("1. Add product")
        ...
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            ...
        elif choice == "6":
            break
        else:
            print("Invalid option.")

    Muestra un menú de opciones en bucle infinito.

    Según la opción (choice), llama a la función correspondiente.

🏁 9. Ejecución

main()
python inventory_manager.py
