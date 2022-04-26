from binance_client import BinanceClient
import pytest


@pytest.fixture
def client():
    return BinanceClient()


def test_system_status(client):
    res = client.system_status()
    assert 'status' in res
    assert 'msg'in res


def test_all_coins_information(client):
    res = client.all_coins_information()
    assert 'coin' in res
    assert 'depositAllEnable'in res
    assert 'free'in res
    assert 'freeze'in res
    assert 'ipoable'in res
    assert 'ipoing'in res
    assert 'isLegalMoney'in res
    assert 'locked'in res
    assert 'name'in res
    assert 'msgnetworkList'in res
    assert 'storage'in res
    assert 'trading'in res
    assert 'withdrawAllEnable'in res
    assert 'withdrawing'in res


# def test_daily_account_snapshot(client):
#     res = client.daily_account_snapshot()
#     assert 'code' in res
#     assert 'msg' in res
#     assert 'snapshotVos' in res



# def test_disable_fast_withdraw_switch(client):
#     res = client.disable_fast_withdraw_switch()
    

# def test_enable_fast_withdraw_switch(client):
#     res = client.enable_fast_withdraw_switch()


# def test_withdraw(client):
#     res = client.withdraw()
#     assert 'id' in res



# def test_deposit_history(client):
#     res = client.deposit_history()




    


