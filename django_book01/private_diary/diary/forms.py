import os

from django import forms
from django.core.mail import EmailMessage


class InquiryForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.EmailField(label="mail address")
    title = forms.CharField(label="title", max_length=30)
    message = forms.CharField(label="message", widget=forms.Textarea)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholader"] = "Input name here"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Input mail address here"

        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["title"].widget.attrs["placeholder"] = "Input title here"

        self.fields["message"].widget.attrs["class"] = "form-control"
        self.fields["message"].widget.attrs["placeholder"] = "Input message here"

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        title = self.cleaned_data["title"]
        message = self.cleaned_data["message"]

        subject = f"Inquiry {title}"
        message = f"Sender: {name}\nmail address: {email}\nmessage:\n{message}"
        from_email = os.environ.get("FROM_EMAIL")
        to_list = [os.environ.get("FROM_EMAIL")]
        cc_list = [email]

        message = EmailMessage(
            subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list
        )
        message.send()
