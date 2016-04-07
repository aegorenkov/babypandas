from unittest import TestCase
from babypandas import DataFrame, Index, Series, to_panda
import numpy as np
import pandas.util.testing as pdt

def assert_frame_equal(left, right):
    """
    The pandas testing utilities have unfortunately decided to enforce instance class.
    Rather than rewriting the testing utilities we just convert babypandas objects to pandas objects

    :param left: babypandas dataframe
    :param right: babypandas dataframe
    :return: None
    """
    pdt.assert_frame_equal(to_panda(left), to_panda(right))


class TestIndex(TestCase):
    def test__getitem__(self):
        df.columns[0]

class TestDataFrame(TestCase):
    def setUp(self):
        self.df = DataFrame([0, 1, 2, 3])

    def test_head(self):
        self.df.head()
        self.df.head(4)

    def test__getitem__(self):
        self.df[0]
        self.assertIsInstance(self.df[0], Series)
        self.df[self.df.columns[0]]

    def test_tail(self):
        self.df.tail()
        self.df.tail(2)

    def test_columns(self):
        cols = (
            DataFrame([[0, 4], [1, 5], [2, 6], [3, 7]], columns=['first', 'second'])
                .columns
        )
        self.assertItemsEqual(cols, ['first', 'second'])

    def test_column_indexing(self):
        self.df.columns[0]

    def test_column_slicing(self):
        self.df.columns[:1]

    def test_index(self):
        self.assertItemsEqual(self.df.index, [0, 1, 2, 3])


    def test_sort_index_ascending(self):
        assert_frame_equal(
                self.df.sort_index(ascending=True),
                DataFrame([0, 1, 2, 3])
        )

    def test_sort_index_descending(self):
        assert_frame_equal(
                self.df.sort_index(ascending=False),
                DataFrame([3, 2, 1, 0], index=[3, 2, 1, 0])
        )

    def test_sort_values_ascending(self):
        assert_frame_equal(
                self.df.sort_values(0, ascending=True),
                DataFrame([0, 1, 2, 3])
        )

    def test_sort_values_descending(self):
        assert_frame_equal(
                self.df.sort_values(0, ascending=False),
                DataFrame([3, 2, 1, 0], index=[3, 2, 1, 0])
        )

    def test_reindex(self):
        self.df.reindex()
        assert_frame_equal(
                self.df.reindex([2, 1, 0, 3]),
                DataFrame([2, 1, 0, 3], index=[2, 1, 0, 3])
        )


    def test_apply(self):
        self.df.apply(np.sum)

    # def test_applymap(self):
    #     self.df.applymap(np.sum)

    def test_append(self):
        df2 = DataFrame([[4, 8], [5, 9], [6, np.NAN], [7, np.NAN]])
        (self.df
         .append(df2)
         )

    def test_values(self):
        self.df.values

    def test_rename(self):
        self.df.rename(columns={0:'first'})

    def test_drop(self):
        self.df.drop(0)
        self.df.drop(2, axis=0)

    def test_dropna(self):
        (
            DataFrame([[4, 8], [5, 9], [6, np.NAN], [7, np.NAN]])
                .dropna()
        )

    def test_fillna(self):
        (DataFrame([[4, 8], [5, 9], [6, np.NAN], [7, np.NAN]])
            .fillna(5)
         )

    def test_groupby(self):
        (self.df
         .rename(columns={0:'first'})
         .groupby('first')
         .apply(np.mean)
        )

    @property
    def test_ix(self):
        self.df.ix[0]

    def test_set_index(self):
        self.df.set_index(0)

    def test_assign(self):
        self.df.assign(test=[4, 5, 6, 7])

    def test_describe(self):
        self.df.describe()

    def test_inf0(self):
        self.df.info()

    def test_replace(self):
        self.df.replace({0:4})

    def test_count(self):
        self.df.count()