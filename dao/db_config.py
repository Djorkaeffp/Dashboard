import psycopg

DB_PATH = "postgresql://neondb_owner:npg_ly2KSID7XiTU@ep-autumn-truth-ahra4w2g-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg.connect(DB_PATH)
