from pyspark import SparkContext
import random

sc = SparkContext("local", "Pi Estimate App")

NUM_SAMPLES = 1000000

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(xrange(0, NUM_SAMPLES)) \
             .filter(inside).count()
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)