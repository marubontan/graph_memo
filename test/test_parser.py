import os
from mock import patch
from graph_memo.parser import load_all_memos, compose_nodes_and_edges

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixture")


@patch("graph_memo.parser.MEMO_DIRECTORY", FIXTURE_PATH)
def test_compose_nodes_and_edges():
    all_memos = load_all_memos()
    actual = compose_nodes_and_edges(all_memos)
    expected = (["hoge_1", "hoge_2"], [("hoge_2", "hoge_1")], [{"name": "hoge_1"}, {"name": "hoge_2", "to": "hoge_1"}])

    assert actual == expected
