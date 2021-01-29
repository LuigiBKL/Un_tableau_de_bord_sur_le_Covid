import pandas as pd

def import_dataset():

    dataset = pd.read_csv('C:/Users/utilisateur/Documents/microsoft_ia/Devoirs/Un_tableau_de_bord_sur_le_Covid/donnees-hospitalieres-covid19-2021-01-21-19h03.csv',sep = ';')
    return dataset

def traitement_dataset():

    donnees = []
    dataset = import_dataset()
    dep = dataset["dep"]
    liste_dep = []
   
    for i in dep:
        if i not in liste_dep:
            liste_dep.append(i)
    
    gpr_dep = dataset.groupby('dep')  

    dc = (gpr_dep.apply(lambda x: x[x['sexe'] == 0]['dc'].max()))
    rea = (gpr_dep.apply(lambda x: x[x['sexe'] == 0]['rea'].max()))
    rad = (gpr_dep.apply(lambda x: x[x['sexe'] == 0]['rad'].max()))
    hosp = (gpr_dep.apply(lambda x: x[x['sexe'] == 0]['hosp'].max()))
   
    

    donnees = [liste_dep,dc.tolist(),rea.tolist(),rad.tolist(),hosp.tolist()]


    return donnees
    
a = traitement_dataset()
print(a)
    


