# GieldaPredict
Predicting stock market behaviour and share declines


## AWS
EMR:
          - prepaired bucket S3 in which I made catalogs for logs, outputs, program code and input (that is probably unnecessary, but I was trying to manage errors)
          - prepaired VPC and connected it to EMR cluster
          - prepaired and launched EC2

## Program
With Yahoo Finance library (yfinance) I took stock data of a company and then used it for prediction model.
Prediction model was made with PySpark usage.

![image](https://github.com/Troll759/GieldaPredict/assets/77497259/6a11c2df-b26f-4f97-9e24-99b469d773ff)



## Sources
how do predictive analysis work? -> https://www.youtube.com/watch?v=Cx8Xie5042M
how to setup AWS and connect to it -> https://www.youtube.com/watch?v=xXirbnUB3NU
          - // -                   -> https://www.youtube.com/watch?v=3sQhVKO5xAA
          AWS EMR                  -> https://www.youtube.com/watch?v=8bOgOvz6Tcg&t=817s
working with PySpark Dataframes -> https://stackoverflow.com/questions/57810102/pyspark-dataframe-get-all-values-of-a-column
             - // -             -> https://www.geeksforgeeks.org/get-value-of-a-particular-cell-in-pyspark-dataframe/
PySpark Linear Regression -> https://www.youtube.com/watch?v=2OAa7lX8dxo
          - // -          -> https://www.youtube.com/watch?v=2m9xI4gs3HM
