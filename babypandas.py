import pandas as pd
import eastereggs

def to_panda_df(df):
    return pd.DataFrame(df.values, index=df.index, columns=df.columns)

# TODO Fix representation to be identical to pandas

class Index(object):
    def __init__(self, *args, **kwargs):
        self._index = pd.Index(*args, **kwargs)

    def __repr__(self):
        return self._index.__repr__()

    def __str__(self):
        return self._index.__str__()

    def __len__(self):
        return self._index.__len__()

    #TODO find a good way to get rid of this
    def __iter__(self):
         return self._index.__iter__()

    @property
    def dtype(self):
        return self._index.dtype

    @property
    def inferred_type(self):
        return self._index.inferred_type


class Series(object):
    def __init__(self, *args, **kwargs):
        self._series = pd.Series(*args, **kwargs)

    def __repr__(self):
        return self._series.__repr__()

    def __str__(self):
        return self._series.__str__()

    def head(self, n=5):
        return Series(self._series.head(n))

    def tail(self, n=5):
        return Series(self._series.tail(n))


class DataFrameGroupBy(object):
    def __init__(self, data_frame_group_by):
        self._dfgb = data_frame_group_by

    def head(self, n=5):
        return DataFrame(self._dfgb.head(n))

    def tail(self, n=5):
        return DataFrame(self._dfgb.tail(n))

    def apply(self, func, *args, **kwargs):
        return DataFrame(self._dfgb.apply(func, *args, **kwargs))


class DataFrame(object):
    def __init__(self, *args, **kwargs):
        self._df = pd.DataFrame(*args, **kwargs)

    def __getitem__(self, key):
        return Series(self._df.__getitem__(key))

    def __repr__(self):
        return self._df.__repr__()

    def __str__(self):
        return self._df.__str__()

    def head(self, n=5):
        return DataFrame(self._df.head(n))

    def tail(self, n=5):
        return DataFrame(self._df.tail(n))

    @property
    def columns(self):
        return Index(self._df.columns)

    @property
    def index(self):
        return Index(self._df.index)

    def sort_index(self, axis=0, level=None, ascending=True, na_position='last', sort_remaining=True,
                   by=None):
        return DataFrame(self._df.sort_index(axis=axis, level=level, ascending=ascending,
                                             inplace=False, kind='quicksort', na_position=na_position,
                                             sort_remaining=sort_remaining, by=by))

    def sort_values(self, by, axis=0, ascending=True, na_position='last'):
        return DataFrame(
                self._df.sort_values(by, axis=axis, ascending=ascending,
                                     inplace=False, kind='quicksort', na_position=na_position))

    def reindex(self, index=None, columns=None, **kwargs):
        return DataFrame(self._df.reindex(index=index, columns=columns, **kwargs))

    def apply(self, func, axis=0, broadcast=False, raw=False, reduce=None, args=(), **kwds):
        return DataFrame(
                self._df.apply(func, axis=axis, broadcast=broadcast,
                              raw=raw, reduce=reduce, args=args, **kwds))

    def applymap(self):
        pass

    def append(self, other, ignore_index=False, verify_integrity=False):
        return DataFrame(self._df.append(to_panda_df(other), ignore_index=ignore_index, verify_integrity=verify_integrity))

    @property
    def values(self):
        return self._df.values

    def rename(self, index=None, columns=None, **kwargs):
        return DataFrame(self._df.rename(index=index, columns=columns, **kwargs))

    def drop(self, labels, axis=0, level=None, errors='raise'):
        return DataFrame(self._df.drop(labels, axis=axis, level=level, inplace=False, errors=errors))

    def dropna(self, axis=0, how='any', thresh=None, subset=None):
        return DataFrame(self._df.dropna(axis=axis, how='any', thresh=thresh, subset=subset, inplace=False))

    def fillna(self, value=None, method=None, axis=None, limit=None, downcast=None, **kwargs):
        return DataFrame(self._df.fillna(value=value, method=method, axis=axis, inplace=False, limit=limit, downcast=downcast, **kwargs))

    def groupby(self, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False):
        return DataFrameGroupBy(self._df.groupby(by=by, axis=axis, level=level, as_index=as_index,
                         sort=sort, group_keys=group_keys, squeeze=squeeze))

    @property
    def shape(self):
        return self._df.shape

    def set_index(self, keys, drop=True, append=False, verify_integrity=False):
        return DataFrameGroupBy(self._df.set_index(keys, drop=drop, append=append, inplace=False, verify_integrity=verify_integrity))

    #Look at ix usage to see if this is ok
    @property
    def ix(self):
        return self._df.ix

    def pivot(self):
        pass

    def baby_panda(self):
        
        baby_panda = """

        babypandas
        The library that does more with less pandas.
        https://github.com/aegorenkov/babypandas.git

                  .;;.
                 /;;;;\  ___      .;;..
                |;(;;;-""   `'-.,;;;;;/
                 \;'            ';;;);/
                 /                \;;'
                /    .;.   .;.     \/
                |   ;;o;; ;;o;;    |
                ;   '"-'` `'-"'    |
                /\      ._.       /
              ;;;;;_   ,_Y_,   _.'
             /;;;;;\`--.___.--;.
            /|;;;;;;;.__.;;;.  \/\/
           ;  \;;;;;;;;;;;;;;\  ;\__  .;.
           |   ';;;;;;;;=;;;;'  |-__;;;;/
           |     `""`  .---._  /;/;;\;;/
          / ;         /;;;;;;;-;/;;/|;/
          \_,\       |;;;;;;;;;;;;| |
              '-...--';;;;;;;;;;;;\/
                       `\"""`   `"`

        """

        return baby_panda

    #TODO add unique, duplicate, dropduplicate
    #TODO consider adding is null
    #TODO look at sortlevel for multi-index
if __name__ == '__main__':
    print eastereggs.baby_panda

