def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches:
        if not is_tree(branch):
            return False 
    return True

def is_leaf(tree):
    return type(tree) == list and not branches(tree)

def count_leaves(t):
    if is_leaf(t):
        return 1 
    else:
        branch_counts = [count_leaves for branch in branches(t)]
        return sum(branch_counts)

def print_tree(t):
    if is_leaf(t):
        print(t)
    else:
        print(label(t))
        print_tree(branches(t))