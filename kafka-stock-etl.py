import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1723109183512 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://kafka-stock-analytics/landing-zone/"], "recurse": True}, transformation_ctx="AmazonS3_node1723109183512")

# Script generated for node Drop Fields
DropFields_node1723109405879 = DropFields.apply(frame=AmazonS3_node1723109183512, paths=["unwanted"], transformation_ctx="DropFields_node1723109405879")

# Script generated for node Amazon S3
AmazonS3_node1723109435189 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1723109405879, connection_type="s3", format="glueparquet", connection_options={"path": "s3://kafka-stock-analytics/transfer-zone/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1723109435189")

job.commit()