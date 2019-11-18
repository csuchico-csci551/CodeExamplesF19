import argparse
from pyspark import SparkContext
from pyspark import SparkConf

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="the path to data file to parse")
args = parser.parse_args()


# create Spark context with Spark configuration
conf = SparkConf().setAppName("read text file in pyspark")
sc = SparkContext(conf=conf)

# Read file into RDD
lines = sc.textFile(args.file)

# Call collect() to get all data
llist = lines.collect()

# print line one by line
for line in llist:
	print(line)
