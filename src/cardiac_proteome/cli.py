"""Console script for cardiac_proteome."""
import cardiac_proteome

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for cardiac_proteome."""
    console.print("Replace this message by putting your code into "
               "cardiac_proteome.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
