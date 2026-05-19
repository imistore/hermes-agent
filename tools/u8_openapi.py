
import os
import json
import time
import logging
import requests
from typing import Dict, Any, Optional,List
from pydantic import BaseModel, Field

from .u8_openapi_client import U8OpenAPIClient

from .u8_openapi_ba import (
    AddCustomerInfoInput,
    GetCustomerInfoInput,
    u8_customer_add_tool, 
    u8_customer_get_tool,
    U8_CUSTOMER_ADD_SCHEMA,
    U8_CUSTOMER_GET_SCHEMA
)

from .u8_openapi_ar import (
    AddAcceptInfoInput,
    GetAcceptInfoInput,
    GetAcceptListInfoInput,
    VerifyAcceptInfoInput,
    UnVerifyAcceptInfoInput,
    u8_accept_add_tool, 
    u8_accept_get_tool,
    u8_accept_list_get_tool,
    u8_accept_verify_tool,
    u8_accept_unverify_tool,
    U8_ACCEPT_ADD_SCHEMA,
    U8_ACCEPT_GET_SCHEMA,
    U8_ACCEPT_LIST_GET_SCHEMA,
    U8_ACCEPT_VERIFY_SCHEMA,
    U8_ACCEPT_UNVERIFY_SCHEMA,
    AddPayInfoInput,
    GetPayInfoInput,
    GetPayListInfoInput,
    VerifyPayInfoInput,
    UnVerifyPayInfoInput,
    u8_pay_add_tool,
    u8_pay_get_tool,
    u8_pay_list_get_tool,
    u8_pay_verify_tool,
    u8_pay_unverify_tool,
    U8_PAY_ADD_SCHEMA,
    U8_PAY_GET_SCHEMA,
    U8_PAY_LIST_GET_SCHEMA,
    U8_PAY_VERIFY_SCHEMA,
    U8_PAY_UNVERIFY_SCHEMA,
    AddOughtpayInfoInput,
    GetOughtpayInfoInput,
    GetOughtpayListInfoInput,
    VerifyOughtpayInfoInput,
    UnVerifyOughtpayInfoInput,
    u8_oughtpay_add_tool,
    u8_oughtpay_get_tool,
    u8_oughtpay_list_get_tool,
    u8_oughtpay_verify_tool,
    u8_oughtpay_unverify_tool,
    U8_OUGHTPAY_ADD_SCHEMA,
    U8_OUGHTPAY_GET_SCHEMA,
    U8_OUGHTPAY_LIST_GET_SCHEMA,
    U8_OUGHTPAY_VERIFY_SCHEMA,
    U8_OUGHTPAY_UNVERIFY_SCHEMA,
    AddOughtreceiveInfoInput,
    GetOughtreceiveInfoInput,
    GetOughtreceiveListInfoInput,
    VerifyOughtreceiveInfoInput,
    UnVerifyOughtreceiveInfoInput,
    u8_oughtreceive_add_tool,
    u8_oughtreceive_get_tool,
    u8_oughtreceive_list_get_tool,
    u8_oughtreceive_verify_tool,
    u8_oughtreceive_unverify_tool,
    U8_OUGHTRECEIVE_ADD_SCHEMA,
    U8_OUGHTRECEIVE_GET_SCHEMA,
    U8_OUGHTRECEIVE_LIST_GET_SCHEMA,
    U8_OUGHTRECEIVE_VERIFY_SCHEMA,
    U8_OUGHTRECEIVE_UNVERIFY_SCHEMA
)

# ===================== 日志配置 =====================
logger = logging.getLogger(__name__)

# ===================== 全局客户端单例 =====================
_u8_client_instance = None

def get_u8_client() -> "U8OpenAPIClient":
    """获取单例 U8 客户端，以复用 Token"""
    global _u8_client_instance
    if _u8_client_instance is None:
        _u8_client_instance = U8OpenAPIClient()
    return _u8_client_instance


# ===================== 检查环境变量是否配置 =====================
def check_u8_openapi_requirements() -> bool:
    """检查U8环境变量是否配置"""
    required_vars = [
        "U8_OPENAPI_APPKEY", 
        "U8_OPENAPI_APPSECRET", 
        "U8_OPENAPI_FROM_ACCOUNT", 
        "U8_OPENAPI_TO_ACCOUNT"
    ]
    return all(os.getenv(var) for var in required_vars)




# ===================== 工具注册 =====================
from tools.registry import registry

# ===================== 获取单个客户信息 工具注册 =====================
# u8_customer_get
registry.register(
    name="u8_customer_get",
    toolset="u8",
    schema=U8_CUSTOMER_GET_SCHEMA,
    handler=lambda args, **kw: u8_customer_get_tool(
        input_data=GetCustomerInfoInput(id=args.get("id", "")),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 添加一个新客户 工具注册 =====================
# u8_customer_add
registry.register(
    name="u8_customer_add",
    toolset="u8",
    schema=U8_CUSTOMER_ADD_SCHEMA,
    handler=lambda args, **kw: u8_customer_add_tool(
        input_data=AddCustomerInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)









# ===================== 新增一张收款单 工具注册 =====================
# u8_accept_add
registry.register(
    name="u8_accept_add",
    toolset="u8",
    schema=U8_ACCEPT_ADD_SCHEMA,
    handler=lambda args, **kw: u8_accept_add_tool(
        input_data=AddAcceptInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取单张收款单 工具注册 =====================
# u8_accept_get
registry.register(
    name="u8_accept_get",
    toolset="u8",
    schema=U8_ACCEPT_GET_SCHEMA,
    handler=lambda args, **kw: u8_accept_get_tool(
        input_data=GetAcceptInfoInput(id=args.get("id", "")),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取收款单列表信息 工具注册 =====================
# u8_accept_list_get
registry.register(
    name="u8_accept_list_get",
    toolset="u8",
    schema=U8_ACCEPT_LIST_GET_SCHEMA,
    handler=lambda args, **kw: u8_accept_list_get_tool(
        input_data=GetAcceptListInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 审批一张收款单 工具注册 =====================
# u8_accept_verify
registry.register(
    name="u8_accept_verify",
    toolset="u8",
    schema=U8_ACCEPT_VERIFY_SCHEMA,
    handler=lambda args, **kw: u8_accept_verify_tool(
        input_data=VerifyAcceptInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 弃审一张收款单 工具注册 =====================
# u8_accept_unverify
registry.register(
    name="u8_accept_unverify",
    toolset="u8",
    schema=U8_ACCEPT_UNVERIFY_SCHEMA,
    handler=lambda args, **kw: u8_accept_unverify_tool(
        input_data=UnVerifyAcceptInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)











# ===================== 新增一张付款单 工具注册 =====================
# u8_pay_add
registry.register(
    name="u8_pay_add",
    toolset="u8",
    schema=U8_PAY_ADD_SCHEMA,
    handler=lambda args, **kw: u8_pay_add_tool(
        input_data=AddPayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取单张付款单 工具注册 =====================
# u8_pay_get
registry.register(
    name="u8_pay_get",
    toolset="u8",
    schema=U8_PAY_GET_SCHEMA,
    handler=lambda args, **kw: u8_pay_get_tool(
        input_data=GetPayInfoInput(id=args.get("id", "")),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取付款单列表信息 工具注册 =====================
# u8_pay_list_get
registry.register(
    name="u8_pay_list_get",
    toolset="u8",
    schema=U8_PAY_LIST_GET_SCHEMA,
    handler=lambda args, **kw: u8_pay_list_get_tool(
        input_data=GetPayListInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 审批一张付款单 工具注册 =====================
# u8_pay_verify
registry.register(
    name="u8_pay_verify",
    toolset="u8",
    schema=U8_PAY_VERIFY_SCHEMA,
    handler=lambda args, **kw: u8_pay_verify_tool(
        input_data=VerifyPayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 弃审一张付款单 工具注册 =====================
# u8_pay_unverify
registry.register(
    name="u8_pay_unverify",
    toolset="u8",
    schema=U8_PAY_UNVERIFY_SCHEMA,
    handler=lambda args, **kw: u8_pay_unverify_tool(
        input_data=UnVerifyPayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)












# ===================== 新增一张应付单 工具注册 =====================
# u8_oughtpay_add
registry.register(
    name="u8_oughtpay_add",
    toolset="u8",
    schema=U8_OUGHTPAY_ADD_SCHEMA,
    handler=lambda args, **kw: u8_oughtpay_add_tool(
        input_data=AddOughtpayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取单张应付单 工具注册 =====================
# u8_oughtpay_get
registry.register(
    name="u8_oughtpay_get",
    toolset="u8",
    schema=U8_OUGHTPAY_GET_SCHEMA,
    handler=lambda args, **kw: u8_oughtpay_get_tool(
        input_data=GetOughtpayInfoInput(id=args.get("id", "")),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取应付单列表信息 工具注册 =====================
# u8_oughtpay_list_get
registry.register(
    name="u8_oughtpay_list_get",
    toolset="u8",
    schema=U8_OUGHTPAY_LIST_GET_SCHEMA,
    handler=lambda args, **kw: u8_oughtpay_list_get_tool(
        input_data=GetOughtpayListInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 审批一张应付单 工具注册 =====================
# u8_oughtpay_verify
registry.register(
    name="u8_oughtpay_verify",
    toolset="u8",
    schema=U8_OUGHTPAY_VERIFY_SCHEMA,
    handler=lambda args, **kw: u8_oughtpay_verify_tool(
        input_data=VerifyOughtpayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 弃审一张应付单 工具注册 =====================
# u8_oughtpay_unverify
registry.register(
    name="u8_oughtpay_unverify",
    toolset="u8",
    schema=U8_OUGHTPAY_UNVERIFY_SCHEMA,
    handler=lambda args, **kw: u8_oughtpay_unverify_tool(
        input_data=UnVerifyOughtpayInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)
















# ===================== 新增一张应收单 工具注册 =====================
# u8_oughtreceive_add
registry.register(
    name="u8_oughtreceive_add",
    toolset="u8",
    schema=U8_OUGHTRECEIVE_ADD_SCHEMA,
    handler=lambda args, **kw: u8_oughtreceive_add_tool(
        input_data=AddOughtreceiveInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取单张应收单 工具注册 =====================
# u8_oughtreceive_get
registry.register(
    name="u8_oughtreceive_get",
    toolset="u8",
    schema=U8_OUGHTRECEIVE_GET_SCHEMA,
    handler=lambda args, **kw: u8_oughtreceive_get_tool(
        input_data=GetOughtreceiveInfoInput(id=args.get("id", "")),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 获取应收单列表信息 工具注册 =====================
# u8_oughtreceive_list_get
registry.register(
    name="u8_oughtreceive_list_get",
    toolset="u8",
    schema=U8_OUGHTRECEIVE_LIST_GET_SCHEMA,
    handler=lambda args, **kw: u8_oughtreceive_list_get_tool(
        input_data=GetOughtreceiveListInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 审批一张应收单 工具注册 =====================
# u8_oughtreceive_verify
registry.register(
    name="u8_oughtreceive_verify",
    toolset="u8",
    schema=U8_OUGHTRECEIVE_VERIFY_SCHEMA,
    handler=lambda args, **kw: u8_oughtreceive_verify_tool(
        input_data=VerifyOughtreceiveInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)

# ===================== 弃审一张应收单 工具注册 =====================
# u8_oughtreceive_unverify
registry.register(
    name="u8_oughtreceive_unverify",
    toolset="u8",
    schema=U8_OUGHTRECEIVE_UNVERIFY_SCHEMA,
    handler=lambda args, **kw: u8_oughtreceive_unverify_tool(
        input_data=UnVerifyOughtreceiveInfoInput(**args),
        client=get_u8_client()  # 使用单例客户端
    ),
    check_fn=check_u8_openapi_requirements,
    requires_env=["U8_OPENAPI_APPKEY", "U8_OPENAPI_APPSECRET", "U8_OPENAPI_FROM_ACCOUNT", "U8_OPENAPI_TO_ACCOUNT"],
)





