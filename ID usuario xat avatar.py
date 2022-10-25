import json
import requests
import os
import pathlib






usuario_xat = input("Escribe el ID del usuario de xat: ")



response = requests.get(f"https://xat.com/web_gear/chat/profile2.php?i={usuario_xat}")





#Programado Por Jose89fcb
#Mi twitter: https://twitter.com/jose89fcb








avatar = response.json()['Err']['Media']['avatar']


nombre_local_imagen = f"{usuario_xat}.png"

pathlib.Path(f"{usuario_xat}").mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),f"{usuario_xat}")) 


imagen = requests.get(avatar).content


    
   
with open(nombre_local_imagen, 'wb') as handler:
    handler.write(imagen)


print(f"{avatar}")
  