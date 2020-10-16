from django import forms
from catalog.choices import *
from django.forms.widgets import TextInput
from django.forms import ModelForm, ModelChoiceField
from catalog.models import Rd1ScoreModel, Rd1SlotModel, PlayerModel, SportsTippingModel, Rd2ScoreModel, Rd2SlotModel, Rd3ScoreModel, Rd3SlotModel, Rd4ScoreModel, Rd4SlotModel, AdminHoleDetails, MatchReportInput, TeamsRoundModel

class MyTelephoneInput(TextInput):
        input_type = 'tel'

class Rd1ScoreForm(ModelForm):
    ctp = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    ld = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    slot1_score = forms.IntegerField(label='', required=False)
    slot2_score = forms.IntegerField(label='', required=False)
    slot3_score = forms.IntegerField(label='', required=False)
    slot4_score = forms.IntegerField(label='', required=False)
    slot5_score = forms.IntegerField(label='', required=False)
    slot6_score = forms.IntegerField(label='', required=False)
    slot7_score = forms.IntegerField(label='', required=False)
    slot8_score = forms.IntegerField(label='', required=False)
    slot9_score = forms.IntegerField(label='', required=False)
    slot10_score = forms.IntegerField(label='', required=False)
    slot11_score = forms.IntegerField(label='', required=False)
    slot12_score = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(Rd1ScoreForm, self).__init__(*args, **kwargs)
        self.fields['slot1_score'].widget=MyTelephoneInput(attrs={'id': 'player1', 'class':'scoreInputField'})
        self.fields['slot2_score'].widget=MyTelephoneInput(attrs={'id': 'player2', 'class':'scoreInputField'})
        self.fields['slot3_score'].widget=MyTelephoneInput(attrs={'id': 'player3', 'class':'scoreInputField'})
        self.fields['slot4_score'].widget=MyTelephoneInput(attrs={'id': 'player4', 'class':'scoreInputField'})
        self.fields['slot5_score'].widget=MyTelephoneInput(attrs={'id': 'player5', 'class':'scoreInputField'})
        self.fields['slot6_score'].widget=MyTelephoneInput(attrs={'id': 'player6', 'class':'scoreInputField'})
        self.fields['slot7_score'].widget=MyTelephoneInput(attrs={'id': 'player7', 'class':'scoreInputField'})
        self.fields['slot8_score'].widget=MyTelephoneInput(attrs={'id': 'player8', 'class':'scoreInputField'})
        self.fields['slot9_score'].widget=MyTelephoneInput(attrs={'id': 'player9', 'class':'scoreInputField'})
        self.fields['slot10_score'].widget=MyTelephoneInput(attrs={'id': 'player10', 'class':'scoreInputField'})
        self.fields['slot11_score'].widget=MyTelephoneInput(attrs={'id': 'player11', 'class':'scoreInputField'})
        self.fields['slot12_score'].widget=MyTelephoneInput(attrs={'id': 'player12', 'class':'scoreInputField'})


    class Meta:
        model = Rd1ScoreModel
        fields = ('ctp', 'ld', 'slot1_score', 'slot2_score', 'slot3_score','slot4_score', 'slot5_score', 'slot6_score', 'slot7_score', 'slot8_score', 'slot9_score', 'slot10_score', 'slot11_score', 'slot12_score',)

class Rd2ScoreForm(ModelForm):
    ctp = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    ld = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    slot1_score = forms.IntegerField(label='', required=False)
    slot2_score = forms.IntegerField(label='', required=False)
    slot3_score = forms.IntegerField(label='', required=False)
    slot4_score = forms.IntegerField(label='', required=False)
    slot5_score = forms.IntegerField(label='', required=False)
    slot6_score = forms.IntegerField(label='', required=False)
    slot7_score = forms.IntegerField(label='', required=False)
    slot8_score = forms.IntegerField(label='', required=False)
    slot9_score = forms.IntegerField(label='', required=False)
    slot10_score = forms.IntegerField(label='', required=False)
    slot11_score = forms.IntegerField(label='', required=False)
    slot12_score = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(Rd2ScoreForm, self).__init__(*args, **kwargs)
        self.fields['slot1_score'].widget=MyTelephoneInput(attrs={'id': 'player1', 'class':'scoreInputField'})
        self.fields['slot2_score'].widget=MyTelephoneInput(attrs={'id': 'player2', 'class':'scoreInputField'})
        self.fields['slot3_score'].widget=MyTelephoneInput(attrs={'id': 'player3', 'class':'scoreInputField'})
        self.fields['slot4_score'].widget=MyTelephoneInput(attrs={'id': 'player4', 'class':'scoreInputField'})
        self.fields['slot5_score'].widget=MyTelephoneInput(attrs={'id': 'player5', 'class':'scoreInputField'})
        self.fields['slot6_score'].widget=MyTelephoneInput(attrs={'id': 'player6', 'class':'scoreInputField'})
        self.fields['slot7_score'].widget=MyTelephoneInput(attrs={'id': 'player7', 'class':'scoreInputField'})
        self.fields['slot8_score'].widget=MyTelephoneInput(attrs={'id': 'player8', 'class':'scoreInputField'})
        self.fields['slot9_score'].widget=MyTelephoneInput(attrs={'id': 'player9', 'class':'scoreInputField'})
        self.fields['slot10_score'].widget=MyTelephoneInput(attrs={'id': 'player10', 'class':'scoreInputField'})
        self.fields['slot11_score'].widget=MyTelephoneInput(attrs={'id': 'player11', 'class':'scoreInputField'})
        self.fields['slot12_score'].widget=MyTelephoneInput(attrs={'id': 'player12', 'class':'scoreInputField'})


    class Meta:
        model = Rd2ScoreModel
        fields = ('ctp', 'ld', 'slot1_score', 'slot2_score', 'slot3_score','slot4_score', 'slot5_score', 'slot6_score', 'slot7_score', 'slot8_score', 'slot9_score', 'slot10_score', 'slot11_score', 'slot12_score',)

class Rd3ScoreForm(ModelForm):
    ctp = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    ld = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    slot1_score = forms.IntegerField(label='', required=False)
    slot2_score = forms.IntegerField(label='', required=False)
    slot3_score = forms.IntegerField(label='', required=False)
    slot4_score = forms.IntegerField(label='', required=False)
    slot5_score = forms.IntegerField(label='', required=False)
    slot6_score = forms.IntegerField(label='', required=False)
    slot7_score = forms.IntegerField(label='', required=False)
    slot8_score = forms.IntegerField(label='', required=False)
    slot9_score = forms.IntegerField(label='', required=False)
    slot10_score = forms.IntegerField(label='', required=False)
    slot11_score = forms.IntegerField(label='', required=False)
    slot12_score = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(Rd3ScoreForm, self).__init__(*args, **kwargs)
        self.fields['slot1_score'].widget=MyTelephoneInput(attrs={'id': 'player1', 'class':'scoreInputField'})
        self.fields['slot2_score'].widget=MyTelephoneInput(attrs={'id': 'player2', 'class':'scoreInputField'})
        self.fields['slot3_score'].widget=MyTelephoneInput(attrs={'id': 'player3', 'class':'scoreInputField'})
        self.fields['slot4_score'].widget=MyTelephoneInput(attrs={'id': 'player4', 'class':'scoreInputField'})
        self.fields['slot5_score'].widget=MyTelephoneInput(attrs={'id': 'player5', 'class':'scoreInputField'})
        self.fields['slot6_score'].widget=MyTelephoneInput(attrs={'id': 'player6', 'class':'scoreInputField'})
        self.fields['slot7_score'].widget=MyTelephoneInput(attrs={'id': 'player7', 'class':'scoreInputField'})
        self.fields['slot8_score'].widget=MyTelephoneInput(attrs={'id': 'player8', 'class':'scoreInputField'})
        self.fields['slot9_score'].widget=MyTelephoneInput(attrs={'id': 'player9', 'class':'scoreInputField'})
        self.fields['slot10_score'].widget=MyTelephoneInput(attrs={'id': 'player10', 'class':'scoreInputField'})
        self.fields['slot11_score'].widget=MyTelephoneInput(attrs={'id': 'player11', 'class':'scoreInputField'})
        self.fields['slot12_score'].widget=MyTelephoneInput(attrs={'id': 'player12', 'class':'scoreInputField'})


    class Meta:
        model = Rd3ScoreModel
        fields = ('ctp', 'ld', 'slot1_score', 'slot2_score', 'slot3_score','slot4_score', 'slot5_score', 'slot6_score', 'slot7_score', 'slot8_score', 'slot9_score', 'slot10_score', 'slot11_score', 'slot12_score',)

class Rd4ScoreForm(ModelForm):
    ctp = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    ld = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select winner', required=False)
    slot1_score = forms.IntegerField(label='', required=False)
    slot2_score = forms.IntegerField(label='', required=False)
    slot3_score = forms.IntegerField(label='', required=False)
    slot4_score = forms.IntegerField(label='', required=False)
    slot5_score = forms.IntegerField(label='', required=False)
    slot6_score = forms.IntegerField(label='', required=False)
    slot7_score = forms.IntegerField(label='', required=False)
    slot8_score = forms.IntegerField(label='', required=False)
    slot9_score = forms.IntegerField(label='', required=False)
    slot10_score = forms.IntegerField(label='', required=False)
    slot11_score = forms.IntegerField(label='', required=False)
    slot12_score = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(Rd4ScoreForm, self).__init__(*args, **kwargs)
        self.fields['slot1_score'].widget=MyTelephoneInput(attrs={'id': 'player1', 'class':'scoreInputField'})
        self.fields['slot2_score'].widget=MyTelephoneInput(attrs={'id': 'player2', 'class':'scoreInputField'})
        self.fields['slot3_score'].widget=MyTelephoneInput(attrs={'id': 'player3', 'class':'scoreInputField'})
        self.fields['slot4_score'].widget=MyTelephoneInput(attrs={'id': 'player4', 'class':'scoreInputField'})
        self.fields['slot5_score'].widget=MyTelephoneInput(attrs={'id': 'player5', 'class':'scoreInputField'})
        self.fields['slot6_score'].widget=MyTelephoneInput(attrs={'id': 'player6', 'class':'scoreInputField'})
        self.fields['slot7_score'].widget=MyTelephoneInput(attrs={'id': 'player7', 'class':'scoreInputField'})
        self.fields['slot8_score'].widget=MyTelephoneInput(attrs={'id': 'player8', 'class':'scoreInputField'})
        self.fields['slot9_score'].widget=MyTelephoneInput(attrs={'id': 'player9', 'class':'scoreInputField'})
        self.fields['slot10_score'].widget=MyTelephoneInput(attrs={'id': 'player10', 'class':'scoreInputField'})
        self.fields['slot11_score'].widget=MyTelephoneInput(attrs={'id': 'player11', 'class':'scoreInputField'})
        self.fields['slot12_score'].widget=MyTelephoneInput(attrs={'id': 'player12', 'class':'scoreInputField'})

    class Meta:
        model = Rd4ScoreModel
        fields = ('ctp', 'ld', 'slot1_score', 'slot2_score', 'slot3_score','slot4_score', 'slot5_score', 'slot6_score', 'slot7_score', 'slot8_score', 'slot9_score', 'slot10_score', 'slot11_score', 'slot12_score',)

class TeamsRoundForm(ModelForm):
    #group 1
    team_name1 = forms.CharField(required=False)
    holes1 = forms.IntegerField(required=False)
    score1 = forms.IntegerField(required=False)
    #group 2
    team_name2 = forms.CharField(required=False)
    holes2 = forms.IntegerField(required=False)
    score2 = forms.IntegerField(required=False)
    #group 3
    team_name3 = forms.CharField(required=False)
    holes3 = forms.IntegerField(required=False)
    score3 = forms.IntegerField(required=False)
    #group 4
    team_name4 = forms.CharField(required=False)
    holes4 = forms.IntegerField(required=False)
    score4 = forms.IntegerField(required=False)

    class Meta:
        model = TeamsRoundModel
        fields = ('team_name1', 'holes1', 'score1', 'team_name2', 'holes2', 'score2','team_name3', 'holes3', 'score3','team_name4', 'holes4', 'score4',)

class SportsTippingForm(ModelForm):
        name = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Player name', required=True)
        password = forms.CharField(widget=forms.PasswordInput, label='', required=False)
        game1 = forms.ChoiceField(choices=GAME_1, required=True)
        game2 = forms.ChoiceField(choices=GAME_2, required=True)
        game3 = forms.ChoiceField(choices=GAME_3, required=True)
        game4 = forms.ChoiceField(choices=GAME_4, required=True)
        game5 = forms.ChoiceField(choices=GAME_5, required=True)
        game6 = forms.ChoiceField(choices=GAME_6, required=True)
        game7 = forms.ChoiceField(choices=GAME_7, required=True)
        game8 = forms.ChoiceField(choices=GAME_8, required=True)
        game9 = forms.ChoiceField(choices=GAME_9, required=True)
        game10 = forms.ChoiceField(choices=GAME_10, required=True)

        class Meta:
                model = SportsTippingModel
                fields = ('name', 'password', 'game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9', 'game10',)

# DEFINE USERMODELCHOICEFIELD TO CALL CHOICES FROM OTHER MODELS
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.roundNum

class ReportInputChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.report_name

class MatchReportForm(forms.Form):
    report_round = UserModelChoiceField(queryset=AdminHoleDetails.objects.all(), empty_label='--', required=True)
    player_input = ReportInputChoiceField(queryset=MatchReportInput.objects.all(), empty_label='Auto-generate', required=False)

    def round_select(self,request):
        roundSelect = self.cleaned_data['report_round']
        return roundSelect

    def player_select(self,request):
        playerSelect = self.cleaned_data['player_input']
        return playerSelect

class PollyVoiceForm(forms.Form):
    polly_name = forms.ChoiceField(choices=VOICE_CHOICES, required=True)
    polly_code = forms.CharField(max_length=4, required=True)

    def voice_select(self,request):
        voiceSelect = self.cleaned_data['polly_name']
        return voiceSelect

    def code_validate(self,request):
        codeValue = self.cleaned_data['polly_code']
        return codeValue

class MatchReportsInputForm(ModelForm):
    report_name = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), label='', empty_label='Select your name', required=True)
    adjective1 = forms.CharField(label='', required=True)
    adjective2 = forms.CharField(label='', required=True)
    old_saying = forms.CharField(label='', required=True)
    animals = forms.CharField(label='', required=True)
    fav_drink = forms.CharField(label='', required=True)
    sports_expression = forms.CharField(label='', required=True)
    golf_saying = forms.CharField(label='', required=True)
    lyric = forms.CharField(label='', required=True)
    group_noone_likes = forms.CharField(label='', required=True)
    recent_news = forms.CharField(label='', required=True)
    jobs = forms.CharField(label='', required=True)
    office_perk = forms.CharField(label='', required=True)

    class Meta:
        model = MatchReportInput
        fields = ('report_name', 'adjective1', 'adjective2', 'old_saying', 'animals', 'fav_drink', 'sports_expression', 'golf_saying', 'lyric', 'group_noone_likes', 'recent_news', 'jobs', 'office_perk',)


# class FridaySocialForm(ModelForm):
#         name = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Your name', required=True)
#         password = forms.CharField(widget=forms.PasswordInput, label='')
#         best = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Best on ground', required=True)
#         honorable = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Honorable mention', required=False)
# #        prefix = 'friday'
#
#         class Meta:
#                 model=FridaySocialModel
#                 fields = ('name', 'password', 'best', 'honorable',)
#
# class SaturdaySocialForm(ModelForm):
#         name = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Your name', required=True)
#         password = forms.CharField(widget=forms.PasswordInput, label='')
#         best = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Best on ground', required=True)
#         honorable = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Honorable mention', required=False)
# #        prefix = 'saturday'
#
#         class Meta:
#                 model=SaturdaySocialModel
#                 fields = ('name', 'password', 'best', 'honorable',)
