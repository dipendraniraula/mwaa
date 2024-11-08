from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testmwaa.config.ConfigStore import *
from testmwaa.functions import *

def datasource1(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("s3://salesidemo/file/")
