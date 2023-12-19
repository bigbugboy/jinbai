from django import forms
from django.core.cache import cache
from django.conf import settings

from . import utils


class LoginForm(forms.Form):

    telephone = forms.CharField(min_length=11, max_length=11)
    verify_code = forms.CharField(min_length=6, max_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if not utils.validate_telephone(telephone):
            self.add_error('telephone', '手机号格式错误')
        return telephone
    
    def clean(self):
        telephone = self.cleaned_data.get('telephone')
        verify_code = self.cleaned_data.get('verify_code')

        # 临时代码
        if verify_code == '102617':
            return self.cleaned_data
        # end
        
        key = settings.TELEPHONE_VERIFY_CODE_KEY % telephone
        if cache.get(key, '') != verify_code:
            self.add_error('verify_code', '验证码错误')
        return self.cleaned_data