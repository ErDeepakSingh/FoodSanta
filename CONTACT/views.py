from django.shortcuts import (render,
                              redirect)

from . import forms as contact_forms
from . import models as contact_models


def contact_us(request):
    form=contact_forms.Contact_Form()
    if request.method=='POST':
        form=contact_forms.Contact_Form(data=request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            mobile=form.cleaned_data.get('mobile_no')
            email=form.cleaned_data.get('email')
            message=form.cleaned_data.get('message')
            contact=contact_models.Contact_Post(
                name=name,
                mobile_no=mobile,
                email=email,
                message=message,
                author=request.user
            )
            contact.save()
            return redirect('food_santa_home')

    return render(request,'contact/contact.html',{'form':form})