# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# import requests
import json


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def surveyStart(request):
    return render(request, 'main_app/surveyStart.html')

def appointmentList(request):
    return render(request, 'main_app/appointmentList.html')

def appointments(request):
    return render(request, 'main_app/appointments.html')

def paymentOptions(request):
    return render(request, 'main_app/paymentOptions.html')

def pricingPreview(request):
    return render(request, 'main_app/pricingPreview.html')

def schedule(request):
    return render(request, 'main_app/schedule.html')



def live_chat(request):
    from opentok import OpenTok, MediaModes

    ##opentok = OpenTok(46070162, 3698c903b6f6dfdb18818edb617da0bd358bf1bd)
    ##### Create a session that attempts to send streams directly between clients (falling back
    # to use the OpenTok TURN server to relay streams if the clients cannot connect):
    ##session = opentok.create_session()

    from opentok import MediaModes
    # # A session that uses the OpenTok Media Router, which is required for archiving:
    # session = opentok.create_session(media_mode=MediaModes.routed)

    # # An automatically archived session:
    # session = opentok.create_session(media_mode=MediaModes.routed, archive_mode=ArchiveModes.always)

    # # A session with a location hint
    # session = opentok.create_session(location=u'12.34.56.78')

    # Store this session ID in the database
    ##session_id = session.session_id    


    ##### Generate a Token from just a session_id (fetched from a database)
    ##token = opentok.generate_token(session_id)
    # Generate a Token by calling the method on the Session (returned from create_session)
    # token = session.generate_token()

    from opentok import Roles
    # Set some options in a token
    # token = session.generate_token(role=Roles.moderator,
    #                             expire_time=int(time.time()) + 10,
    #                             data=u'name=Mark'
    #                             initial_layout_class_list=[u'focus'])
    
    return render(request, 'main_app/live-chat.html')
