import os
import json
import time
import logging
import requests
from typing import Dict, Any, Optional,List
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# ===================== U8 接口基础配置 =====================
U8_OPENAPI_URL = "https://api.yonyouup.com"

class U8OpenAPIClient:
    def __init__(self):
        self.app_key = os.getenv("U8_OPENAPI_APPKEY")
        self.app_secret = os.getenv("U8_OPENAPI_APPSECRET")
        self.from_account = os.getenv("U8_OPENAPI_FROM_ACCOUNT")
        self.to_account = os.getenv("U8_OPENAPI_TO_ACCOUNT")
        self.token_expire_time = 0
        self.token = None
    def get_access_token(self) -> str:

        if self.token and time.time() < self.token_expire_time:
            return self.token
        
        url = f"{U8_OPENAPI_URL}/system/token"
        payload = {
            "from_account": self.from_account,
            "app_key": self.app_key,
            "app_secret": self.app_secret
        }

        response = requests.get(url, params=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("errcode") == "0":
            self.token = data["token"]["id"]
            expires_in = data.get("expiresIn", 7200)
            self.token_expire_time = time.time() + expires_in - 60  # 提前1分钟过期
        
        return self.token

    def get_access_tradeid(self) -> str:
        """获取交易ID"""
        token = self.get_access_token()
        
        url = f"{U8_OPENAPI_URL}/system/tradeid"
        payload = {
            "from_account": self.from_account,
            "app_key": self.app_key,
            "token": token
        }

        response = requests.get(url, params=payload)
        response.raise_for_status()
        data = response.json()
        if data.get("errcode") == "0":
            tradeid = data["trade"]["id"]
        
        return tradeid
    
    def user_login_v2(self,token:str, tradeid:str)->str:
        """用户登录"""

        url = f"{U8_OPENAPI_URL}/api/user/login_v2"

        inparams = {
            "from_account": self.from_account,
            "to_account": self.to_account,
            "app_key": self.app_key,
            "token": token,
            "tradeid": tradeid,
            "user_id": "demo",
            "password": "DEMO"
        }

        json_body = {
            "user":{
            "user_id": "demo",
            "password": "DEMO"
            }
        }

        resp = requests.post(url, params=inparams, json=json_body)
        resp.raise_for_status()
        data = resp.json()
        return data

    
    def request_api(self, method: str, path: str, inparams: Optional[Dict] = None, json_body: Optional[Dict] = None, is_tradeid: bool = False,is_user_login_v2=False) -> Dict[str, Any]:
        """通用API请求方法"""
        token = self.get_access_token()
        url = f"{U8_OPENAPI_URL}{path}"
        
        headers = {
            "Content-Type": "application/json"
        }

        try:
            if method.upper() == "GET":

                # 公共参数
                public_params = {
                    "from_account": self.from_account,
                    "to_account": self.to_account,
                    "app_key": self.app_key,
                    "token": token,
                }
        
                # 合并参数：公共参数在前，用户参数在后（用户参数优先级高）
                if inparams:
                    params = {**public_params, **inparams}
                else:
                    params = public_params
        
                resp = requests.get(url, params=params, headers=headers)
                resp.raise_for_status()
                return resp.json()
            
            elif method.upper() == "POST":
                tradeid=self.get_access_tradeid()
                if is_tradeid:
                    # 公共参数
                    public_params = {
                        "from_account": self.from_account,
                        "to_account": self.to_account,
                        "app_key": self.app_key,
                        "token": token,
                        "tradeid": tradeid,
                    }
                else:
                    public_params = {
                        "from_account": self.from_account,
                        "to_account": self.to_account,
                        "app_key": self.app_key,
                        "token": token,
                    }

                if is_user_login_v2:
                    userinfo=self.user_login_v2(token=token,tradeid=tradeid)
        
                # 合并参数：公共参数在前，用户参数在后（用户参数优先级高）
                if inparams:
                    params = {**public_params, **inparams}
                else:
                    params = public_params
        
                resp = requests.post(url, params=params, json=json_body, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                result_url=data.get("url")
                if result_url:
                    time.sleep(3)
                    result_response = requests.get(result_url)
                    result_response.raise_for_status()
                    result_data = result_response.json()
                else:
                    result_data = data
                
                if result_data.get("errcode") == "0":
                    # 如果 errmsg 缺失或为空字符串，则设置为“成功”
                    if not result_data.get("errmsg"):
                        result_data["errmsg"] = "成功"

                return result_data

            else:
                raise ValueError(f"Unsupported method: {method}")

        except Exception as e:
            return {"error": str(e), "status_code": getattr(resp, 'status_code', None)}
        
