import unittest

import pandas as pd

from kg_covid_19.edges import make_edges, tsv_to_df


class TestEdges(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_tsv_to_df(self):
        tsv_file = 'tests/resources/edges/small_graph_edges.tsv'
        df = tsv_to_df(tsv_file)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual((21, 5), df.shape)
        self.assertEqual(df['subject'][0], 'g1')

    def test_make_edges(self):
        self.assertTrue(True)

