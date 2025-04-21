from airflow.operators.python import PythonOperatos
from datetime import datetime, timedelta
from airflow.decorators import dag, task

#now we will see the params that i always need to define

#1- dag id
#2 - datetime
#3 - schedule
#4 - catchup
#5 - description
#6 - tags
#7 - default arguments
#8 - dagrun timeout
#9 - max consecutive failed dag runs

@dag(start_date=datetime(2025, 1, 1),
     schedule='@daily', #scheduled everyday at midnight
     catchup=False,
     description="This DAG process ecommerce data",
     tags=["team_a", "ecom", "..."],
     default_args={"retries": 1},#instead of put in each task the retry argument, for example, u can set default here
     dagrun_timeout=timedelta(minutes=20),
     max_consecutive_failed_dag_runs=2)

def ecom_params(): #the first one is dag id. Using operator, the id is the name (ecom). As the best practice, use the same name of python file
    ta = PythonOperator(task_id='ta')

    tb = PythonOperator(task_id='tb')

    tc = PythonOperator(task_id='tc')

ecom_params()