import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from helpers.helpers import  retail_data_prep, check_df

df = pd.read_excel("datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")

######################################################
# Rule of Association:
######################################################

df_pivot = df.groupby(["Invoice", "StockCode"])["Quantity"].sum(). \
    unstack().fillna(0).applymap(lambda x: 1 if x > 0 else 0)
df_pivot.head(10)

frequent_items = apriori(df_pivot, min_support=0.01, use_colnames=True)
frequent_items.sort_values("support", ascending=False).head(20)

rules = association_rules(frequent_items, metric="support", min_threshold=0.01)
rules.sort_values("support", ascending=False).head(10)
rules.sort_values("lift", ascending=False).head(10)

######################################################
# Some stock codes are given, let's see product descriptions of the products
######################################################
# 21987
# 23235

def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)

product_id = 21987
check_id(df, product_id)
product_id_2 = 23235
check_id(df, product_id_2)

######################################################
# Product recommendation for above products
######################################################

def recommend_me(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])
    print(recommendation_list[0: rec_count])


recommend_me(rules, 21987)
recommend_me(rules, 23235, 3)

### Description of a recommended product:
recom_id = 21989
check_id(df, recom_id)