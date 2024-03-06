import os
import json
import pandas as pd

path1="C:/Users/User/Phonepe/pulse/data/aggregated/transaction/country/india/state/"
aggre_trans_list= os.listdir(path1)

columns1={"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}
for state in aggre_trans_list:
    cur_states=path1+state+"/"
    agg_year_list=os.listdir(cur_states)

    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            A=json.load(data)

            for i in A["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))

path2="C:/Users/User/Phonepe/pulse/data/aggregated/transaction/country/india/state/"

columns2={"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in aggre_trans_list:
    cur_states=path2+state+"/"
    agg_year_list=os.listdir(cur_states)

    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            B=json.load(data)