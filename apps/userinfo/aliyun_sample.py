from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

from django.conf import settings


class Sample:

    def __init__(self):
        config = open_api_models.Config(
            access_key_id=settings.ALIYUN_ACCESSKEY_ID,
            access_key_secret=settings.ALIYUN_ACCESSKEY_SECERT,
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = 'dysmsapi.aliyuncs.com'
        self.client = Dysmsapi20170525Client(config)
    
    def send_sms(self, telephone):
        _request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=telephone,
            sign_name=settings.ALIYUN_SAMPLE_SIGNNAME
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            self.client.send_sms_with_options(_request, util_models.RuntimeOptions())
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)



aliyun_sample = Sample()


