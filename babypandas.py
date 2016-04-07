# -*- coding: utf-8 -*-

import pandas as pd


def baby_panda():
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


def to_panda(baby_object):
    if isinstance(baby_object, DataFrame):
        return pd.DataFrame(baby_object.values, index=baby_object.index, columns=baby_object.columns)
    elif isinstance(baby_object, Index):
        return pd.Index(baby_object)
    elif isinstance(baby_object, Index):
        return pd.Series(baby_object.values, index=baby_object.index, name=baby_object.name)
    else:
        return baby_object


def from_panda(panda_object):
    if isinstance(panda_object, pd.DataFrame):
        return DataFrame(panda_object.values, index=panda_object.index, columns=panda_object.columns)
    elif isinstance(panda_object, pd.Index):
        return Index(panda_object)
    elif isinstance(panda_object, pd.Series):
        return Series(panda_object)
    else:
        return panda_object


def read_csv(filepath_or_buffer, header='infer', names=None, index_col=None, sep=',', skiprows=None, usecols=None,
             encoding=None, low_memory=True, squeeze=False, na_values=None, dtype=None, converters=None):
    return from_panda(
        pd.read_csv(filepath_or_buffer, sep=sep, dialect=None, compression='infer', doublequote=True, escapechar=None,
                    quotechar='"', quoting=0, skipinitialspace=False, lineterminator=None, header=header,
                    index_col=index_col, names=names, prefix=None, skiprows=skiprows, skipfooter=None, skip_footer=0,
                    na_values=na_values, true_values=None, false_values=None, delimiter=None, converters=converters,
                    dtype=dtype, usecols=usecols, engine=None, delim_whitespace=False, as_recarray=False,
                    na_filter=True, compact_ints=False, use_unsigned=False, low_memory=low_memory, buffer_lines=None,
                    warn_bad_lines=True, error_bad_lines=True, keep_default_na=True, thousands=None, comment=None,
                    decimal='.', parse_dates=False, keep_date_col=False, dayfirst=False, date_parser=None,
                    memory_map=False, float_precision=None, nrows=None, iterator=False, chunksize=None, verbose=False,
                    encoding=encoding, squeeze=squeeze, mangle_dupe_cols=True, tupleize_cols=False,
                    infer_datetime_format=False, skip_blank_lines=True))

def to_datetime():
    pass


def cut():
    pass


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

    # TODO find a good way to get rid of this
    def __iter__(self):
        return self._index.__iter__()

    def __getitem__(self, key):
        return from_panda(self._index.__getitem__(to_panda(key)))

    @property
    def dtype(self):
        return self._index.dtype

    @property
    def inferred_type(self):
        return self._index.inferred_type


class Series(object):
    # TODO consider adding astype
    def __init__(self, data=None, index=None, dtype=None, name=None, copy=False, fastpath=False):
        self._series = pd.Series(data=data, index=index, dtype=dtype, name=name, copy=copy, fastpath=fastpath)

    def __repr__(self):
        return self._series.__repr__()

    def __str__(self):
        return self._series.__str__()

    # TODO see why this is wrong
    def __sub__(self, other, axis=None, level=None, fill_value=None):
        return from_panda(self._series.__sub__(other, axis=axis, level=level, fill_value=fill_value))

    # TODO this also fails
    def __div__(self, other, axis=None, level=None, fill_value=None):
        return self._series.__div__(other, axis=None, level=None, fill_value=None)

    def head(self, n=5):
        return Series(self._series.head(n))

    def tail(self, n=5):
        return Series(self._series.tail(n))

    def apply(self, func, convert_dtype=True, args=(), **kwds):
        return from_panda(self._series.apply(func, convert_dtype=convert_dtype, args=args, **kwds))

    def unique(self):
        pass

    @property
    def values(self):
        return from_panda(self._series.values)

    @property
    def index(self):
        return from_panda(self._series.index)

    def name(self):
        return from_panda(self._series.name)


class DataFrameGroupBy(object):
    def __init__(self, data_frame_group_by):
        self._dfgb = data_frame_group_by

    def head(self, n=5):
        return from_panda(self._dfgb.head(n))

    def tail(self, n=5):
        return from_panda(self._dfgb.tail(n))

    def apply(self, func, *args, **kwargs):
        return from_panda(self._dfgb.apply(func, *args, **kwargs))


class DataFrame(object):
    # TODO add unique, duplicate, dropduplicate
    # TODO consider adding is null
    # TODO look at sortlevel for multi-index
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False):
        self._df = pd.DataFrame(data=data, index=index, columns=columns, dtype=dtype, copy=copy)

    def __getitem__(self, key):
        return from_panda(self._df.__getitem__(to_panda(key)))

    def __repr__(self):
        df = self._df.head()
        return df.__repr__()

    def __str__(self):
        df = self._df.head()
        return df.__str__()

    def head(self, n=5):
        return from_panda(self._df.head(n))

    def tail(self, n=5):
        return from_panda(self._df.tail(n))

    @property
    def columns(self):
        return from_panda(self._df.columns)

    @property
    def index(self):
        return from_panda(self._df.index)

    def sort_index(self, axis=0, level=None, ascending=True, na_position='last', sort_remaining=True, by=None):
        return from_panda(
            self._df.sort_index(axis=axis, level=level, ascending=ascending, inplace=False, kind='quicksort',
                                na_position=na_position, sort_remaining=sort_remaining, by=by))

    def sort_values(self, by, axis=0, ascending=True, na_position='last'):
        return from_panda(
                self._df.sort_values(by, axis=axis, ascending=ascending,
                                     inplace=False, kind='quicksort', na_position=na_position))

    def reindex(self, index=None, columns=None, **kwargs):
        return from_panda(self._df.reindex(index=index, columns=columns, **kwargs))

    def apply(self, func, axis=0, broadcast=False, raw=False, reduce=None, args=(), **kwds):
        return from_panda(
                self._df.apply(func, axis=axis, broadcast=broadcast,
                               raw=raw, reduce=reduce, args=args, **kwds))

    def applymap(self):
        pass

    def append(self, other, ignore_index=False, verify_integrity=False):
        return from_panda(
                self._df.append(to_panda(other), ignore_index=ignore_index, verify_integrity=verify_integrity))

    @property
    def values(self):
        return self._df.values

    def rename(self, index=None, columns=None, **kwargs):
        return from_panda(self._df.rename(index=index, columns=columns, **kwargs))

    def drop(self, labels, axis=0, level=None, errors='raise'):
        return from_panda(self._df.drop(labels, axis=axis, level=level, inplace=False, errors=errors))

    def dropna(self, axis=0, how='any', thresh=None, subset=None):
        return from_panda(self._df.dropna(axis=axis, how='any', thresh=thresh, subset=subset, inplace=False))

    def fillna(self, value=None, method=None, axis=None, limit=None, downcast=None, **kwargs):
        return from_panda(
            self._df.fillna(value=value, method=method, axis=axis, inplace=False, limit=limit, downcast=downcast,
                            **kwargs))

    def groupby(self, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False):
        return DataFrameGroupBy(
            self._df.groupby(by=by, axis=axis, level=level, as_index=as_index, sort=sort, group_keys=group_keys,
                             squeeze=squeeze))

    @property
    def shape(self):
        return self._df.shape

    def set_index(self, keys, drop=True, append=False, verify_integrity=False):
        return from_panda(
            self._df.set_index(keys, drop=drop, append=append, inplace=False, verify_integrity=verify_integrity))

    # Look at ix usage to see if this is ok
    @property
    def ix(self):
        return self._df.ix

    def assign(self, **kwargs):
        # In for now, but may be removed if it's inconsistent with the API
        return from_panda(self._df.assign(**kwargs))

    def describe(self, percentiles=None, include=None, exclude=None):
        return from_panda(self._df.describe(percentiles=percentiles, include=include, exclude=exclude))

    def info(self, verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None):
        self._df.info(verbose=verbose, buf=buf, max_cols=max_cols, memory_usage=memory_usage, null_counts=null_counts)

    def replace(self, to_replace=None, value=None, limit=None, regex=False, method='pad', axis=None):
        return from_panda(
            self._df.replace(to_replace=to_replace, value=value, inplace=False, limit=limit, regex=regex, method=method,
                             axis=axis))

    def count(self, axis=0, level=None, numeric_only=False):
        return from_panda(self._df.count(axis=axis, level=level, numeric_only=numeric_only))


if __name__ == '__main__':
    print baby_panda()
