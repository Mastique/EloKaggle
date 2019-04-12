# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:37:58 2019

@author: Mastique
"""

import pandas as pd
import pickle


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
historical_transactions = pd.read_csv('historical_transactions.csv')
merchants = pd.read_csv('merchants.csv')
new_merchant_transactions = pd.read_csv('new_merchant_transactions.csv')
sample_submission = pd.read_csv('sample_submission.csv')


        
pickle.dump(new_merchant_transactions,open('new_merchant_transactions.pkl','wb'))

test = subsample_new_merchant['merchant_id'].iloc[0]

"M_ID_55d9186a93" in subsample_new_merchant['merchant_id'].tolist()

dat = dat.merge(train, on = 'card_id')
