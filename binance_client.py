from pytest import param
from requests import get, post
from datetime import datetime





class BinanceClient():

    api_url = "https://api.binance.com"


    def __inti__(self):
        pass

    

    def system_status(self):
        """
        System Status (System)

        GET /sapi/v1/system/status

        Fetch system status.
        """
        params = locals()
        print(params)
        params = self._get_parameters(params)
        print(params)
        endpoint_url = f"{self.api_url}/sapi/v1/system/status"
        response = get(endpoint_url, params=params)
        response.raise_for_status()
        return response.json()



    def all_coins_information(self, 
                            recvWindow: int = None):
        """
        All Coins' Information (USER_DATA)

        GET /sapi/v1/capital/config/getall (HMAC SHA256)

        Get information of coins (available for deposit and withdraw) for user.	
        """
        params = locals()
        print(params)
        params = self._get_parameters(params)
        print(params)
        endpoint_url = f"{self.api_url}/sapi/v1/capital/config/getall"
        response = get(endpoint_url, params=params)
        response.raise_for_status()
        return response.json()


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
        endpoint_url = f"{self.api_url}/sapi/v1/accountSnapshot"
        response = get(endpoint_url)
        response.raise_for_status()
        return response.json()


    def disable_fast_withdraw_switch(self, 
                                    recvWindow=None):
        """
        Disable Fast Withdraw Switch (USER_DATA)

        POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)
        """
        endpoint_url = f"{self.api_url}/sapi/v1/account/disableFastWithdrawSwitch"
        response = post(endpoint_url)
        response.raise_for_status()
        return response.json()



    def enable_fast_withdraw_switch(self, 
                                    recvWindow=None):
        """
        Enable Fast Withdraw Switch (USER_DATA)

        POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)
        """
        endpoint_url = f"{self.api_url}/sapi/v1/account/enableFastWithdrawSwitch"
        response = post(endpoint_url)
        response.raise_for_status()
        return response.json()



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
        endpoint_url = f"{self.api_url}/sapi/v1/capital/withdraw/apply"
        response = post(endpoint_url)
        response.raise_for_status()
        return response.json()


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
        endpoint_url = f"{self.api_url}/sapi/v1/capital/deposit/hisrec"
        response = get(endpoint_url)
        response.raise_for_status()
        return response.json()
        


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
        endpoint_url = f"{self.api_url}/sapi/v1/capital/withdraw/history"
        response = get(endpoint_url)
        response.raise_for_status()
        return response.json()

    

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
        endpoint_url = f"{self.api_url}/sapi/v1/capital/deposit/address"
        response = get(endpoint_url)
        response.raise_for_status()
        return response.json()


    def account_status(self,
                        recv_window: int = None):
        """
        Account Status (USER_DATA)

        GET /sapi/v1/account/status

        Fetch account status detail.
        """
        endpoint_url = f"{self.api_url}/sapi/v1/account/status"
        response = get(endpoint_url)
        response.raise_for_status()
        return response.json()














    def _get_timestamp(self):
        now = datetime.now()
        return round(datetime.timestamp(now))


    def _get_parameters(self, params):
        del params['self']
        for key in list(params):
            if params[key] == None: del params[key]
        params['timestamp'] = self._get_timestamp()
        return params

bc = BinanceClient()
bc.system_status()
bc.all_coins_information()