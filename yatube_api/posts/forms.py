from django import forms


class FollowForm(forms.ModelForm):
    """
    Форма для админки подписок.
    Переопределён метод Clean для предотвращения самоподписок.
    """

    def clean(self):
        user = self.cleaned_data.get('user')
        following = self.cleaned_data.get('following')
        if user == following:
            raise forms.ValidationError(
                {'following': "Self-following is prohibit"}
            )
