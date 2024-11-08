from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testmwaa.config.ConfigStore import *
from testmwaa.functions import *
from prophecy.utils import *
from testmwaa.graph import *

def pipeline(spark: SparkSession) -> None:
    df_datasource1 = datasource1(spark)
    target1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("TestMWAA")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/TestMWAA")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/TestMWAA", config = Config)(pipeline)

if __name__ == "__main__":
    main()
