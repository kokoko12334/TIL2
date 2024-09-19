import requests
import json

class KisApi():
    real_domain = "https://openapi.koreainvestment.com:9443"
    fake_domain = "https://openapivts.koreainvestment.com:29443"

    def __init__(self, appkey: str, appsecret: str, account: str):
        self.appkey = appkey
        self.appsecret = appsecret

        account_no, product_code  = account.split("-")
        self.account_no =account_no
        self.product_code = product_code
        self.access_token = ""
        
    def get_access_token(self) -> None:
        if self.access_token:
            return
         
        url = f"{self.real_domain}/oauth2/tokenP"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }

        payload = {
            "grant_type": "client_credentials",
            "appkey": self.appkey,
            "appsecret": self.appsecret
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            return
        raise Exception(f"Error: {response.status_code}, {response.text}")

    def get_fluctuation_rank(self, fid_input_iscd="0000", fid_rank_sort_cls_code="0") -> dict:
        if not self.access_token:
            raise Exception("no access_token")
        
        url = f"{self.real_domain}/uapi/domestic-stock/v1/ranking/fluctuation"

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f'Bearer {self.access_token}', 
            'appkey': self.appkey,
            'appsecret': self.appsecret,
            'tr_id': 'FHPST01700000',
            'custtype': 'P'
        }

        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_cond_scr_div_code": "20170",
            "fid_input_iscd": fid_input_iscd,
            "fid_rank_sort_cls_code": fid_rank_sort_cls_code,
            "fid_input_cnt_1": "0",
            "fid_prc_cls_code": "0",  
            "fid_input_price_1": "",  
            "fid_input_price_2": "", 
            "fid_vol_cnt": "", 
            "fid_trgt_cls_code": "0",
            "fid_trgt_exls_cls_code": "0",  
            "fid_div_cls_code": "0",
            "fid_rsfl_rate1": "", 
            "fid_rsfl_rate2": "",
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()['output']
        
        raise Exception(f"Error: {response.status_code}, {response.text}")


    def inquire_account_balance(self):
        """
        계좌 자산현황 조회 API 호출

        Returns:
        - 잔고 조회 결과 (JSON 형식)
        """
    
        url = f"{self.real_domain}/uapi/domestic-stock/v1/trading/inquire-account-balance"

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'authorization': f'Bearer {self.access_token}',
            'appkey': self.appkey,
            'appsecret': self.appsecret,
            'tr_id': 'CTRP6548R'
        }

        params = {
            'CANO': self.account_no,
            'ACNT_PRDT_CD': self.product_code,
            'INQR_DVSN_1': "",
            'BSPR_BF_DT_APLY_YN': ""
        }

        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f"Error: {response.status_code}, {response.text}")

    def inquire_balance(self, inqr_dvsn="01", prcs_dvsn="00", is_real=True):
        """
        주식 잔고 조회 API 호출

        Parameters:
        - inqr_dvsn: 01(대출일별), 02(종목별)
        - prcs_dvsn: 00(전일매매포함), 01(전일매매미포함)
        - is_real: True(실전), False(모의)

        Returns:
        - 잔고 조회 결과 (JSON 형식)
        """

        self.base_url = self.real_domain if is_real else self.fake_domain
    
        url = f"{self.base_url}/uapi/domestic-stock/v1/trading/inquire-balance"

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'authorization': f'Bearer {self.access_token}',
            'appkey': self.appkey,
            'appsecret': self.appsecret,
            'tr_id': 'TTTC8434R' if is_real else 'VTTC8434R'
        }

        params = {
            'CANO': self.account_no,
            'ACNT_PRDT_CD': self.product_code,
            'AFHR_FLPR_YN': "N",
            'OFL_YN': '',
            'INQR_DVSN': inqr_dvsn,
            'UNPR_DVSN': "01",
            'FUND_STTL_ICLD_YN': "N",
            'FNCG_AMT_AUTO_RDPT_YN': "N",
            'PRCS_DVSN': prcs_dvsn,
            'CTX_AREA_FK100': "",
            "CTX_AREA_NK100": ""
        }

        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f"Error: {response.status_code}, {response.text}")


    def inquire_possible_order(self, pdno, ord_unpr="", ord_dvsn="00", is_real=True):
        
        """
        매수 가능 조회 API 호출

        Parameters:
        - pdno: 종목번호(6자리) * PDNO, ORD_UNPR 공란 입력 시, 매수수량 없이 매수금액만 조회됨
        - ord_unpr: 1주당 가격 * 시장가(ORD_DVSN:01)로 조회 시, 공란으로 입력
        - ord_dvsn: 특정 종목 전량매수 시 가능수량을 확인할 경우
        - is_real: True(실전), False(모의)

        Returns:
        - 조회 결과 (JSON 형식)
        """
        self.base_url = self.real_domain if is_real else self.fake_domain
        url = f"{self.base_url}/uapi/domestic-stock/v1/trading/inquire-psbl-order"

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'authorization': f'Bearer {self.access_token}',
            'appkey': self.appkey,
            'appsecret': self.appsecret,
            'tr_id': 'TTTC8434R' if is_real else 'VTTC8434R'
        }

        params = {
            "CANO": self.account_no,
            "ACNT_PRDT_CD": self.product_code,
            "PDNO": pdno,
            "ORD_UNPR": ord_unpr,
            "ORD_DVSN": ord_dvsn,
            "CMA_EVLU_AMT_ICLD_YN": "N",
            "OVRS_ICLD_YN": 'N'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        
        raise Exception(f"Error: {response.status_code}, {response.text}")



from dotenv import load_dotenv
import os

load_dotenv()

#token

appkey = os.getenv("REAL_APPKEY")
appsecret = os.getenv("REAL_APPSECRET")
account = os.getenv("REAL_ACCOUNT")

kis = KisApi(appkey=appkey, appsecret=appsecret, account=account)
kis.get_access_token()

# 주식잔고 조회
result = kis.inquire_balance(is_real=False)
result

#계좌잔액 조회
result = kis.inquire_account_balance()
result

##랭킹
result = kis.get_fluctuation_rank()
for i in range(len(result)):
    re = result[i]
    if float(re['prdy_ctrt']) >= 10.0:
        print(f"순위:{re['data_rank']}위 종목:{re['hts_kor_isnm']}({re['stck_shrn_iscd']}), 등락:{re['prdy_ctrt']}, 현재가:{re['stck_prpr']}, 거래량:{re['acml_vol']}")




#주문 가능금액
kis.inquire_possible_order()

