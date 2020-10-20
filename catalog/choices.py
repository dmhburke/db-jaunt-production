from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

#CHOICES
YES_NO = (
    ("YES", "Yes"),
    ("NO", "No"),
    )

EVENT_CATEGORY = (
    ("Round1Golf", "Round1Golf"),
    ("Round1CTPLD", "Round1CTPLD"),
    ("Round1_Bonus", "Round1_Bonus"),
    ("Round2Golf", "Round2Golf"),
    ("Round2CTPLD", "Round2CTPLD"),
    ("Round2_Bonus", "Round2_Bonus"),
    ("Round3Golf", "Round3Golf"),
    ("Round3CTPLD", "Round3CTPLD"),
    ("Round3_Bonus", "Round3_Bonus"),
    ("Social", "Social"),
    ("Best_dressed", "Best_dressed"),
    ("Tipping", "Tipping"),
)

DAYS = (
    ("FRIDAY", "Friday"),
    ("SATURDAY", "Saturday"),
    ("SUNDAY", "Sunday"),
    )

#TIPPING_SETUP
GAME_1 = (
    ("", "Select result"),
    ("CHENNAI", "Chennai"),
    ("MUMBAI", "Mumbai"),
    ("TIE", "Tie"),
    )

GAME_2 = (
    ("", "Select result"),
    ("BARCELONA", "Barcelona"),
    ("REAL_MADRID", "Real Madrid"),
    ("DRAW", "Draw"),
    )

GAME_3 = (
    ("", "Select result"),
    ("RAYS", "Rays"),
    ("DODGERS", "Dodgers"),
    )

GAME_4 = (
    ("", "Select result"),
    ("AUBURN", "Auburn"),
    ("OLE_MISS", "Ole Miss"),
    )

GAME_5 = (
    ("", "Select result"),
    ("MICHIGAN", "Michigan"),
    ("MINNESOTA", "Minnesota"),
    )

GAME_6 = (
    ("", "Select result"),
    ("IOWA_STATE", "Iowa State"),
    ("OKLAHOMA_STATE", "Oklahoma State"),
    )

GAME_7 = (
    ("", "Select result"),
    ("MAN_UNITED", "Man United"),
    ("CHELSEA", "Chelsea"),
    ("DRAW", "Draw"),
    )

GAME_8 = (
    ("", "Select result"),
    ("FRANCE", "France"),
    ("WALES", "Wales"),
    ("TIE", "Tie"),
    )

GAME_9 = (
    ("", "Select result"),
    ("DODGERS", "Dodgers"),
    ("RAYS", "Rays"),
    )

GAME_10 = (
    ("", "Select result"),
    ("PANTHERS", "Panthers"),
    ("STORM", "Storm"),
    )

#RESULTS CHECK - change empty result value
GAME_1R = (
    ("NOT_COMPLETE", "No result"),
    ("CHENNAI", "Chennai"),
    ("MUMBAI", "Mumbai"),
    ("TIE", "Tie"),
    )

GAME_2R = (
    ("NOT_COMPLETE", "No result"),
    ("BARCELONA", "Barcelona"),
    ("REAL_MADRID", "Real Madrid"),
    ("DRAW", "Draw"),
    )

GAME_3R = (
    ("NOT_COMPLETE", "No result"),
    ("RAYS", "Rays"),
    ("DODGERS", "Dodgers"),
    )

GAME_4R = (
    ("NOT_COMPLETE", "No result"),
    ("AUBURN", "Auburn"),
    ("OLE_MISS", "Ole Miss"),
    )

GAME_5R = (
    ("NOT_COMPLETE", "No result"),
    ("MICHIGAN", "Michigan"),
    ("MINNESOTA", "Minnesota"),
    )

GAME_6R = (
    ("NOT_COMPLETE", "No result"),
    ("IOWA_STATE", "Iowa State"),
    ("OKLAHOMA_STATE", "Oklahoma State"),
    )

GAME_7R = (
    ("NOT_COMPLETE", "No result"),
    ("MAN_UNITED", "Man United"),
    ("CHELSEA", "Chelsea"),
    ("DRAW", "Draw"),
    )

GAME_8R = (
    ("NOT_COMPLETE", "No result"),
    ("FRANCE", "France"),
    ("WALES", "Wales"),
    ("TIE", "Tie"),
    )

GAME_9R = (
    ("NOT_COMPLETE", "No result"),
    ("DODGERS", "Dodgers"),
    ("RAYS", "Rays"),
    )

GAME_10R = (
    ("NOT_COMPLETE", "No result"),
    ("PANTHERS", "Panthers"),
    ("STORM", "Storm"),
    )

VOICE_CHOICES = (
    ('Amy', 'Amy (UK)'),
    ('Emma', 'Emma (UK)'),
    ('Brian', 'Brian (UK)'),
    ('Joey', 'Joey (US)'),
    ('Kendra', 'Kendra (US)'),
    # ('Nicole', 'Nicole (Aussie)'),
    # ('Russell', 'Russell (Aussie)'),
    # ('Geraint', 'Geraint (Welsh)'),
    # ('Mathieu', 'Mathieu (French)'),
    # ('Karl', 'Karl (Icelandic)'),
    # ('Liv', 'Liv (Norwegian)'),
    # ('Astrid', 'Astrid (Swedish)'),
    # ('Miguel', 'Miguel (Mexican)'),
    )
