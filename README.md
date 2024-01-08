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