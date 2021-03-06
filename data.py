""" 
A script to identify the most retweeted tweets from curated user lists
"""
import pandas as pd
import json
import config

"""
# Grab  data from twitter and dump to text files.
"""

class GetData(object):

    def __init__(self):
        pass


    def get_tweets(self, listname, listcollection):
        for each_list in config.the_lists.values():
            for each_json_tweet in each_list:
                if each_list == config.the_lists[listname]:
                    listcollection.append(each_json_tweet._json)


    def make_txt(self, listname, tweets):
        with open('tweet_json_' + str(listname) + '.txt', 'w') as file:
            file.write(json.dumps(tweets, indent=4))


"""
# Set up dataframes object from text files
"""

class DataFrames(object):

    def __init__(self):
        pass

    def make_list(self, listname, textfile):
       with open(textfile, encoding='utf-8') as json_file:
            all_data = json.load(json_file)
            for each_dictionary in all_data:
                text = each_dictionary['text']
                retweet_count = each_dictionary['retweet_count']
                favorite_count = each_dictionary['favorite_count']
                user_name = each_dictionary['user']['name']
                created_at = each_dictionary['created_at']

                try:
                    url = each_dictionary['entities']['urls'][0]['url']
                except:
                    url = 'none'

                listname.append({'text': str(text),
                                     'retweet_count': int(retweet_count),
                                     'url': str(url),
                                     'combo': (int(retweet_count) + int(favorite_count)),
                                     'user_name': str(user_name),
                                     'created_at': str(created_at)
                                    })


    def make_DF(self, listname):
        listname =  pd.DataFrame(listname, columns =
                               ['text', 'retweet_count', 'combo', 'url', 'user_name', 'created_at'])
        listname = listname.nlargest(15, ['retweet_count'])
        return listname


"""
This code is still largely a mess but it is able to get the basic app working. Will definitely be cleaned up later.
"""

GetData().get_tweets('gaming', config.gaming_tweets), GetData().get_tweets('gurus', config.gurus_tweets), GetData().get_tweets('eth', config.eth_tweets), GetData().get_tweets('econ', config.econ_tweets)
GetData().get_tweets('ai', config.ai_tweets), GetData().get_tweets('btc', config.btc_tweets), GetData().get_tweets('space', config.space_tweets), GetData().get_tweets('systems', config.systems_tweets)
GetData().get_tweets('cryptofunds', config.cryptofunds_tweets), GetData().get_tweets('dao', config.dao_tweets), GetData().get_tweets('defi', config.defi_tweets), GetData().get_tweets('network', config.network_tweets)
GetData().get_tweets('politicaleconomy', config.politicaleconomy_tweets), GetData().get_tweets('psych', config.psych_tweets), GetData().get_tweets('techexecs', config.techexecs_tweets), GetData().get_tweets('vc', config.vc_tweets)


GetData().make_txt('gaming', config.gaming_tweets), GetData().make_txt('gurus', config.gurus_tweets), GetData().make_txt('eth', config.eth_tweets), GetData().make_txt('econ', config.econ_tweets)
GetData().make_txt('ai', config.ai_tweets), GetData().make_txt('btc', config.btc_tweets), GetData().make_txt('space', config.space_tweets), GetData().make_txt('systems', config.systems_tweets)
GetData().make_txt('cryptofunds', config.cryptofunds_tweets), GetData().make_txt('dao', config.dao_tweets), GetData().make_txt('defi', config.defi_tweets), GetData().make_txt('network', config.network_tweets)
GetData().make_txt('politicaleconomy', config.politicaleconomy_tweets), GetData().make_txt('psych', config.psych_tweets), GetData().make_txt('techexecs', config.techexecs_tweets), GetData().make_txt('vc', config.vc_tweets)



DataFrames().make_list(config.gaming_list, 'tweet_json_gaming.txt'), DataFrames().make_list(config.gurus_list, 'tweet_json_gurus.txt'), DataFrames().make_list(config.eth_list, 'tweet_json_eth.txt'), DataFrames().make_list(config.econ_list, 'tweet_json_econ.txt'),
DataFrames().make_list(config.ai_list, 'tweet_json_ai.txt'), DataFrames().make_list(config.btc_list, 'tweet_json_btc.txt'), DataFrames().make_list(config.space_list, 'tweet_json_space.txt'), DataFrames().make_list(config.systems_list, 'tweet_json_systems.txt')
DataFrames().make_list(config.cryptofunds_list, 'tweet_json_cryptofunds.txt'), DataFrames().make_list(config.dao_list, 'tweet_json_dao.txt'), DataFrames().make_list(config.defi_list, 'tweet_json_defi.txt'), DataFrames().make_list(config.network_list, 'tweet_json_network.txt'), DataFrames().make_list(config.politicaleconomy_list, 'tweet_json_politicaleconomy.txt'),
DataFrames().make_list(config.psych_list, 'tweet_json_psych.txt'), DataFrames().make_list(config.techexecs_list, 'tweet_json_techexecs.txt'), DataFrames().make_list(config.vc_list, 'tweet_json_vc.txt')



eth_df, gaming_df, gurus_df, econ_df, ai_df, btc_df, space_df, systems_df, cryptofunds_df, dao_df, defi_df, network_df, politicaleconomy_df, psych_df, techexecs_df, vc_df = DataFrames().make_DF(config.eth_list), DataFrames().make_DF(config.gaming_list), DataFrames().make_DF(config.gurus_list), DataFrames().make_DF(config.econ_list), DataFrames().make_DF(config.ai_list), DataFrames().make_DF(config.btc_list), DataFrames().make_DF(config.space_list), DataFrames().make_DF(config.systems_list), DataFrames().make_DF(config.cryptofunds_list), DataFrames().make_DF(config.dao_list), DataFrames().make_DF(config.defi_list), DataFrames().make_DF(config.network_list), DataFrames().make_DF(config.politicaleconomy_list), DataFrames().make_DF(config.psych_list), DataFrames().make_DF(config.techexecs_list), DataFrames().make_DF(config.vc_list)


eth_df.to_excel("ethexcel.xlsx"), gaming_df.to_excel("gamingexcel.xlsx"), gurus_df.to_excel("gurusexcel.xlsx"), econ_df.to_excel("econexcel.xlsx"),
ai_df.to_excel("aiexcel.xlsx"), btc_df.to_excel("btcxcel.xlsx"), space_df.to_excel("spaceexcel.xlsx"), systems_df.to_excel("systemsexcel.xlsx"), cryptofunds_df.to_excel("cryptofundsexcel.xlsx"),
dao_df.to_excel("daoexcel.xlsx"), defi_df.to_excel("defiexcel.xlsx"), network_df.to_excel("networkexcel.xlsx"), politicaleconomy_df.to_excel("politicaleconomyexcel.xlsx"),
psych_df.to_excel("psychexcel.xlsx"), techexecs_df.to_excel("techexecsexcel.xlsx"), vc_df.to_excel("vcexcel.xlsx")
