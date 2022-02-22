# About it

Backbone is a Minimal Batch Folder Maker. It was created to **standardize the creation of folders** associated with an academic semester, however, it also allows to **communicate and build the folder structure** of software projects in a simple, yet useful, way.

# Getting started

For now, Backbone can be used directly from the python script. To get started let's create the folders associated with an academic semester:

```
git clone https://github.com/diegoquezadac/backbone.git
cd ./backbone
python backbone.py
```

The folder structure is defined in the config file. 

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
