import mlflow.sagemaker as mfs

experiment_id = '897254543458316938'
run_id = 'b2b20dff826b4def99dc50e5792fcbab'
region = 'us-west-2'
aws_id = '718163805631'
arn = 'arn:aws:iam::718163805631:role/aws-sagemaker-for-deploy'
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