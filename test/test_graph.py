from graph_memo.graph import compose_graph


def test_compose_graph():
    nodes = ["hoge_1", "hoge_2"]
    edges = [("hoge_2", "hoge_1")]
    attributes = [{"name": "hoge_1"}, {"name": "hoge_2", "to": "hoge_1"}]

    actual = compose_graph(nodes, edges, attributes)

    assert actual.nodes['hoge_1'] == {'hoge_1': 'hoge_2', 'hoge_2': 'hoge_2'}
