
from iploc.loc_tools import ipinfo
from resources.mls_handler import MLS


if __name__ == '__main__':

    print("Running MLS checks")
    mls = MLS()
    print("Getting IP information")
    ip = ipinfo()
    mcc_dataset = mls.get_mcc(ip.mcc)
    print("Sorting dataset")
    sorted_dataset = mls.sort_data(mcc_dataset, ip.initial_coords)
