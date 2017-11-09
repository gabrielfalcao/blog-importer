import os
import sys
import codecs

from envelop import Environment
from p4rr0t007.web import Application
from plant import Node
from flask_oauthlib.client import OAuth

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


client_id = config.get('blogger_outh_client_id')
client_secret = config.get('blogger_outh_client_secret')
secret_key = config.get('server_secret') or codecs.encode(os.urandom(32), 'hex')

options = dict(
    static_folder=root_node.join('static'),
    static_path='/static',
    secret_key=secret_key,
)

server = Application(root_node, **options)
server.config['GOOGLE_ID'] = client_id
server.config['GOOGLE_SECRET'] = client_secret


oauth = OAuth(server)

google = oauth.remote_app(
    'google',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    consumer_key=client_id,
    consumer_secret=client_secret,
)
