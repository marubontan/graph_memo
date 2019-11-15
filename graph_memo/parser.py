import os
import glob
from typing import Dict, List, Tuple
import yaml

MEMO_DIRECTORY = os.path.join(os.path.dirname(__file__), "memos")


def load_memo(memo_path: str) -> Dict:
    with open(memo_path, "r") as f:
        memo = yaml.load(f)
    return memo


def load_all_memos() -> Dict:
    all_memo_paths = glob.glob(os.path.join(MEMO_DIRECTORY, "*"))
    memos = {}
    for memo_path in all_memo_paths:
        memo = load_memo(memo_path)
        memos[memo["name"]] = memo

    return memos


def compose_nodes_and_edges(memos: Dict) -> Tuple[List[str], List[Tuple[str, str]], List[Dict]]:
    nodes = []
    edges = []
    attributes = []
    for memo_name, memo in memos.items():
        nodes.append(memo_name)
        to_node = memo.get("to")
        if to_node is not None:
            edges.append((memo_name, to_node))
        attributes.append(memo)

    return nodes, edges, attributes
