import os
import zipfile

ruta="C:/Users/ADMDell/Downloads"
rutaLocal=os.path.dirname(__file__)
os.chdir(ruta)

matchlist = ['.pdf' , '.txt', '.png' , '.py', '.docx', '.xlsx']

with zipfile.ZipFile('comprimidos.zip','w') as zip:
    for archivo in os.listdir():
        for ext in matchlist:
            if archivo.endswith(ext):
                zip.write(os.path.join(ruta,archivo))
                print(f'se agregó {archivo} a la carpeta comprimida')
zip.close()



