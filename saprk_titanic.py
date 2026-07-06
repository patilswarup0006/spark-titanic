from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .getOrCreate()


print("SparkSession created successfully!")


df = spark.read.csv('titanic.csv', header=True, inferSchema=True)
df.printSchema()
df.show(10)

df = df.dropna(subset=['Age'])
from pyspark.sql.functions import when
df = df.withColumn('Age_Group', when(df['Age'] < 18, 'Child').when((df['Age'] >= 18) & (df['Age'] <= 59), 'Adult').otherwise('Senior'))
df.show()


df.createOrReplaceTempView("titanic")

spark.sql("SELECT pclass, COUNT(*) as passenger_count FROM titanic GROUP BY pclass ORDER BY pclass").show()

spark.sql("SELECT pclass, AVG(Age) as average_age FROM titanic GROUP BY pclass ORDER BY pclass").show()

spark.sql("SELECT * FROM titanic ORDER BY Age DESC LIMIT 5").show()

output_path = "./output_titanic"
df.write.mode("overwrite").csv(output_path, header=True)