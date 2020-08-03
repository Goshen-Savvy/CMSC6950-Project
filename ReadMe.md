## Project Title
[Autorank - A third-party package in python](https://www.kaggle.com/janiobachmann/bank-marketing-dataset)

## Project Scope
The project is focused on reproducing the implementation of autorank.

## Project Task
The ease of reproducing the project.

## Technologies
Project was created with the following:
* Python version: 3.8.2
* GNU nano version: 4.8
* Pip version: 20.0.2

## Dependencies
### Installation
To run this project, install the following locally using pip or pip3:
* pip3 install requirements.txt

### Python Packages
* Pandas
* Numpy
* Seaborn	
* Matplotlib
* Wget
* autorank
* missingno

### Unforseen Technical Issues

* To download datasets from kaggle using wget or curl:
    * Create an account on kaggle
    * Go to <b>my account</b> and download the kaggle's API
    * From the terminal copy or move the API (kaggle.json) in the download directory to the home directory
        * home directory -> .kaggle -> kaggle.json file
    * $ kaggle datasets download janiobachmann/bank-marketing-dataset
    * $ unzip bank-marketing-dataset.zip
    * $ rm bank-marketing-dataset.zip 


## Work-Flow
### Create the local repository

```
$ cd your directory (Ex. desktop)
$ mkdir folderName
$ git init
$ git clone https://github.com/Goshen-Savvy/CMSC6950-Analyzing-Autorank.git
$ git pull
```
### Create your branch

* git branch branch_name

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