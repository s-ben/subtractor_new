from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
    docfile2 = forms.FileField(
        label='Select a file'
    )
# 	recording_file = forms.FileField()
# 	music_file = forms.FileField()