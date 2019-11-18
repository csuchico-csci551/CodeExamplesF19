from pyspark.sql import SparkSession  
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

scSpark = SparkSession \
    .builder \
    .appName("Python Spark SQL example: Reading CSV file with schema") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

#CSV taken from https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
sdfData = scSpark.read.csv("biostats.csv", header=True, inferSchema = True)
#Print schema/data to show it's all collected/formatted correctly
print(sdfData.schema)
sdfData.show()
#Sum all of the column Age values
#Must make sure you purge whitespace or match exactly on column names
print(sdfData.groupBy().sum('Age').collect())
