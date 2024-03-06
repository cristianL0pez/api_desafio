import csv

# Genera una lista de 10 datos distintos
datos = [
    {"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz", "street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough", "zipcode": "92998-3874", "lat": "-37.3159", "lng": "81.1496"},
    {"id": 2, "name": "Ervin Howell", "username": "Antonette", "email": "Shanna@melissa.tv", "street": "Victor Plains", "suite": "Suite 879", "city": "Wisokyburgh", "zipcode": "90566-7771", "lat": "-43.9509", "lng": "-34.4618"},
    {"id": 3, "name": "Clementine Bauch", "username": "Samantha", "email": "Nathan@yesenia.net", "street": "Douglas Extension", "suite": "Suite 847", "city": "McKenziehaven", "zipcode": "59590-4157", "lat": "-68.6102", "lng": "-47.0653"},
    {"id": 4, "name": "Patricia Lebsack", "username": "Karianne", "email": "Julianne.OConner@kory.org", "street": "Hoeger Mall", "suite": "Apt. 692", "city": "South Elvis", "zipcode": "53919-4257", "lat": "29.4572", "lng": "-164.2990"},
    {"id": 5, "name": "Chelsey Dietrich", "username": "Kamren", "email": "Lucio_Hettinger@annie.ca", "street": "Skiles Walks", "suite": "Suite 351", "city": "Roscoeview", "zipcode": "33263", "lat": "-31.8129", "lng": "62.5342"},
    {"id": 6, "name": "Mrs. Dennis Schulist", "username": "Leopoldo_Corkery", "email": "Karley_Dach@jasper.info", "street": "Norberto Crossing", "suite": "Apt. 950", "city": "South Christy", "zipcode": "23505-1337", "lat": "-71.4197", "lng": "71.7478"},
    {"id": 7, "name": "Kurtis Weissnat", "username": "Elwyn.Skiles", "email": "Telly.Hoeger@billy.biz", "street": "Rex Trail", "suite": "Suite 280", "city": "Howemouth", "zipcode": "58804-1099", "lat": "24.8918", "lng": "21.8984"},
    {"id": 8, "name": "Nicholas Runolfsdottir V", "username": "Maxime_Nienow", "email": "Sherwood@rosamond.me", "street": "Ellsworth Summit", "suite": "Suite 729", "city": "Aliyaview", "zipcode": "45169", "lat": "-14.3990", "lng": "-120.7677"},
    {"id": 9, "name": "Glenna Reichert", "username": "Delphine", "email": "Chaim_McDermott@dana.io", "street": "Dayna Park", "suite": "Suite 449", "city": "Bartholomebury", "zipcode": "76495-3109", "lat": "24.6463", "lng": "-168.8889"},
    {"id": 10, "name": "Clementina DuBuque", "username": "Moriah.Stanton", "email": "Rey.Padberg@karina.biz", "street": "Kattie Turnpike", "suite": "Suite 198", "city": "Lebsackbury", "zipcode": "31428-2261", "lat": "-38.2386", "lng": "57.2232"}
]

# Escribe los datos en un archivo CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = datos[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for dato in datos:
        writer.writerow(dato)

print("Datos CSV creados exitosamente")