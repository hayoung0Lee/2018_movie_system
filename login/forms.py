from django.forms import ModelForm
from .models import Feedback
#views와 templates에서 forms를 사용허겠다
class login_form(ModelForm):# ModelForm은 위에서 받아온거
    class Meta:
        model = Customer #Meta에  models.Customer 사용하겠다
        fields = [' customer_id', 'customer_name','dob','contact', 'pwd', 'member_check', 'email']#Customer의 각 컬럼들
        #입력받을값
