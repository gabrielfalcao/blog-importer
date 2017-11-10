import sys

from envelop import Environment
from p4rr0t007.web import Application
from plant import Node
from blogimporter.googlelogin import GoogleLogin


root_node = Node(__file__).dir
config_node = root_node.cd('config.yml')


if config_node.exists is not True:
    sys.stderr.write('you must the config file\n\r')
    sys.stderr.write(config_node.path)
    sys.stderr.write('\nexample:\n--------\n')
    sys.stderr.write('\n'.join([
        '---',
        'google_oauth_client_id: YOUR CLIENT ID',
        'google_oauth_client_secret: YOUR CLIENT SECRET',
        'server_secret_key: A RANDOM SECRET STRING OF YOUR CHOICE',
    ]))
    raise SystemExit(1)

config = Environment.from_file(config_node.path)

client_id = config.get('google_oauth_client_id')
client_secret = config.get('google_oauth_client_secret')
secret_key = config.get('server_secret_key')

options = dict(
    static_folder=root_node.join('static'),
    static_path='/static',
    secret_key=secret_key,
)

server = Application(root_node, **options)
server.config.update(dict(config.items()))
server.initialize_extensions()

google = GoogleLogin(server)
