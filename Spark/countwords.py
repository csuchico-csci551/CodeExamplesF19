import argparse
from pyspark import SparkContext
from pyspark import SparkConf
from operator import add

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="the path to data file to parse")
args = parser.parse_args()


# create Spark context with Spark configuration
conf = SparkConf().setAppName("read text file in pyspark")
sc = SparkContext(conf=conf)

# Read file into RDD
lines = sc.textFile(args.file)
words = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
#count the frequency for words
counts = words.reduceByKey(add)
#Sort the counts in descending order based on the word frequency
sorted_counts =  counts.sortBy(lambda x: x[1], False)
#Get an iterator over the counts to print a word and its frequency
for word,count in sorted_counts.toLocalIterator():
    print(u"{} --> {}".format(word, count))