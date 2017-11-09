from blogimporter.http import root_node


def get_example_snippets():
    result = scan_files()
    return dict(result)


def load_node(node):
    contents = open(node.path).read()
    return node.basename, contents


def scan_files():
    for node in root_node.glob('*.py'):
        if node.basename.startswith('__'):
            continue

        yield load_node(node)
