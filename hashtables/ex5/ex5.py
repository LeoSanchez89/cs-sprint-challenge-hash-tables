# Your code here
import string
import itertools

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    matching_paths = []
    path_dict = {}
    for path in files:
        split = path.split("/")
        idx = split[len(split) - 1]
        if idx in path_dict:
            path_dict[idx].append(path)
        else:
            path_dict[idx] = []
            path_dict[idx].append(path)
    for target in queries:
        if target in path_dict:
            matching_paths.append(path_dict[target])
    result = list(itertools.chain.from_iterable(matching_paths))
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        'usr/blah/example/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
