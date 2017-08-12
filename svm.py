from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext
datahome = r"/home/fernando/anaconda3/lib/python3.6/site-packages/pyspark/"
SPARK_HOME = '/usr/bin/Spark'
sc = SparkContext()

# Load and parse the data into LabeledPoint
def parsePoint(line):
	values = [float(x) for x in line.split(' ')]
	return LabeledPoint(values[0], values[1:])

data = sc.textFile(datahome + "data/mllib/sample_svm_data.txt")
parsedData = data.map(parsePoint)

# Build the model for SVM with Stocastic Gradient Descent
model = SVMWithSGD.train(parsedData, iterations=100)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))

# Compute the accuracy
trainErr = labelsAndPreds.filter(lambda v, p: v != p).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))