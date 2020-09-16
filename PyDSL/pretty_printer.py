from PyDSL.AVL_tree import AVLTree
from random import randint
from typing import List, Tuple, Callable

# TREE_LAYER_DIFF = 3


def __print_branch(branch, layer_height: int, print_fn: Callable) -> Tuple[int, int, List[str]]:
    if branch is None:
        return 0, 0, []

    val_string = print_fn(branch)

    if branch.left_child is None and branch.right_child is None:
        return len(val_string), int(len(val_string) / 2), [val_string]

    left_branch_width, left_tree_centre, left_branch_lines = __print_branch(branch.left_child, layer_height, print_fn)
    right_branch_width, right_tree_centre, right_branch_lines = __print_branch(branch.right_child, layer_height, print_fn)

    central_padding = max(1, len(val_string) - left_branch_width - right_branch_width)

    line_width = left_branch_width + central_padding + right_branch_width

    small_side = min(len(left_branch_lines), len(right_branch_lines))
    large_side = max(len(left_branch_lines), len(right_branch_lines))

    centre = int(left_branch_width + central_padding / 2)

    left_element_padding = max(0, centre - round(len(val_string) / 2))
    right_element_padding = line_width - len(val_string) - left_element_padding

    if right_element_padding < 0:
        left_element_padding += right_element_padding
        right_element_padding = 0

    lines = [" " * left_element_padding + val_string + " " * right_element_padding]

    sx = centre
    dxl = left_tree_centre - sx
    dxr = (left_branch_width + central_padding + right_tree_centre) - sx

    for i in range(layer_height):
        line_str = [" " for _ in range(line_width)]

        if left_branch_width != 0:
            pos = sx + (i / (layer_height - 1)) * dxl

            # if i < layer_height - 1:
            #     for fill in range(round(pos), round(pos + dxl / (2 * layer_height)), -1):
            #         line_str[fill] = "-"
            # if i > 0:
            #     for fill in range(round(pos), round(pos - dxl / (2 * layer_height)), 1):
            #         line_str[fill] = "-"
            line_str[round(pos)] = "/"

        if right_branch_width != 0:
            pos = sx + (i / (layer_height - 1)) * dxr
            line_str[round(pos)] = "\\"

        lines.append("".join(line_str))

    for i in range(0, small_side):
        lines.append(left_branch_lines[i] + " " * central_padding + right_branch_lines[i])

    if len(left_branch_lines) > len(right_branch_lines):
        for i in range(small_side, large_side):
            lines.append(left_branch_lines[i] + " " * (right_branch_width + central_padding))
    else:
        for i in range(small_side, large_side):
            lines.append(" " * (left_branch_width + central_padding) + right_branch_lines[i])

    return line_width, centre, lines


def pretty_print_tree(tree, layer_height=2, print_fn=lambda br: f"{{{br.key}:{br.val}}}"):
    _, _, lines = __print_branch(tree.root, layer_height, print_fn)
    for line in lines:
        print(line)


def pretty_print_graph(graph):
    pass


if __name__ == '__main__':
    tree = AVLTree()
    for _ in range(1000):
        k = randint(100, 200)
        v = randint(100, 200)
        tree[k] = v

        # --
        #   --
        #     --

    pretty_print_tree(tree, 6)
