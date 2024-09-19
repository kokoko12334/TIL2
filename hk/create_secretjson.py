import os
from pykis import KisAuth
from dotenv import load_dotenv

load_dotenv()

id = os.getenv("ID")

# 실전투자 json키
appkey = os.getenv("REAL_APPKEY")
appsecret = os.getenv("REAL_APPSECRET")
account = os.getenv("REAL_ACCOUNT")
auth = KisAuth(id=id, appkey=appkey, secretkey=appsecret, account=account, virtual=False)
auth.save("real_secret.json")


# 모의투자 json키
appkey = os.getenv("FAKE_APPKEY")
appsecret = os.getenv("FAKE_APPSECRET")
account = os.getenv("FAKE_ACCOUNT")
auth = KisAuth(id=id, appkey=appkey, secretkey=appsecret, account=account, virtual=True)
auth.save("fake_secret.json")


