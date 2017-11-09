import os
import sys
import codecs

from envelop import Environment
from p4rr0t007.web import Application
from plant import Node

root_node = Node(__file__).dir
config_node = root_node.cd('config.yml')


if config_node.exists is not True:
    sys.stderr.write('you must the config file\n\r')
    sys.stderr.write(config_node.path)
    sys.stderr.write('\nexample:\n--------\n')
    sys.stderr.write('\n'.join([
        '---',
        'blogger_outh_client_id: YOUR CLIENT ID',
        'blogger_outh_client_secret: YOUR CLIENT SECRET',
        'server_secret: A RANDOM SECRET STRING OF YOUR CHOICE',
    ]))
    raise SystemExit(1)

config = Environment.from_file(config_node.path)

secret_key = config.get('server_secret') or codecs.encode(os.urandom(32), 'hex')

options = dict(
    static_folder=root_node.join('static'),
    static_path='/static',
    secret_key=secret_key,
)

server = Application(root_node, **options)
