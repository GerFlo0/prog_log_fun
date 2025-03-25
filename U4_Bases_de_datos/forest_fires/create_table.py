import psycopg2
import pandas as pd
import consts as c

def create_and_import(DB_PARAMS, CSV_PATH, TABLE_NAME):
    df = pd.read_csv(CSV_PATH, encoding='utf-8')
    df = df.dropna(how="any")
    
    df.columns = df.columns.astype(str)
    columnas = df.columns.to_list()
    column_types = {col: c.TYPE_MEANING.get(str(df[col].dtype), "TEXT") for col in df.columns}
    
    create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ("
    for col in columnas:
        create_table_query += f"{col} {column_types[col]}, "
    create_table_query = create_table_query.rstrip(", ") + ");"
    
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created")
    
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO {TABLE_NAME} ({', '.join(columnas)}) VALUES ({', '.join(['%s'] * len(row))});"
        cursor.execute(insert_query, tuple(row))
    conn.commit()
    print("Data imported")
    
    cursor.close()
    conn.close()