from zipfile import ZipFile

file = "path_file.zip"
file_path = r"path_folder_lavorazione"


#estraggo sulla cartella
with ZipFile(file, "r") as zip:
        zip.printdir()
        zip.extractall()
  
#ottengo i nomi dei file zip nelle sotto cartelle:        
import os

os.chdir(file_path)
for root, dirs, files in os.walk(file_path):
   for name in files:
      print(os.path.join(name))
      
#creo la lista dei file zip in ogni cartella e sotto cartella:     
list = []
for root, dirs, files in os.walk(file_path):
   for name in files:
      list.append(os.path.join(root, name))
print(list)   

#estraggo files:
#(lo script non riesce ad estrarre tutti i file quindi creo una variabile che mi \\
    #ritorna i file andati in errore -non estratti- per una successiva valutazione)
file_error = [] 
for i in range(len(list)-1):
       try:
           with ZipFile(list[i], "r") as zip:
                   zip.printdir()
                   zip.extractall("Estrazione")  #nomino la nuova cartella di estrazione      
           
       except:
           file_error.append(list[i]) 

#creo la lista senza path:
list_no_path = []
for root, dirs, files in os.walk(file_path):
   for name in files:
      list_no_path.append(name)
print(list_no_path)

#controllo se ogni primo valore delle stringhe che compongono la lista è un numero \\
    # (se numero: fatture elettroniche --> ciò che sto cercando!):
for i in range(len(list_no_path)-1):
    if (list_no_path[i][0]).isdigit():
        first_num = list_no_path[i][0]
        print(type(first_num))
        print("Il primo valore è un numero:" + first_num)

#creo una nuova lista dove inserisco solo le fatture elettroniche:
lista_fatt_electr = []   
for i in range(len(list_no_path)-1):
    if (list_no_path[i][0]).isdigit():     
        x = list_no_path[i]
        lista_fatt_electr.append(x)
    
#creo cartella "estrazione fatt elettroniche"    
directory = "Estrazione Fatture Elettroniche" 
# Path è il path della nuova cartella che sto creando \\
    #sarà uguale al path dove già stiamo lavorando joined la nuova cartella:
path = os.path.join(file_path, directory)
os.mkdir(path)
print("Directory '%s' created" %directory)


#creo lista fatt elect + i path per poi inserirli nella cartella;
    
#path cartella "estrazione"
new_path = r"path_cartlla_estrazione" #dove ho inizialmente estratto i files
lista_final_path = []        
for i in range(len(lista_fatt_electr)-1):
    z = new_path + "\\" + lista_fatt_electr[i] 
    lista_final_path.append(z)


import shutil

for i in range(len(lista_final_path)-1):
    shutil.move(lista_final_path[i], path)
