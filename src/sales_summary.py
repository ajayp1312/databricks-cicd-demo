# Databricks notebook source

from pyspark.sql import functions as F

# COMMAND ----------

print("Sales summary demo - version 1aa")

sales = spark.createDataFrame(
    [
        (1, "North", 100),
        (2, "South", 80),
        (3, "North", 50),
    ],
    schema="order_id INT, region STRING, amount INT",
)

# COMMAND ----------

summary = (
    sales.groupBy("region")
    .agg(F.sum("amount").alias("total_sales"))
    .orderBy("region")
)

display(summary)

# COMMAND ----------

actual = {
    row["region"]: row["total_sales"]
    for row in summary.collect()
}

expected = {
    "North": 150,
    "South": 80,
}

assert actual == expected, (
    f"Expected {expected}, got {actual}"
)

print("SUCCESS: sales totals are correct.")