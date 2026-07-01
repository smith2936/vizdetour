from typing import Any, List, Optional, Iterable, Tuple
import random

class Node:
    """
    A wrapper node that stores:
      - e: reference to the original element
      - children: list[Node], mirroring e.get_children()
      - size: total number of nodes in this subtree (including self)
      - removable_size: total number of removable nodes in this subtree (including self if removable)
      - is_removable: whether this node's element can be removed
      - parent: optional parent Node (None for root)
      - index_within_parent: index of this node in parent's children (None for root)
    """
    __slots__ = ("e", "children", "size", "removable_size", "is_removable", "parent", "index_within_parent")

    def __init__(self, e: Any, children: Optional[List["Node"]] = None):
        self.e = e
        self.children: List[Node] = children if children is not None else []
        self.size: int = 1  # will be finalized after building children
        self.removable_size: int = 0  # will be finalized after building children
        self.is_removable: bool = False  # will be set during tree construction
        self.parent: Optional[Node] = None
        self.index_within_parent: Optional[int] = None

    def __repr__(self) -> str:
        label = getattr(self.e, "name", None) or getattr(self.e, "id", None) or str(self.e)
        return f"Node({label!r}, size={self.size}, removable_size={self.removable_size}, is_removable={self.is_removable})"


def get_tree(root: Any) -> Node:
    """
    Recursively build a Node tree from the given root element.
    Assumes `root` has a method `get_children()` returning an iterable of elements.
    Also computes subtree sizes for efficient sampling.
    Additionally sets parent pointers and indices for backtracing.
    Checks _remove_method attribute to determine if node is removable.
    """
    node = Node(root)

    # Check if this element is removable
    remove_method = getattr(root, "_remove_method", None)
    node.is_removable = remove_method is not None

    # Safely call get_children(); treat missing or non-callable as empty
    children_iter: Iterable[Any] = []
    get_children = getattr(root, "get_children", None)
    if callable(get_children):
        children_iter = get_children() or []

    node.children = [get_tree(child) for child in children_iter]

    # Set parent pointers and index positions
    for i, child in enumerate(node.children):
        child.parent = node
        child.index_within_parent = i

    # Compute subtree size (1 for self + sum of child sizes)
    node.size = 1 + sum(child.size for child in node.children)
    
    # Compute removable subtree size (1 if self is removable + sum of child removable sizes)
    node.removable_size = (1 if node.is_removable else 0) + sum(child.removable_size for child in node.children)
    
    return node


def print_tree(root: Node) -> None:
    """
    Pretty-print the Node tree. Uses a readable label from the wrapped element:
    tries `e.name`, then `e.id`, then `str(e)`.
    Shows removability status with [R] for removable nodes.
    """
    def label(e: Any) -> str:
        return str(getattr(e, "name", None) or getattr(e, "id", None) or e)

    def dfs(node: Node, prefix: str = "", is_last: bool = True) -> None:
        connector = "└── " if is_last else "├── "
        removable_marker = "[R] " if node.is_removable else ""
        print(prefix + connector + removable_marker + label(node.e))
        next_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(node.children):
            dfs(child, next_prefix, i == len(node.children) - 1)

    dfs(root, "", True)


def sample_node(root: Node) -> Node:
    """
    Uniformly sample a Node from the tree (each node has equal probability).
    Requires that `size` is correctly computed (via get_tree).

    Returns a Node. Use `get_index_path(node)` or `format_access_path(root_expr, node)`
    to reconstruct the access path from the root element to the sampled node.
    """
    if root is None or root.size <= 0:
        raise ValueError("Root must be a valid Node with positive size.")

    k = random.randint(1, root.size)  # inclusive
    if k == 1:
        return root
    k -= 1  # account for the root itself

    node = root
    while True:
        for child in node.children:
            if k <= child.size:
                if k == 1:
                    return child
                k -= 1
                node = child
                break
            else:
                k -= child.size
        else:
            # Should never happen if sizes are correct
            return node


def sample_removable_node(root: Node) -> Node:
    """
    Uniformly sample a removable Node from the tree (each removable node has equal probability).
    Requires that `removable_size` is correctly computed (via get_tree).
    
    Raises ValueError if there are no removable nodes in the tree.

    Returns a Node. Use `get_index_path(node)` or `format_access_path(root_expr, node)`
    to reconstruct the access path from the root element to the sampled node.
    """
    if root is None or root.removable_size <= 0:
        raise ValueError("Root must be a valid Node with at least one removable node.")

    k = random.randint(1, root.removable_size)  # inclusive
    
    # Check if root itself is the target
    if root.is_removable:
        if k == 1:
            return root
        k -= 1  # account for the root itself

    node = root
    while True:
        for child in node.children:
            if k <= child.removable_size:
                # Check if this child is the target
                if child.is_removable and k == 1:
                    return child
                # Decrement k if this child is removable
                if child.is_removable:
                    k -= 1
                # Continue searching in this child's subtree
                node = child
                break
            else:
                k -= child.removable_size
        else:
            # Should never happen if removable_size is correct
            return node


def get_index_path(node: Node) -> List[int]:
    """
    Reconstruct the path from the root to the given node as a list of child indices.
    Example: [0, 1, 2] means root.get_children()[0].get_children()[1].get_children()[2]
    """
    path_rev: List[int] = []
    cur = node
    while cur.parent is not None:
        # index_within_parent is guaranteed to be set for non-root nodes
        assert cur.index_within_parent is not None
        path_rev.append(cur.index_within_parent)
        cur = cur.parent
    return list(reversed(path_rev))


def format_access_path(root_expr: str, node: Node) -> str:
    """
    Format the path as a Python expression using get_children() calls.
    - root_expr: the variable/expression that refers to the original root element (e.g., "fig")
    Example output:
      "fig"                        for the root itself
      "fig.get_children()[0]"     for path [0]
      "fig.get_children()[0].get_children()[1]" for path [0, 1]
    """
    indices = get_index_path(node)
    expr = root_expr
    for i in indices:
        expr += f".get_children()[{i}]"
    return expr


def sample_node_with_path(root: Node, root_expr: str = "root") -> Tuple[Node, List[int], str]:
    """
    Sample a node and return:
      - the Node itself,
      - the list of indices path from root to that node,
      - the formatted Python access expression using get_children().
    """
    node = sample_node(root)
    idx_path = get_index_path(node)
    expr = format_access_path(root_expr, node)
    return node, idx_path, expr


def sample_removable_node_with_path(root: Node, root_expr: str = "root") -> Tuple[Node, List[int], str]:
    """
    Sample a removable node and return:
      - the Node itself,
      - the list of indices path from root to that node,
      - the formatted Python access expression using get_children().
    """
    node = sample_removable_node(root)
    idx_path = get_index_path(node)
    expr = format_access_path(root_expr, node)
    return node, idx_path, expr