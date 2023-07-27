from psycopg_pool import ConnectionPool
import os

class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  # we want to commit data such as an insert
  def query_commit_returning_id(self,sql,*kwargs):
    print("SQL STATEMENT-[commit with returning]-----") 
    try: 
      conn = self.pool.connection() 
      cur = conn.cursor()
      cur.execute(sql,kwargs)
      returning_id = cur.fetchone()[0]
      conn.commit()
      return returning_id
    except Exception as err: 
      self.print_sql_err(err)
  def query_commit(self,sql):
    try: 
      conn = self.pool.connection() 
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
    except Exception as err: 
      self.print_sql_err(err)   
        #conn.rollback()
  # when we want to return a json object 
  def query_array_json(self): 
    print("SQL STATEMENT-[array]-----")  
    print(sql + "/n")
    wrapped_sql = self.query_wrap_array(self,sql)
    with self.pool.connection() as conn:
      cur.execute(wrapped_sql)
      json = cur.fetchone()
      return json[0]        

  # When we want to return an array of json objects
  def query_object_json(sql):
    print("SQL STATEMENT-[object]-----")  
    print(sql + "/n")
    wrapped_sql = self.query_wrap_object(self,sql)
    with self.pool.connection() as conn:
      cur.execute(wrapped_sql)
      json = cur.fetchone()
      return json[0]
      
def query_wrap_object(self,template):
  sql = f"""
  (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
  {template}
  ) object_row);
  """
  return sql

def query_wrap_array(self,template):
  sql = f"""
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  """
  return sql
def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg ERROR:", err, "on line number:", line_num)
    print ("psycopg traceback:", traceback, "-- type:", err_type)

    # psycopg extension.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")
db = Db()
  

