# concatenate.py
def concatenate(**kwargs):
    # Iterating over the Python kwargs dictionary
    print(kwargs)
    print(kwargs["a"])


concatenate(a="Real", b="Python", c="Is", d="Great", e="!")

