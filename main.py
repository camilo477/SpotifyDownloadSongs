import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Ruta completa de spotdl obtenida del comando `where spotdl`
spotdl_path = r"C:\Users\camil\AppData\Local\Programs\Python\Python312\Scripts\spotdl.exe"
# Variable global para almacenar la carpeta de destino
carpeta_destino = ""

# Función para seleccionar la carpeta de destino
def seleccionar_carpeta_destino():
    global carpeta_destino
    carpeta_destino = filedialog.askdirectory()
    if carpeta_destino:
        messagebox.showinfo("Carpeta seleccionada", f"La carpeta de destino seleccionada es:\n{carpeta_destino}")

# Función que se ejecuta al presionar el botón de aceptar
def ejecutar_comando():
    link = entrada_link.get()
    if link:
        try:
            # Verificar si se ha seleccionado una carpeta de destino
            if not carpeta_destino:
                messagebox.showwarning("Advertencia", "Por favor, selecciona una carpeta de destino primero.")
                return

            # Ejecutar el comando spotdl (link) con la opción correcta --output
            subprocess.run([spotdl_path, "--output", carpeta_destino, link], check=True)
            messagebox.showinfo("Éxito", f"Comando ejecutado correctamente. Los archivos se han guardado en:\n{carpeta_destino}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error al ejecutar el comando: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"No se encontró el archivo especificado: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce un enlace")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descargar Música")

# Crear y colocar los widgets
titulo = tk.Label(ventana, text="Descargar Música")
titulo.pack(pady=10)

etiqueta_link = tk.Label(ventana, text="Enlace:")
etiqueta_link.pack(pady=5)

entrada_link = tk.Entry(ventana, width=50)
entrada_link.pack(pady=5)

boton_carpeta = tk.Button(ventana, text="Seleccionar Carpeta Destino", command=seleccionar_carpeta_destino)
boton_carpeta.pack(pady=10)

boton_aceptar = tk.Button(ventana, text="Aceptar", command=ejecutar_comando)
boton_aceptar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()