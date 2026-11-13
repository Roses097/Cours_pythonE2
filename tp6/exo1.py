from pymongo import MongoClient
database = MongoClient ('mongodb://localhost:27017')


db = database.tp6

### 1
for r in db.baccalaureat.find({"academie": "NORMANDIE"}).limit(2):
    print(r)
print("\n\n\n")


#### 2
for ac in db.baccalaureat.distinct("academie"):
    print(ac)
print("\n\n\n")


### 3
                                                                    #sort -1 pour high to low (1 for low to high)
for doc in db.baccalaureat.find({"sexe": "MASCULIN"}).sort("nombre_d_inscrits",-1).limit(10):
    print(f"")
    
print("\n\n\n")

### 4
for serie in db.baccalaureat.find({"sexe": "MASCULIN"}).sort("nombre_d_inscrits", -1).limit(10):
    
    print(f"{serie['session']} - {serie['academie']} - {serie['serie']} - {serie['nombre_d_inscrits']}")


#### 4
print("\n\n\n")
academies = {}
for serie in db.baccalaureat.find({"sexe": "FEMININ"}):
    
    aca_nom = serie["academie"]
    
    if aca_nom not in academies:
        academies[aca_nom] = serie["nombre_d_inscrits"]
        continue
    
    academies[aca_nom] += serie["nombre_d_inscrits"]

for ac, ins in academies.items():
    print(ac, ins)
