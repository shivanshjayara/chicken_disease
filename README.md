# chicken_disease

* utils folder:
    - This will contains those modules which we will frequently be using in the code.
    - Example: Reading yaml file, because every time we will be using this in many function.

- Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity: It is just a return type of a function **This we will call in the configuration manager file**
5. Update the configuration manager in src config  **This we will call in the pipeline file**
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


- Data Ingestion
- Prepare base model
    **In image classification we don not require data validattion stage is not require because the image folders are in  correct format. But we can add if we require. It is general require for NLP and object detetction problem**
    **Fist we will build configuration for paths in config.yaml**
- Call back
    **We will not be creating any pipeline for this. We will use this inside the training piepline. This will actually help us in training**

- Model Evaluation: 
    **In evaluation we dont need any configuration.**
    **Here we check loss and accuracy**

- DVC:
    **DVC need git to be initialized.**
    **Use 'dvc repro' command to start execution**
    **Use 'dvc dag' command to see the piepline. Here we can see which stage is depemdemt on which stage.**

- Prediction:
    **Healthy chicken denoted by- 1**
    **Not healthy chicken chicken denoted by- 0**


- app.py
    **For runninng training using "main.py" file use 'os.system("python main.py")'**
    **For runninng training using "dvc" file use 'os.system("dvc repro")'**


- Dockerization
    **Create docker file before proceed to deployment**
    **Creating docker image and use this image for the deployment**
    **This is for the AWS deployment and for that we need aws cli**


- main.yaml
    **This file is for CICD deplyment**
    **This can be use same as it is. Only we need to change the name of the project at line number 95 i.e. --name==[PROJECT_NAME]**
    **In branch section, it tries to check the 'main' branch for new commit. If there is any new commit except README.md file, it will start cicd pipeline**


# AWS Deployment

- 1. Login to AWS console.

- 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
- 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
- 4. Create EC2 machine (Ubuntu) 

- 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
- 6. Configure EC2 as self-hosted runner:
    setting > actions > runner > new self hosted runner > choose os > then run command one by one


- 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = reponame




# AZURE-CICD-Deployment-with-Github-Actions

- Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6


- Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


- Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 


# ECR: 
    - URI: 395796441631.dkr.ecr.us-east-1.amazonaws.com/chicken