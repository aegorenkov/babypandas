from unittest import TestCase


class TestRead_csv(TestCase):
    def test_read_csv(self):
        #Just a collection of common cases for now
        users = pandas.read_csv("data/users.csv", header=None)
        views = pandas.read_csv("data/views.csv", header=None, low_memory=False)
        gtap_emis = pd.read_csv("tot_emis_gtap.csv",header=None,names=["country","emis"],index_col = "country", squeeze=True)
        iea_emis=pd.read_csv("carbon_emissions_from_iea.csv",skiprows=[1],na_values=[".."])
        data=pandas.read_csv("Galton.csv",sep="\t")
        read_csv('data/schools/J390307_2030_GeoPolicy_LSOA.csv', usecols=[0,2])
        pandas.read_csv(r'C:\Python27\Lib\site-packages\pandas\tests\data\iris.csv', sep=',')
        pd.read_csv('Data/SyriaIDPSites2015LateJunHIUDoS.csv', encoding='latin-1')
        converters = {
        "name": lambda x: x.strip()
        }
        stations = pandas.read_csv('../data/psmsl/rlr_annual/filelist.txt', sep=';',
                     names=metadata_fields, dtype=dtypes,
                    converters=converters)
        pd.read_csv('cars.csv', index_col=0)
        pd.read_csv('ad.data', header=None, delimiter='\t')