from pytest import param
from requests import get, post
from datetime import datetime
import hmac
import hashlib





class BinanceClient():

    api_url = "https://api.binance.com"


    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key


    

    def system_status(self):
        """
        System Status (System)

        GET /sapi/v1/system/status

        Fetch system status.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/system/status"
        return self._api_call('GET', endpoint_url, local_variables)




    def all_coins_information(self, 
                            recvWindow: int = None):
        """
        All Coins' Information (USER_DATA)

        GET /sapi/v1/capital/config/getall (HMAC SHA256)

        Get information of coins (available for deposit and withdraw) for user.	
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/capital/config/getall"
        return self._api_call('GET', endpoint_url, local_variables)



    def daily_account_snapshot(self, 
                            type: str, 
                            start_time: int = None, 
                            end_tme: int = None, 
                            limit: int = None, 
                            recvWindow: int = None):
        """
        Daily Account Snapshot (USER_DATA)

        GET /sapi/v1/accountSnapshot (HMAC SHA256)

        - The query time period must be less then 30 days
        - Support query within the last one month only
        - If startTimeand endTime not sent, return records of the last 7 days by default
        - limit min 7, max 30, default 7
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/accountSnapshot"
        return self._api_call('GET', endpoint_url, local_variables)



    def disable_fast_withdraw_switch(self, 
                                    recvWindow=None):
        """
        Disable Fast Withdraw Switch (USER_DATA)

        POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/account/disableFastWithdrawSwitch"
        return self._api_call('POST', endpoint_url, local_variables)




    def enable_fast_withdraw_switch(self, 
                                    recvWindow=None):
        """
        Enable Fast Withdraw Switch (USER_DATA)

        POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/account/enableFastWithdrawSwitch"
        return self._api_call('POST', endpoint_url, local_variables)



    def withdraw(self, 
                coin: str, 
                address: str, 
                withdraw_order_id: str = None, 
                network: str = None, 
                address_tag: str = None, 
                amount: float = None, 
                transaction_fee_flag: bool = None, 
                name: str = None, 
                wallet_type: int = None, 
                recv_window: str = None):
        """
        Withdraw(USER_DATA)

        POST /sapi/v1/capital/withdraw/apply (HMAC SHA256) 

        Submit a withdraw request.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/capital/withdraw/apply"
        return self._api_call('POST', endpoint_url, local_variables)



    def deposit_history(self,
                        coin: str = None,
                        status: int = None,
                        start_time: int = None,
                        end_time: int = None,
                        offset: int = None,
                        limit: int = None,
                        recv_window: int = None):
        """
        Deposit History(supporting network) (USER_DATA)

        GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)

        Fetch deposit history.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/capital/deposit/hisrec"
        return self._api_call('GET', endpoint_url, local_variables)

        


    def withdraw_history(self,
                        coin: str = None,
                        withdraw_order_id: str = None,
                        status: int = None,
                        offset: int = None,
                        limit: int = None,
                        start_time: int = None,
                        end_time: int = None,
                        recv_window: int = None):
        """
        Withdraw History (supporting network) (USER_DATA)

        GET /sapi/v1/capital/withdraw/history (HMAC SHA256)

        Fetch withdraw history.

        network may not be in the response for old withdraw.
        Please notice the default startTime and endTime to make sure that time interval is within 0-90 days.
        If both startTime and endTimeare sent, time between startTimeand endTimemust be less than 90 days.
        If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
        If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/capital/withdraw/history"
        return self._api_call('GET', endpoint_url, local_variables)


    

    def deposit_address(self,
                        coin: str, 
                        network: str = None,
                        recv_window: int = None):
        """
        Deposit Address (supporting network) (USER_DATA)

        GET /sapi/v1/capital/deposit/address (HMAC SHA256)

        Fetch deposit address with network.

        If network is not send, return with default network of the coin.
        You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC SHA256).
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/capital/deposit/address"
        return self._api_call('GET', endpoint_url, local_variables)



    def account_status(self, recv_window: int = None):
        """
        Account Status (USER_DATA)

        GET /sapi/v1/account/status

        Fetch account status detail.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/account/status"
        return self._api_call('GET', endpoint_url, local_variables)



    def account_api_trading_status(self, recv_window: int = None):
        """
        Account API Trading Status (USER_DATA)

        GET /sapi/v1/account/apiTradingStatus (HMAC SHA256) 

        Fetch account api trading status detail.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/account/apiTradingStatus"
        return self._api_call('GET', endpoint_url, local_variables)


    def dust_log(self,
                start_time: int = None,
                end_time: int = None,
                recv_window: int = None):
        """
        Dust Log (USER_DATA)

        GET /sapi/v1/asset/dribblet (HMAC SHA256) 	
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/dribblet"
        return self._api_call('GET', endpoint_url, local_variables)


    def get_assets_that_can_be_convertes_into_bnb(self, recv_window: int = None):
        """
        Get Assets That Can Be Converted Into BNB (USER_DATA)

        POST /sapi/v1/asset/dust-btc (HMAC SHA256)
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/dust-btc"
        return self._api_call('POST', endpoint_url, local_variables)


    def dust_transfer(self, 
                        asset: list,
                        recv_window: int = None):
        """
        Dust Transfer (USER_DATA)

        POST /sapi/v1/asset/dust (HMAC SHA256) 

        Convert dust assets to BNB.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/dust"
        return self._api_call('POST', endpoint_url, local_variables)


    def asset_dividend_record(self,
                            asset: str = None,
                            start_time: int = None,
                            end_time: int = None,
                            limit: int = None,
                            recv_window: int = None):
        """
        Asset Dividend Record (USER_DATA)

        GET /sapi/v1/asset/assetDividend (HMAC SHA256)

        Query asset dividend record.
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/assetDividend"
        return self._api_call('GET', endpoint_url, local_variables)


    def asset_detail(self,
                    asset: str = None,
                    recv_window: int = None):
        """
        Asset Detail (USER_DATA)
        
        GET /sapi/v1/asset/assetDetail (HMAC SHA256)

        Fetch details of assets supported on Binance.
        """ 
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/assetDetail"
        return self._api_call('GET', endpoint_url, local_variables)


    def trade_fee(self,
                symbol: str = None,
                recv_window: int = None):
        """
        Trade Fee (USER_DATA)

        GET /sapi/v1/asset/tradeFee (HMAC SHA256)

        Fetch trade fee
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/tradeFee"
        return self._api_call('GET', endpoint_url, local_variables)


    def user_universal_transfer(self,
                                type: str,
                                asset: str,
                                amount: float,
                                from_symbol: str = None,
                                to_symbol: str = None,
                                recv_window: int = None):
        """
        User Universal Transfer (USER_DATA)

        POST /sapi/v1/asset/transfer (HMAC SHA256) 

        You need to enable Permits Universal Transfer option for the API Key which requests this endpoint.


        fromSymbol must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        toSymbol must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

        ENUM of transfer types:
            MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
            MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
            MAIN_MARGIN Spot account transfer to Margin（cross）account
            UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
            UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin（cross）account
            CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
            CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
            MARGIN_MAIN Margin（cross）account transfer to Spot account
            MARGIN_UMFUTURE Margin（cross）account transfer to USDⓈ-M Futures
            MARGIN_CMFUTURE Margin（cross）account transfer to COIN-M Futures
            ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
            MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
            ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
            MAIN_FUNDING Spot account transfer to Funding account
            FUNDING_MAIN Funding account transfer to Spot account
            FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
            UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
            MARGIN_FUNDING MARGIN account transfer to Funding account
            FUNDING_MARGIN Funding account transfer to Margin account
            FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
            CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/transfer"
        return self._api_call('POST', endpoint_url, local_variables)


    def query_user_universal_transfer(self,
                                    type: str,
                                    start_time:int = None,
                                    end_time: int = None,
                                    current: int = None,
                                    size: int = None,
                                    from_symbol: str = None,
                                    to_symbol: str = None,
                                    recv_window: int = None):
        """
        Query User Universal Transfer History (USER_DATA)

        GET /sapi/v1/asset/transfer (HMAC SHA256)

        fromSymbol must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        toSymbol must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        Support query within the last 6 months only
        If startTimeand endTime not sent, return records of the last 7 days by default
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/transfer"
        return self._api_call('GET', endpoint_url, local_variables)


    def funding_wallet(self,
                        asset: str = None,
                        need_btc_valuation: str = None,
                        recv_window: int = None):
        """
        Funding Wallet (USER_DATA)

        POST /sapi/v1/asset/get-funding-asset (HMAC SHA256) 
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/asset/get-funding-asset"
        return self._api_call('POST', endpoint_url, local_variables)


    def get_api_key_permissions(self, recv_window: int = None):
        """
        Get API Key Permission (USER_DATA)

        GET /sapi/v1/account/apiRestrictions (HMAC SHA256) 
        """
        local_variables = locals()
        endpoint_url = f"{self.api_url}/sapi/v1/account/apiRestrictions"
        return self._api_call('GET', endpoint_url, local_variables)







    def _api_call(self, rest_method: str, endpoint_url: str, informed_params: dict):
        params = self._get_parameters(informed_params, sign=True)
        headers = self._get_header()

        if rest_method == 'GET':
            response = get(endpoint_url, params=params, headers=headers)
        elif rest_method == 'POST':
            response = post(endpoint_url, data=params, headers=headers)
        else:
            return {}
        
        response.raise_for_status()

        if response.content:
            return response.json()
        else:
            return {}



    def _get_timestamp(self):
        now = datetime.now()
        return round(datetime.timestamp(now))


    def _get_parameters(self, params, sign=True):
        del params['self']
        for key in list(params):
            if params[key] == None: del params[key]
        timestamp = (self._get_timestamp()*1000)-1000 # adjust to match the server
        params['timestamp'] = timestamp

        if sign: params = self._sign(params)

        return params


    def _sign(self, params):
        temp = []
        for key in params:
            if type(params[key]) is list:
                for item in params[key]:
                    temp.append(f"{key}={item}")
            else:
                temp.append(f"{key}={params[key]}")
        query = '&'.join(temp).encode('utf-8')
        signature = hmac.new(self.secret_key.encode('utf-8'), query, hashlib.sha256).hexdigest()
        params['signature'] = signature
        return params


    def _get_header(self):
        headers = dict()
        headers['X-MBX-APIKEY'] = self.api_key
        headers['Accept'] = "application/json"
        return headers
    


