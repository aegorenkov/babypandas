from unittest import TestCase
import babypandas as bpd


class TestTo_panda_df(TestCase):
    def test_to_panda_df(self):
        df = bpd.DataFrame([0, 1, 2, 3])
        bpd.to_panda_df(df)
