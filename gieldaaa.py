import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col, lag, avg
import pyspark.sql.functions as f
from pyspark.sql.window import Window

stock = ["AAPL"]
stocks = yf.download(stock, start="2020-01-01")
stocks.to_csv("st_data.csv")
data = stocks.loc[:, "Close"].copy()
spark = SparkSession.builder.appName('gielda').getOrCreate()
stock_df = spark.read.csv("st_data.csv", inferSchema = True, header = True)
window_spec = Window.orderBy("Date")

stock_df = stock_df.withColumn("Prev_Close", lag("Close", 1).over(window_spec))
stock_df = stock_df.withColumn("Rolling_Mean_5", avg("Close").over(Window.orderBy("Date").rowsBetween(-4, 0)))
stock_df = stock_df.withColumn("Rolling_Mean_10", avg("Close").over(Window.orderBy("Date").rowsBetween(-9, 0)))
stock_df = stock_df.dropna()

assembler = VectorAssembler(
    inputCols=["Prev_Close", "Rolling_Mean_5", "Rolling_Mean_10"],
    outputCol="features"
)
assembled_df = assembler.transform(stock_df)

lr = LinearRegression(featuresCol="features", labelCol="Close", regParam=0.3, elasticNetParam=0.8)
train_data, test_data = assembled_df.randomSplit([0.8, 0.2])

lr_model = lr.fit(train_data)
predictions = lr_model.transform(test_data)
evaluator = RegressionEvaluator(labelCol="Close", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

pred = predictions.select(f.collect_list('prediction')).first()[0]
p_date = predictions.select(f.collect_list('Date')).first()[0]

plt.plot(data, color = 'blue', label = "Original data")
plt.plot(p_date, pred, color = 'red', label = "Predictions")

plt.xlabel("Date")
plt.ylabel("Stock Values")
plt.legend()
plt.show()