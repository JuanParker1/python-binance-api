from binance_client import BinanceClient
import pytest
import os
import time

SLEEP_TIME = 1

@pytest.fixture
def client():
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    return BinanceClient(api_key, api_secret)


def test_system_status(client):
    time.sleep(SLEEP_TIME)
    res = client.system_status()
    assert 'status' in res
    assert 'msg'in res
    


def test_all_coins_information(client):
    time.sleep(SLEEP_TIME)
    res = client.all_coins_information()
    if res:
        assert 'coin' in res[0]
        assert 'depositAllEnable'in res[0]
        assert 'free'in res[0]
        assert 'freeze'in res[0]
        assert 'ipoable'in res[0]
        assert 'ipoing'in res[0]
        assert 'isLegalMoney'in res[0]
        assert 'locked'in res[0]
        assert 'name'in res[0]
        assert 'networkList'in res[0]
        assert 'storage'in res[0]
        assert 'trading'in res[0]
        assert 'withdrawAllEnable'in res[0]
        assert 'withdrawing'in res[0]


def test_daily_account_snapshot(client):
    time.sleep(SLEEP_TIME)
    res = client.daily_account_snapshot('SPOT')
    assert 'code' in res
    assert 'msg' in res
    assert 'snapshotVos' in res


def test_disable_fast_withdraw_switch(client):
    time.sleep(SLEEP_TIME)
    res = client.disable_fast_withdraw_switch()
    assert not res
    

def test_enable_fast_withdraw_switch(client):
    time.sleep(SLEEP_TIME)
    res = client.enable_fast_withdraw_switch()
    assert not res


def test_withdraw(client):
    time.sleep(SLEEP_TIME)
    res = client.withdraw('ETH', '')
    assert 'id' in res


def test_deposit_history(client):
    time.sleep(SLEEP_TIME)
    res = client.deposit_history()
    if res:
        assert 'amount' in res[0]
        assert 'coin' in res[0]
        assert 'network' in res[0]
        assert 'status' in res[0]
        assert 'address' in res[0]
        assert 'addressTag' in res[0]
        assert 'txId' in res[0]
        assert 'insertTime' in res[0]
        assert 'transferType' in res[0]
        assert 'unlockConfirm' in res[0]
        assert 'confirmTimes' in res[0]


def test_withdraw_history(client):
    time.sleep(SLEEP_TIME)
    res = client.withdraw_history()
    if res:
        assert 'address' in res[0]
        assert 'amount' in res[0]
        assert 'applyTime' in res[0]
        assert 'coin' in res[0]
        assert 'id' in res[0]
        #assert 'withdrawOrderId' in res[0]
        assert 'network' in res[0]
        assert 'transferType' in res[0]
        assert 'status' in res[0]
        assert 'transactionFee' in res[0]
        assert 'confirmNo' in res[0]
        assert 'info' in res[0]
        assert 'txId' in res[0]
    

def test_deposit_address(client):
    time.sleep(SLEEP_TIME)
    res = client.deposit_address('BTC')
    assert 'address' in res
    assert 'coin' in res
    assert 'tag' in res
    assert 'url' in res


def test_account_status(client):
    time.sleep(SLEEP_TIME)
    res = client.account_status()
    assert 'data' in res


def test_account_api_trading_status(client):
    time.sleep(SLEEP_TIME)
    res = client.account_api_trading_status()
    assert 'data' in res


def test_dust_log(client):
    time.sleep(SLEEP_TIME)
    res = client.dust_log()
    assert 'total' in res
    assert 'userAssetDribblets' in res


def test_get_assets_that_can_be_convertes_into_bnb(client):
    time.sleep(SLEEP_TIME)
    res = client.get_assets_that_can_be_convertes_into_bnb()
    assert 'details' in res
    assert 'totalTransferBtc' in res
    assert 'totalTransferBNB' in res
    assert 'dribbletPercentage' in res


def test_dust_transfer(client):
    time.sleep(SLEEP_TIME)
    res = client.dust_transfer(['BTC', 'USDT'])
    assert 'totalServiceCharge' in res
    assert 'totalTransfered' in res
    assert 'transferResult' in res


def test_asset_dividend_record(client):
    time.sleep(SLEEP_TIME)
    res = client.asset_dividend_record()
    assert 'rows' in res
    assert 'total' in res


def test_asset_detail(client):
    time.sleep(SLEEP_TIME)
    res = client.asset_detail('BTC')
    assert 'BTC' in res


def test_trade_fee(client):
    time.sleep(SLEEP_TIME)
    res = client.trade_fee('BTC')
    if res:
        assert 'symbol' in res[0]
        assert 'makerCommission' in res[0]
        assert 'takerCommission' in res[0]

def test_user_universal_transfer(client):
    time.sleep(SLEEP_TIME)
    res = client.user_universal_transfer('MAIN_UMFUTURE', 'BTC', 0.0001)
    assert 'tranId' in res


def test_query_user_universal_transfer(client):
    time.sleep(SLEEP_TIME)
    res = client.query_user_universal_transfer('MAIN_UMFUTURE')
    assert 'total' in res
    if 'total'in res:
        if res['total'] > 0:
            assert 'rows' in res


def test_funding_wallet(client):
    time.sleep(SLEEP_TIME)
    res = client.funding_wallet()
    if res:
        assert 'asset' in res[0]
        assert 'free' in res[0]
        assert 'locked' in res[0]
        assert 'freeze' in res[0]
        assert 'withdrawing' in res[0]
        assert 'btcValuation' in res[0]
        

def test_get_api_key_permissions(client):
    time.sleep(SLEEP_TIME)
    res = client.get_api_key_permissions()
    assert 'ipRestrict' in res
    assert 'createTime' in res
    assert 'enableWithdrawals' in res
    assert 'enableInternalTransfer' in res
    assert 'permitsUniversalTransfer' in res
    assert 'enableVanillaOptions' in res
    assert 'enableReading' in res
    assert 'enableFutures' in res
    assert 'enableMargin' in res
    assert 'enableSpotAndMarginTrading' in res
    #assert 'tradingAuthorityExpirationTime' in res
