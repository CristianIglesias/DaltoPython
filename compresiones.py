import os
import zipfile

ruta="C:/Users/ADMDell/Desktop/TODO"
rutaLocal=os.path.dirname(__file__)
os.chdir(ruta)

matchlist = ['.pdf' , '.txt', '.png' , '.py', '.docx', '.xlsx']

with zipfile.ZipFile('comprimidos.zip','w') as zip:
    for archivo in os.listdir():
        for ext in matchlist:
            if archivo.endswith(ext):
                zip.write(os.path.join(rutaLocal,archivo))

zip.close()



