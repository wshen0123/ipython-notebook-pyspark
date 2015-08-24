from os import getenv
if not getenv('PYSPARK_SUBMIT_ARGS', None):
    raise ValueError('PYSPARK_SUBMIT_ARGS environment variable is not set')

spark_home = getenv('SPARK_HOME', None)
if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')
