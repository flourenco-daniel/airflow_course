from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime

#lets do a less convenient way to start a dag

dag = DAG(
    'minha_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily'
)

ta = PythonOperator(task_id='ta', 
                    dag=dag)
                    
tb = PythonOperator(task_id='tb', 
                    dag=dag)

tc = PythonOperator(task_id='tc', 
                    dag=dag) ##is not a convenient way because every time that o build a dag you need to declarate a dag=dag


#the most convenient way is:

with DAG('minha_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily'):

    ta = PythonOperator(task_id='ta')

    tb = PythonOperator(task_id='tb')

    tc = PythonOperator(task_id='tc')

    #we dont need to use the dag=dag because the tasks is on context of my dag

#now lets use dag decorators using the lib airflow.decoratos

@dag("dag parameters here")
def my_dag():
    ta = PythonOperator(task_id='ta')

    tb = PythonOperator(task_id='tb')

    tc = PythonOperator(task_id='tc')

my_dag()

#now, using task decorators

#now lets use decorators using the lib airflow.decoratos

@dag("dag parameters here")
def my_dag():

    @task
    def ta():
        (...)

    def tb():
        (...)

    def tc():
        (...)

    ta()
    tb()
    tc()
my_dag()