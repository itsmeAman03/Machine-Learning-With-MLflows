# Machine-Learning-With-MLflows


## Work Flow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?

### Steps 

```bash
https://github.com/itsmeAman03/Machine-Learning-With-MLflows.git
```

### STEP-01 Create Virtual environment after opening Repositry

#### For Linux/Mac/Windows Using bash/terminal/cmd
```bash
python -m venv env
```

#### By using conda 
```bash
conda create -n env python=<python-version> -y 
```
{env is your virtual environment name}

#### Activate Virtual Environment

###### For Windows:

```bash
.\env\Scripts\activate.bat
```

##### For Linux/Mac Using bash/terminal

```bash
source env/bin/activate
```

### STEP-02 Install the Requirements

```bash
pip install -r requirements.txt
```

```bash
#Run the following command
python app.py
```

Now,
```bash
open up your local hosh and port
```

## ML flow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd

- mlflow ui

### Dagshub
[Dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/itsmeAman03/Machine-Learning-With-MLflows.mlflow \
MLFLOW_TRACKING_USERNAME=itsmeAman03 \
MLFLOW_TRACKING_PASSWORD=514907432d019f32917391c0128fcca6a593fdf1 \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/itsmeAman03/Machine-Learning-With-MLflows.mlflow 

export MLFLOW_TRACKING_USERNAME=itsmeAman03

export MLFLOW_TRACKING_PASSWORD=514907432d019f32917391c0128fcca6a593fdf1

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

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

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 200988175983.dkr.ecr.ap-south-1.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI = 200988175983.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = mlproject



# ScreenShot of the project Insights

1. Form of the Model which takes input for prediction to be made
![form-model][images/form.png]

2. Prediction that we made from above inputs
![prediction][images/prediction.png]

3. We found the best parameter for our ElasticNet linear model for which mae and rmse should be low and r2 score should be high and it was alpha = 0.2 and l1_ration = 0.9 . It was done one dagshub/
![prameters][images/params.png]

4. CI/CD progress which was done on AWS EC2 Machine
![cicd][images/cicd.png]

5. After deploying the Project on EC2 machine and using docker our form page on public link
![publiclink][images/epic.png]


## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


