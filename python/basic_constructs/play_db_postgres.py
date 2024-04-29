import os
import json
import psycopg2



# host
# port
# user
# password
# db

RAPTOR_USER = os.environ['GEMINI_JDBC_RAPTOR_USER']
RAPTOR_PASSWORD = os.environ['GEMINI_JDBC_RAPTOR_PASSWORD']
ENGINE_USER = os.environ['GEMINI_JDBC_ENGINE_USER']
ENGINE_PASSWORD = os.environ['GEMINI_JDBC_ENGINE_PASSWORD']
RAPTOR_HOST_URL = os.environ['GEMINI_JDBC_RAPTOR_URL']
RAPTOR_HOST = RAPTOR_HOST_URL.split(":")[2].split("//")[1]
RAPTOR_PORT = RAPTOR_HOST_URL.split(":")[3].split("/")[0]
ENGINE_HOST_URL = os.environ['GEMINI_JDBC_ENGINE_URL']
ENGINE_HOST = ENGINE_HOST_URL.split(":")[2].split("//")[1]
ENGINE_PORT = ENGINE_HOST_URL.split(":")[3].split("/")[0]
ENGINE_DATABASE = "engine"

def play_engine_db():
    query_str = "select max(id) from engine_events"
    connection = psycopg2.connect(host=ENGINE_HOST, port=ENGINE_PORT, user=ENGINE_USER, password=ENGINE_PASSWORD, database = ENGINE_DATABASE)
    print(f" psycopg2.connect(host={ENGINE_HOST}, port={ENGINE_PORT}, user={ENGINE_USER}, password={ENGINE_PASSWORD}, database = {ENGINE_DATABASE})")
    if connection :
        print("connection obtainee")
    else:
        print("connection is null")
    cursor = connection.cursor()
    if cursor:
        print("cursor obtained")
    cursor.execute(query=query_str)
    output = cursor.fetchall()
    print(f"\t\toutput from db\n{output}")
    connection.close()
    # 213117804950


if __name__ == "__main__":
    play_engine_db()

