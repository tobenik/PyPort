import configparser

config = configparser.ConfigParser()
config['datapaths'] = {}
config['datapaths']['transactions'] = 'data/transactions.csv'
config['datapaths']['test_transactions'] = 'tests/testdata/transactions.csv'

with open('config/config.ini', 'w') as configFile:
    config.write(configFile)
