from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv

app = FastAPI()

# Definir un modelo Pydantic para los datos del usuario
class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    street: str
    suite: str
    city: str
    zipcode: str
    lat: str
    lng: str

# Leer los datos del archivo CSV
def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [User(**row) for row in reader]
    return data

# Obtener todos los usuarios
@app.get("/users/")
async def get_all_users():
    return read_csv('data.csv')

# Obtener un usuario por su ID
@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    users_data = read_csv('data.csv')
    for user in users_data:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Agregar un nuevo usuario
@app.post("/users/")
async def create_user(user: User):
    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=user.dict().keys())
        writer.writerow(user.dict())
    return user

# Actualizar un usuario existente
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    users_data = read_csv('data.csv')
    for i, item in enumerate(users_data):
        if item.id == user_id:
            users_data[i] = user
            break
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=user.dict().keys())
        writer.writeheader()
        writer.writerows([item.dict() for item in users_data])
    
    return user

# Eliminar un usuario existente
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    users_data = read_csv('data.csv')
    updated_data = [user for user in users_data if user.id != user_id]
    
    if len(updated_data) == len(users_data):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=updated_data[0].dict().keys())
        writer.writeheader()
        writer.writerows([user.dict() for user in updated_data])
    
    return {"message": "Usuario eliminado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)














