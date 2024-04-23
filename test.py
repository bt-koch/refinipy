import sys
sys.path.append("../")
import get_data
import config
import utils

config.connect()
banks_meta = get_data.read_meta()
ric_equity = get_data.ric_equity(banks_meta)
ric_cds = get_data.ric_cds(ric_equity)
cds = get_data.get_cds(ric_cds)
cds.head
utils.export_csv(cds, "dataset_cds")
p2b = get_data.get_price_to_book(ric_equity)
p2b.head
utils.export_csv(p2b, "dataset_p2b")