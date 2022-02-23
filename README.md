# About it

Backbone is a Minimal Batch Folder Maker. It was created to **standardize the creation of folders** associated with an academic semester, however, it also allows to **communicate and build the folder structure** of software projects in a simple, yet useful, way.

# Getting started

To get started let's clone the repo:

```
git clone https://github.com/diegoquezadac/backbone.git
cd backbone/
```

Now, let's create and activate the virtual environment as declared in the *environment.yml* file:

```
conda env create -f environment.yml
conda activate backbone
```

Finally, let's create the folders associated with my academic semester:

```
cd /src
python app.py build
```

# Configuration file

## Variables

1. courses: Specify the name of the folder(s) that will be created with the backbone configuration.
2. root: Specify the directory in which the folders will be created.

## Commands

1. f: create folder
2. t: create txt file
3. m: create markdown file
4. \>  move down one directory
5. <  move up one directory
