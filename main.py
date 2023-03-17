import csv
import sys
archivo = 'dat.csv'
# Abrir el archivo CSV y leerlo con la función csv.DictReader
with open(archivo, newline='') as f:
    reader = csv.DictReader(f)

    # Recorrer las filas del archivo CSV y generar las sentencias INSERT INTO
    sql = []
    for row in reader:
        # Validar cada una de las columnas y eliminar saltos de línea
        id = row['id'].replace('\n', '') and row['id'].replace("'","")  if row['id'] != '' else '0'
        brandId = row['brandId'].replace('\n', '') if row['brandId'] != '' else '0'
        product_name = row['product_name'].replace('\n', '') and row['product_name'].replace("'", '')  if row['product_name'] != '' else '0'
        model = row['model'].replace('\n', '') if row['model'] != '' else '0'
        uploadRetailPrice = row['uploadRetailPrice'].replace('\n', '') if row['uploadRetailPrice'] != '' else '0'
        measuringUnitId = row['measuringUnitId'].replace('\n', '') if row['measuringUnitId'] != '' else '0'
        isActive  = row['isActive'].replace('\n', '') if row['isActive'] != '' else '0'
        isKit  = row['isKit'].replace('\n', '') if row['isKit'] != '' else '0'

       

        # Generar la sentencia INSERT INTO y agregarla a la lista de sentencias
        sql.append(f"INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES ({id},{brandId}, '{product_name}', '{model}', {uploadRetailPrice}, {measuringUnitId}, {isActive}, {isKit});")

# Escribir las sentencias INSERT INTO en un archivo .sql
with open('inserts.sql', 'w') as f:
    f.write('\n'.join(sql))


# Abrir el archivo CSV y leerlo con la función csv.DictReader
with open(archivo, newline='') as f:
    reader = csv.DictReader(f)

    # Recorrer las filas del archivo CSV y generar las sentencias INSERT INTO
    sql = []
    for row in reader:
        # Validar cada una de las columnas y eliminar saltos de línea
        productId = row['id'].replace('\n', '') if row['id'] != '' else '0'
        priceCost = row['baseCost'].replace('\n', '') if row['baseCost'] != '' else '0'
        supplierId = row['supplierId'].replace('\n', '') if row['supplierId'] != '' else '0'
        
        # Verificar si todas las columnas están vacías
        if productId == '0' and priceCost == '0' and supplierId == '0':
            print("Error: Todas las columnas están vacías en la fila actual.")
            break

        # Generar la sentencia INSERT INTO y agregarla a la lista de sentencias
        sql.append(f"INSERT INTO `ProductSupplier` (`productId`, `priceCost`, `supplierId`) VALUES ({productId},{priceCost}, {supplierId});")

# Escribir las sentencias INSERT INTO en un archivo .sql
with open('inserts2.sql', 'w') as f:
    f.write('\n'.join(sql))


    # Abrir el archivo CSV y leerlo con la función csv.DictReader
with open(archivo, newline='') as f:
    reader = csv.DictReader(f)

    # Recorrer las filas del archivo CSV y generar las sentencias INSERT INTO
    sql = []
    for row in reader:
        # Validar cada una de las columnas y eliminar saltos de línea
        productId = row['id'].replace('\n', '') if row['id'] != '' else '0'
        tagId = row['tagId'].replace('\n', '') if row['tagId'] != '' else '0'
        
        
        # Verificar si todas las columnas están vacías
        if productId == '0' and priceCost == '0':
            print("Error: Todas las columnas están vacías en la fila actual.")
            break

        # Generar la sentencia INSERT INTO y agregarla a la lista de sentencias
        sql.append(f"INSERT INTO `ProductTag` (`productId`, `tagId`) VALUES ({productId},{tagId});")

# Escribir las sentencias INSERT INTO en un archivo .sql
with open('inserts3.sql', 'w') as f:
    f.write('\n'.join(sql))


# Abrir el archivo CSV y leerlo con la función csv.DictReader
with open(archivo, newline='') as f:
    reader = csv.DictReader(f)

    # Recorrer las filas del archivo CSV y generar las sentencias INSERT INTO
    sql = []
    for row in reader:
        # Validar cada una de las columnas y eliminar saltos de línea
        productId = row['id'].replace('\n', '') if row['id'] != '' else '0'
        maxQuantity = row['quantity'].replace('\n', '') if row['quantity'] != '' else '0'
        productId=productId.strip()
        maxQuantity=maxQuantity.strip()
        
        # Verificar si todas las columnas están vacías
        if productId == '0' and maxQuantity == '0':
            print("Error: Todas las columnas están vacías en la fila actual.")
            break

        # Generar la sentencia INSERT INTO y agregarla a la lista de sentencias
        sql.append(f"INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES ({productId},0,0, {maxQuantity},1);")

# Escribir las sentencias INSERT INTO en un archivo .sql
with open('inserts4.sql', 'w') as f:
    f.write('\n'.join(sql))