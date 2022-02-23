##### BACKBONE,
##### A
##### MINIMAL
##### BATCH
##### FOLDER
##### MAKER
##### <>

import typer
from shutil import rmtree
from typing import Optional
from backbone import build_backbone, get_variables

app = typer.Typer()

@app.command()
def build(root: Optional[str] = None):
    if(root is None):
        build_backbone()
    else:
        build_backbone(root)


@app.command()
def destroy(root: Optional[str] = None):
    variables = get_variables()
    folders = variables["courses"].split(",")
    if(root is None):
        root = variables["root"]
    for folder in folders:
        rmtree(f"{root}/{folder}")

@app.command()
def variables():
    typer.echo(get_variables())


if __name__ == "__main__":
    app()