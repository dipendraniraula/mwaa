from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dag1.config.ConfigStore import *
from dag1.functions import *
from prophecy.utils import *
from dag1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_datasource1 = datasource1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Dag1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Dag1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Dag1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
