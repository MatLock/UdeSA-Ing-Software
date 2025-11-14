from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


@dag(
  dag_id='dummy_dag_example',
  schedule=None,
  start_date=None,
  catchup=False,
  tags=['dummy_dag']
)
def my_dummy_dag():
  @task(task_id='task_1')
  def task_1():
    return 1
  
  @task(task_id='task_2')
  def task_2():
    return 2
  
  @task(task_id='task_3')
  def task_3():
    return 3
  
  @task.branch()
  def define_which_to_execute(result_lst: list[int]):
    if max(result_lst) > 2:
      return 'bigger_than_2'
    return 'lower_than_2'
  
  bigger_than_2 = BashOperator(
    task_id='bigger_than_2',
    bash_command="echo 'is bigger than 2'"
  )
  
  lower_than_2 = BashOperator(
    task_id='lower_than_2',
    bash_command="echo 'is lower than 2'"
  )
  
  results = [task_1(), task_2(), task_3()]
  define_which_to_execute(results) >> [bigger_than_2, lower_than_2]


my_dummy_dag()
