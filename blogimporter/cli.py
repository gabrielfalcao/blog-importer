import click

from blogimporter.web import application


@click.command()
@click.option('-H', '--host', default='127.0.0.1')
@click.option('-P', '--port', default=3000)
@click.option('-d', '--debug/--no-debug', default=False)
def run(host, port, debug):
    "runs the local development web server"
    application.run(host=host, port=port, debug=debug)


@click.group()
def main():
    pass


main.add_command(run)


if __name__ == '__main__':
    main()
