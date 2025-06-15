from collections import deque
from copy import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def gen_tree_nodes(input: list):
    queue = deque()
    root = None
    for item in input:
        print(item, end=", ")
        node = TreeNode(item)
        if len(queue) == 0:
            root = node
            queue.append(node)
            continue
        top_node = queue[0]
        if top_node.left is None:
            top_node.left = node
        else:
            top_node.right = node
            queue.popleft()
        queue.append(node)
    return root

def merge_node_flat(merged_list, node_list: list, centre_val):
    new_node_list = []
    is_list_of_list = False
    for item in node_list:
        print(f"\n\t\t\t -- {type(item)}:::: {type(item)==list}")
        if type(item) is list:
            is_list_of_list = True
            new_node_list_sub = []
            for sub_item in item:
                new_node_list_sub.append(sub_item)
            new_node_list_sub.append(centre_val)
            merged_list.append(new_node_list_sub)
        else:
            new_node_list.append(item)
    if is_list_of_list == False:
        new_node_list.append(centre_val)
        merged_list.append(new_node_list)
    return merged_list

def merge_node_list(left: list, right: list, centre_val):
    print(f"\t left:{left} \t right:{right} \t node_val:{centre_val}" )
    merged_list = []
    path_list = []
    if left:
        merge_node_flat(merged_list, left, centre_val)
        print(f"\t\t  merge_node_list::left_list:{merged_list}", end="")
    if right:
        merge_node_flat(merged_list, right, centre_val)
        print(f"\t\t  merge_node_list::right_list:{merged_list}", end="")

    if left is None and right is None:
        path_list.append(centre_val)
        merged_list.append(centre_val)
    elif (left is None and right is not None) or (right is None and left is not None):
        path_list = copy(merged_list)
    else:
        permutations = [(x, y) for x in left for y in right]
        for left_list, right_list in permutations:
            print(f"\n\t merge_node_list::getting path for {left_list} + {centre_val} + {right_list} ")
            if type(left_list) is list:
                path_list_temp = list()
                merge_node_flat(path_list_temp, left_list, centre_val)
                if type(right_list) is list:
                    for path in path_list_temp:
                        for ritem in right_list:
                            path.append(ritem)
                else:
                    for path in path_list_temp:
                        path.append(right_list)
                print(f"\n\t merge_node_list::got pathlist:{path_list_temp}")
                for path_temp in path_list_temp:
                    path_list.append(path_temp)
            else:
                flat_left_list = []
                flat_left_list.append(left_list)
                flat_left_list.append(centre_val)
                is_list_of_list_right = False
                if type(right_list) is list:
                    is_list_of_list_right = True
                    for ritem in right_list:
                        flat_left_list.append(ritem)
                else:
                    flat_left_list.append(right_list)
                path_list.append(flat_left_list)
                print(f"\n\t merge_node_list::got pathlist:{flat_left_list}")
    print(f"\n\t\t merge_node_list::path_list:{path_list}\t merge_list:{merged_list}")
    return path_list, merged_list

def get_all_paths(root: TreeNode, my_callable: callable):

    def get_paths_at_node(node: TreeNode, my_callable: callable):
        result = []
        if node is None:
            return None
        left_list = get_paths_at_node(node.left, my_callable=my_callable)
        right_list = get_paths_at_node(node.right, my_callable=my_callable)
        path_list, permute_list = merge_node_list(left_list, right_list, node.val)
        for path_item in path_list:
            my_callable(path_item)
        result.append (permute_list)
        return result

    final_path_list = get_paths_at_node(root, my_callable=my_callable)
    for path_item in final_path_list:
        callable(path_item)
    return final_path_list
    
def print_dfs(root: TreeNode, level = 1):
    if root is None:
        print("tree is empty")
    if root.left is not None:
        print_dfs(root.left, level + 1 )
    print(f"{level}:{root.val}", end=", ")
    if root.right is not None:
        print_dfs(root.right, level + 1)

def test_1():
    input = "abcdefghijklmno"
    input_list = [s for s in input]
    print(input_list)
    tree_root = gen_tree_nodes(input_list)
    print_dfs(tree_root)
    print(f"\n{'_'*20}")
    output_paths = get_all_paths(tree_root, display_list)
    print(f"\nlist of outputs:{output_paths}")

def display_list(path_list: list):
    print("\tpath-value::", end="")
    for path in path_list:
        print(f"{path}", end=", ")
    print("::")

def test_merge_node_flat():
    left_outer = [['j', 'e'], ['k', 'e']]
    right_outer = [['h', 'd'],['i', 'd']]
    center_val = 'b'
    merged_list = []
    path_list, merged_list = merge_node_list(left_outer, right_outer, center_val)
    print(f"\nmerged_list:{path_list} \n path_list:{merged_list}")


if __name__ == "__main__":
    # test_1()
    test_merge_node_flat()
