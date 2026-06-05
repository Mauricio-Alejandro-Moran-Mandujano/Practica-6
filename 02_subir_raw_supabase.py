import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

from sqlalchemy.engine.url import URL

engine = create_engine(URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
), connect_args={"sslmode": "require"})

df = pd.read_csv("walmart_sales_clean.csv")

# Subir tabla cruda a Supabase
df.to_sql("raw_walmart_sales", engine, if_exists="replace", index=False)
print("Tabla raw_walmart_sales subida correctamente a Supabase")
print("Registros cargados:", len(df))