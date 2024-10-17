# Project Documentation

## Project Approach

```plaintext
       pypdf2              
PDF ------------> Text ---------> API --------> response


## Setting Up the Environment

### Step 1: Install Anaconda

1. Download and install [Anaconda](https://www.anaconda.com/products/distribution).
2. Add Anaconda (`scripts` and `condabin`) to your environment variables.

### Step 2: Create a Virtual Environment

Open the terminal and run the following command to create a virtual environment using Anaconda:

```bash
& "C:\Users\deept\anaconda3\Scripts\conda.exe" create -p venv python==3.10 -y


## Create REQUIREMENTS.txt file

## Activate Conda Environment
In Anaconda Prompt, as Admin,

conda init powershell
(now the path in powershell appears like):
(d:\Application Tracking System\venv) PS D:\Application Tracking System>  

conda activate venv/ 

pip install -r requirements.txt


## Create API key
Go to makersuite and get a key 
Add the key to .env

## Create APP.py
(add the code)

### Back to powershell:
streamlit run app.py

(this will launch the app on web localhost)

Now the app will work successfully!
