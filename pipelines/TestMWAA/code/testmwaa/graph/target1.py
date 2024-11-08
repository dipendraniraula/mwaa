from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testmwaa.config.ConfigStore import *
from testmwaa.functions import *

def target1(spark: SparkSession, in0: DataFrame):
    in0.write.format("text").text("s3://salesidemo/files", compression = None, lineSep = None)
