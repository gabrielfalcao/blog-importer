import click

from blogimporter.web import application


@click.command()
@click.option('-H', '--host', default='0.0.0.0')
@click.option('-P', '--port', default=3000)
@click.option('-d', '--debug', default=False, type=bool)
def run(host, port, debug):
    """runs the local development web server"""
    application.run(host=host, port=port, debug=debug)


@click.group()
def cli():
    pass


cli.add_command(run)


if __name__ == '__main__':
    cli()
