setup:
	@python setup.py develop > .setup.log
	@date >> .setup.log

run: setup
	blog-importer run --host=127.0.0.1 --port=5000 --debug
