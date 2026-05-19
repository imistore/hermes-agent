import json
import logging
from typing import Dict, Any, Optional,List
from pydantic import BaseModel, Field
from .u8_openapi_client import U8OpenAPIClient

# ===================== 日志配置 =====================
logger = logging.getLogger(__name__)





# ===================== 添加一个新客户 子数据模型 =====================
class Addresses(BaseModel):
    ccuscode: Optional[str] = Field(None, description="客户编码")
    caddcode: Optional[str] = Field(None, description="收货地址编码")
    bdefault: Optional[bool] = Field(None, description="默认值（1/0）")
    cdeliveradd: Optional[str] = Field(None, description="收货地址")
    cenglishadd: Optional[str] = Field(None, description="英文地址")
    cenglishadd2: Optional[str] = Field(None, description="英文地址2")
    cenglishadd3: Optional[str] = Field(None, description="英文地址3")
    cenglishadd4: Optional[str] = Field(None, description="英文地址4")
    cdeliverunit: Optional[str] = Field(None, description="收货单位")
    clinkperson: Optional[str] = Field(None, description="联系人")

class Banks(BaseModel):
    ccuscode: Optional[str] = Field(None, description="客户编码")
    caccountnum: Optional[str] = Field(None, description="银行账号")
    bdefault: Optional[bool] = Field(None, description="默认值（1/0）")
    cbank: Optional[str] = Field(None, description="所属银行编码")
    cbranch: Optional[str] = Field(None, description="开户银行")
    caccountname: Optional[str] = Field(None, description="账户名称")
    cCusPrinvince: Optional[str] = Field(None, description="省")
    cCusCity: Optional[str] = Field(None, description="市")
    cCusCBBDepId: Optional[str] = Field(None, description="机构号")
    cCusBranchId: Optional[str] = Field(None, description="联行号")
    cCusBranchIdSec: Optional[str] = Field(None, description="联行号II")

class Invoicecustomers(BaseModel):
    ccuscode: Optional[str] = Field(None, description="客户编码")
    cinvoicecompany: Optional[str] = Field(None, description="开票单位编码")
    bdefault: Optional[bool] = Field(None, description="默认值（1/0）")

class Users(BaseModel):
    ccuscode: Optional[str] = Field(None, description="客户编码")
    user_id: Optional[str] = Field(None, description="操作员编码")
    is_self: Optional[bool] = Field(None, description="相关或负责员工(true/false)")

class Auths(BaseModel):
    ccuscode: Optional[str] = Field(None, description="客户编码")
    privilege_type: Optional[str] = Field(None, description="管理维度类型编码")
    privilege_id: Optional[str] = Field(None, description="管理维度编码")

# ===================== 添加一个新客户 主数据模型 =====================
class AddCustomerInfoInput(BaseModel):
    code: str = Field(..., description="客户编码")
    name: str = Field(..., description="客户名称")
    abbrname: Optional[str] = Field(None, description="客户简称")
    sort_code: Optional[str] = Field(None, description="所属分类码")
    domain_code: Optional[str] = Field(None, description="所属地区码")
    industry: Optional[str] = Field(None, description="所属行业")
    contact: Optional[str] = Field(None, description="联系人")
    phone: Optional[str] = Field(None, description="电话")
    fax: Optional[str] = Field(None, description="传真")
    mobile: Optional[str] = Field(None, description="手机")
    devliver_site: Optional[str] = Field(None, description="发货地址")
    end_date: Optional[str] = Field(None, description="停用日期")
    memo: Optional[str] = Field(None, description="备注")
    ccusexch_name: Optional[str] = Field(None, description="币种")
    bcusdomestic: Optional[str] = Field(None, description="国内")
    bcusoverseas: Optional[str] = Field(None, description="国外")
    bserviceattribute: Optional[str] = Field(None, description="服务")
    self_define1: Optional[str] = Field(None, description="自定义项1")
    self_define2: Optional[str] = Field(None, description="自定义项2")
    self_define3: Optional[str] = Field(None, description="自定义项3")
    self_define4: Optional[str] = Field(None, description="自定义项4")
    self_define5: Optional[str] = Field(None, description="自定义项5")
    self_define6: Optional[str] = Field(None, description="自定义项6")
    self_define7: Optional[str] = Field(None, description="自定义项7")
    self_define8: Optional[str] = Field(None, description="自定义项8")
    self_define9: Optional[str] = Field(None, description="自定义项9")
    self_define10: Optional[str] = Field(None, description="自定义项10")
    self_define11: Optional[str] = Field(None, description="自定义项11")
    self_define12: Optional[str] = Field(None, description="自定义项12")
    self_define13: Optional[str] = Field(None, description="自定义项13")
    self_define14: Optional[str] = Field(None, description="自定义项14")
    self_define15: Optional[str] = Field(None, description="自定义项15")
    self_define16: Optional[str] = Field(None, description="自定义项16")
    addresses: Optional[List[Addresses]] = Field(None, description="地址信息列表")
    banks: Optional[List[Banks]] = Field(None, description="银行信息列表")
    invoicecustomers: Optional[List[Invoicecustomers]] = Field(None, description="开票客户信息列表")
    users: Optional[List[Users]] = Field(None, description="用户信息列表")
    auths: Optional[List[Auths]] = Field(None, description="权限信息列表")

# ===================== 获取单个客户信息 数据模型 =====================
class GetCustomerInfoInput(BaseModel):
    id: str = Field(..., description="客户编号，用于查询客户详细信息")


# ===================== 添加一个新客户 Tool函数 =====================
def u8_customer_add_tool(input_data: AddCustomerInfoInput, client: U8OpenAPIClient) -> str:
    """
    向用友U8系统中添加新的客户信息。
    """
    # 1. 构造接口要求的标准 JSON 结构（外层必须包一层 customer）
    request_body: Dict[str, Any] = {
        "customer": input_data.model_dump(exclude_none=True)
    }

    # 2. 固定接口路径
    api_path = "/api/customer/add" 
    
    try:
        # 3. 核心：POST 请求
        # inparams = None（公共参数由 U8OpenAPIClient 自动拼接）
        # json_body = 完整的请求体（必须带外层 customer）

        result = client.request_api("POST", api_path, inparams=None, json_body=request_body,is_tradeid=True)
        
        # 4. 统一返回格式
        if str(result.get("errcode", "")) != "0":
            return json.dumps({
                "success": False,
                "error": result.get("errmsg", "接口调用失败"),
                "raw_response": result
            }, ensure_ascii=False, indent=2)

        return json.dumps({
            "success": True,
            "message": "客户新增成功",
            "raw_response": result
        }, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({
            "success": False,
            "error": f"程序异常：{str(e)}"
        }, ensure_ascii=False, indent=2)

# ===================== 获取单个客户信息 Tool函数 =====================
def u8_customer_get_tool(input_data: GetCustomerInfoInput, client: U8OpenAPIClient) -> str:
    """
    通过客户编号获取用友U8中的客户基本信息。
    """
    params = {
        "id": input_data.id 
    }
    
    # 修改点3: 更新API路径
    api_path = "/api/customer/get" 
    
    try:
        # 使用 GET 或 POST 取决于具体接口要求，这里假设是 GET 请求带参数
        result = client.request_api("GET", api_path, inparams=params)
        
        # 检查业务错误码 (可选，根据实际返回结构调整)
        if result.get("errcode") != "0":
            return json.dumps({"error": result.get("errmsg", "Unknown error"), "data": result}, ensure_ascii=False)
            
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)
 






# ===================== 添加一个新客户 Schema定义 =====================
U8_CUSTOMER_ADD_SCHEMA = {
    "name": "u8_customer_add",
    "description": "在用友U8 OpenAPI中新增客户，支持客户主信息、地址、银行账户、开票单位、负责员工、数据权限等完整信息录入",
    "parameters": {
        "type": "object",
        "properties": {
            # 客户主信息
            "code": {
                "type": "string",
                "description": "客户编码（必填）"
            },
            "name": {
                "type": "string",
                "description": "客户名称（必填）"
            },
            "abbrname": {
                "type": "string",
                "description": "客户简称"
            },
            "sort_code": {
                "type": "string",
                "description": "所属分类编码"
            },
            "domain_code": {
                "type": "string",
                "description": "地区编码"
            },
            "industry": {
                "type": "string",
                "description": "所属行业"
            },
            "contact": {
                "type": "string",
                "description": "联系人"
            },
            "phone": {
                "type": "string",
                "description": "固定电话"
            },
            "fax": {
                "type": "string",
                "description": "传真"
            },
            "mobile": {
                "type": "string",
                "description": "手机号码"
            },
            "devliver_site": {
                "type": "string",
                "description": "发货地址"
            },
            "end_date": {
                "type": "string",
                "description": "停用日期，格式：yyyy-MM-dd"
            },
            "memo": {
                "type": "string",
                "description": "备注信息"
            },
            "ccusexch_name": {
                "type": "string",
                "description": "币种"
            },
            "bcusdomestic": {
                "type": "string",
                "description": "是否国内客户"
            },
            "bcusoverseas": {
                "type": "string",
                "description": "是否国外客户"
            },
            "bserviceattribute": {
                "type": "string",
                "description": "服务属性"
            },

            # 自定义项 1~16
            "self_define1": {"type": "string", "description": "自定义项1"},
            "self_define2": {"type": "string", "description": "自定义项2"},
            "self_define3": {"type": "string", "description": "自定义项3"},
            "self_define4": {"type": "string", "description": "自定义项4"},
            "self_define5": {"type": "string", "description": "自定义项5"},
            "self_define6": {"type": "string", "description": "自定义项6"},
            "self_define7": {"type": "string", "description": "自定义项7"},
            "self_define8": {"type": "string", "description": "自定义项8"},
            "self_define9": {"type": "string", "description": "自定义项9"},
            "self_define10": {"type": "string", "description": "自定义项10"},
            "self_define11": {"type": "string", "description": "自定义项11"},
            "self_define12": {"type": "string", "description": "自定义项12"},
            "self_define13": {"type": "string", "description": "自定义项13"},
            "self_define14": {"type": "string", "description": "自定义项14"},
            "self_define15": {"type": "string", "description": "自定义项15"},
            "self_define16": {"type": "string", "description": "自定义项16"},

            # 子表：收货地址（数组）
            "addresses": {
                "type": "array",
                "description": "收货地址列表",
                "items": {
                    "type": "object",
                    "properties": {
                        "ccuscode": {"type": "string", "description": "客户编码"},
                        "caddcode": {"type": "string", "description": "地址编码"},
                        "bdefault": {"type": "boolean", "description": "是否默认地址：true=是，false=否"},
                        "cdeliveradd": {"type": "string", "description": "收货地址"},
                        "cenglishadd": {"type": "string", "description": "英文地址"},
                        "cenglishadd2": {"type": "string", "description": "英文地址2"},
                        "cenglishadd3": {"type": "string", "description": "英文地址3"},
                        "cenglishadd4": {"type": "string", "description": "英文地址4"},
                        "cdeliverunit": {"type": "string", "description": "收货单位"},
                        "clinkperson": {"type": "string", "description": "联系人"}
                    }
                }
            },

            # 子表：银行账户（数组）
            "banks": {
                "type": "array",
                "description": "银行账户信息列表",
                "items": {
                    "type": "object",
                    "properties": {
                        "ccuscode": {"type": "string", "description": "客户编码"},
                        "caccountnum": {"type": "string", "description": "银行账号"},
                        "bdefault": {"type": "boolean", "description": "是否默认账户：true=是，false=否"},
                        "cbank": {"type": "string", "description": "银行编码"},
                        "cbranch": {"type": "string", "description": "开户支行"},
                        "caccountname": {"type": "string", "description": "账户名称"},
                        "cCusPrinvince": {"type": "string", "description": "省"},
                        "cCusCity": {"type": "string", "description": "市"},
                        "cCusCBBDepId": {"type": "string", "description": "机构号"},
                        "cCusBranchId": {"type": "string", "description": "联行号"},
                        "cCusBranchIdSec": {"type": "string", "description": "联行号II"}
                    }
                }
            },

            # 子表：开票单位（数组）
            "invoicecustomers": {
                "type": "array",
                "description": "开票单位列表",
                "items": {
                    "type": "object",
                    "properties": {
                        "ccuscode": {"type": "string", "description": "客户编码"},
                        "cinvoicecompany": {"type": "string", "description": "开票单位编码"},
                        "bdefault": {"type": "boolean", "description": "是否默认开票单位"}
                    }
                }
            },

            # 子表：负责员工（数组）
            "users": {
                "type": "array",
                "description": "负责员工列表",
                "items": {
                    "type": "object",
                    "properties": {
                        "ccuscode": {"type": "string", "description": "客户编码"},
                        "user_id": {"type": "string", "description": "操作员编码"},
                        "is_self": {"type": "boolean", "description": "是否负责员工：true=是，false=否"}
                    }
                }
            },

            # 子表：数据权限（数组）
            "auths": {
                "type": "array",
                "description": "数据权限列表",
                "items": {
                    "type": "object",
                    "properties": {
                        "ccuscode": {"type": "string", "description": "客户编码"},
                        "privilege_type": {"type": "string", "description": "管理维度类型编码"},
                        "privilege_id": {"type": "string", "description": "管理维度编码"}
                    }
                }
            }
        },
        "required": [
            "code",
            "name"
        ]
    }
}

# ===================== 获取单个客户信息 Schema定义 =====================
U8_CUSTOMER_GET_SCHEMA = {
    "name": "u8_customer_get",
    "description": "通过客户编码获得客户信息",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "客户编码"
            }
        },
        "required": ["id"]
    }
}


