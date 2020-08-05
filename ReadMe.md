## Project Title
### Using Autorank, Missingno and Machine learning algorithm to predict bank deposit from clients.
I used two third-party packages. Below are the relevant links for your information.
* [Autorank](https://pypi.org/project/autorank/#description)
* [Missingno](https://github.com/ResidentMario/missingno)


## Project Task
The ease of reproducing the project.

## Technologies
Project was created with the following:
```
* Python version: 3.8.2
* GNU nano version: 4.8
* Pip version: 20.0.2
```
## Dependencies
### Installation
To run this project, install the following:
* python dependencies:
    ```
    * pip3 install requirements.txt
    ```
* linux dependencies
    ```
    * sudo apt install texlive-latex-base
    ```


### Python Packages
```
* pandas
* numpy
* seaborn	
* matplotlib
* scikit learn
* xgboost
* autorank
* missingno
```

### Do the following to reproduce my work:
```
* To download datasets from kaggle using wget or curl:
    * Create an account on kaggle
    * Go to my account and download the kaggle's API
    * From the terminal copy or move the API (kaggle.json) in the download directory to the home directory ('Ex. anne@Awesome-God:')
        * home directory -> .kaggle -> kaggle.json file 
        * anne@Awesome-God: cd .kaggle
        * ls .kaggle --> kaggle.json
             
* To access the machine learning model:
    * pip3 install --force-reinstall pip==20.0.2
    * pip3 install xgboost or python3 -m pip install xgboost
```

## Work-Flow
### Create the local repository

```
$ git clone https://github.com/Goshen-Savvy/CMSC6950-Project.git
$ git pull
```
### Execute the project

```
Run
#To call the Makefile and execute all.
$ make
#To removing all the downloaded data and complied files
$ make clean
#To generate files by file name (Ex. report.pdf).
$ make report.pdf
```

## Tasks completed      