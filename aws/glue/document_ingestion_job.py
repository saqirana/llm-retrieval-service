"""
AWS Glue Job - Document Ingestion
Processes large batches of documents and generates embeddings.
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3
import json
from typing import List, Dict, Any

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_BUCKET', 'PINECONE_API_KEY'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# AWS clients
s3_client = boto3.client('s3')


def process_document(document_path: str) -> Dict[str, Any]:
    """
    Process a single document.

    Args:
        document_path: S3 path to document

    Returns:
        Processed document metadata
    """
    # TODO: Download document from S3
    # TODO: Extract text
    # TODO: Chunk text
    # TODO: Generate embeddings
    # TODO: Store in Pinecone

    return {
        'document_path': document_path,
        'status': 'processed',
        'chunks_count': 0
    }


def main():
    """Main Glue job execution."""

    # Read documents from S3
    bucket = args['S3_BUCKET']
    prefix = 'documents/'

    print(f"Processing documents from s3://{bucket}/{prefix}")

    # List objects in S3
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)

    documents = []
    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith(('.pdf', '.txt', '.docx')):
                documents.append(f"s3://{bucket}/{key}")

    print(f"Found {len(documents)} documents to process")

    # Process documents in parallel using Spark
    if documents:
        # Create RDD from documents list
        documents_rdd = sc.parallelize(documents)

        # Process each document
        results = documents_rdd.map(process_document).collect()

        print(f"Processed {len(results)} documents")

        # Write results to S3
        results_json = json.dumps(results, indent=2)
        s3_client.put_object(
            Bucket=bucket,
            Key='processing-results/latest.json',
            Body=results_json.encode('utf-8')
        )

    print("Job completed successfully")


if __name__ == '__main__':
    main()
    job.commit()

