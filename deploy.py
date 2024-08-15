import mlflow.sagemaker as mfs

experiment_id = '214535389302989232'
run_id = '30d4fa4e2cf747e796f680c27b282035'
region = 'us-west-2'
aws_id = '718163805631'
arn = 'arn:aws:iam::718163805631:role/aws-sagemaker-for-deploy-ml-model'
app_name = 'model-application'
model_uri = f'mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model'
tag_id = '2.15.1'


image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id


mfs._deploy(app_name,
	model_uri=model_uri,
	region_name=region,
	mode='create',
	execution_role_arn=arn,
	image_url=image_url,
    flavor="python_function")