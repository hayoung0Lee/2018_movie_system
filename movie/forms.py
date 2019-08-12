from django import forms

from .models import Seat, Theater, Movie, ScrnClass
from ticket.models import ScrnSchd
import datetime

#https://stackoverflow.com/questions/5747188/django-form-multiple-choice

#https://stackoverflow.com/questions/5747188/django-form-multiple-choice/5747533

class PostForm(forms.ModelForm):
    # OPTIONS = (
    #         ("a", "A"),
    #         ("b", "B"),
    #         )
    #OPTIONS = Theater.objects.all()
    # rqs = Theater.objects.raw('Select * from Theater')
    # tuples = tuple((o.theater_no, o.theater_name) for o in rqs)
    OPTIONS_A = (
    ('A1','A1'),('A2','A2'),('A3','A3'),('A4','A4'),('A5','A5'),('A6','A6'),('A7','A7'),('A8','A8'),('A9','A9')
    )

    OPTIONS_B = (
    ('B1','B1'),('B2','B2'),('B3','B3'),('B4','B4'),('B5','B5'),('B6','B6'),('B7','B7'),('B8','B8'),('B9','B9')
    )

    OPTIONS_C = (
    ('C1','C1'),('C2','C2'),('C3','C3'),('C4','C4'),('C5','C5'),('C6','C6'),('C7','C7'),('C8','C8'),('C9','C9')
    )

    OPTIONS_D = (
    ('D1','D1'),('D2','D2'),('D3','D3'),('D4','D4'),('D5','D5'),('D6','D6'),('D7','D7'),('D8','D8'),('D9','D9')
    )

    OPTIONS_E = (
    ('E1','E1'),('E2','E2'),('E3','E3'),('E4','E4'),('E5','E5'),('E6','E6'),('E7','E7'),('E8','E8'),('E9','E9')
    )

    OPTIONS_F = (
    ('F1','F1'),('F2','F2'),('F3','F3'),('F4','F4'),('F5','F5'),('F6','F6'),('F7','F7'),('F8','F8'),('F9','F9')
    )

    OPTIONS_G = (
    ('G1','G1'),('G2','G2'),('G3','G3'),('G4','G4'),('G5','G5'),('G6','G6'),('G7','G7'),('G8','G8'),('G9','G9')
    )

    name_A = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_A)

    name_B = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_B)

    name_C = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_C)

    name_D = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_D)

    name_E = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_E)

    name_F = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_F)

    name_G = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS_G)


    class Meta:
        model = Seat
        fields = ('theater_no',)


class DeleteForm(forms.ModelForm):

    class Meta:
        model = Seat
        fields = ('theater_no',)


class MovieSchdForm(forms.ModelForm):
    time = ['06:00:00', '06:30:00','07:00:00','07:30:00','08:00:00', '08:30:00', '09:00:00', '09:30:00','10:00:00','10:30:00','11:00:00','11:30:00','12:00:00','12:30:00','13:00:00']
    time += ['13:30:00', '14:00:00','14:30:00','15:00:00','15:30:00','16:00:00','16:30:00','17:00:00','17:30:00','18:00:00','18:30:00','19:00:00','19:30:00','20:00:00','20:30:00', '21:00:00', '21:30:00']
    time += ['22:00:00','22:30:00','23:00:00','23:30:00','00:00:00','00:30:00','01:00:00','01:30:00','02:00:00','02:30:00' ]

    Movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())

    rqs = Theater.objects.raw('Select distinct Theater.theater_no, Theater.theater_name from Theater,Seat where Theater.theater_no = Seat.theater_no')
    options = tuple((o.theater_no,o.theater_name) for o in rqs)
    Theaters = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=options)

    #Theaters = forms.ModelMultipleChoiceField(queryset=Theater.objects.all())
    # start_time = forms.MultipleChoiceField(choices=time) #hhmm(24시간)
    # end_time = forms.MultipleChoiceField(choices=time) #hhmm(24시간)
    #promotion_type = forms.ChoiceField(label="Promotion Type", choices=time)

    class Meta:
        model = Movie
        fields = ('Movies','Theaters')


# 날짜를 입력하여 그날의 상영관 현황을 볼수 있도록 하는 폼
class SchdSearchForm(forms.ModelForm):
    wanted_scrn_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = ScrnSchd
        fields = ('wanted_scrn_date',)


