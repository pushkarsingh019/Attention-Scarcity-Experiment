﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on Mon Oct 14 13:36:50 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.2.2')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from load_variables
# variables for positioning throughout the expeirment
import numpy as np
import base64

height = 150
width = 150
left_position = -400
right_position = 400
center_position = 0
bottom_position = -150
top_position = 200
below_position = -240
letter_height = 36
triangle_width = 150
triangle_height = 170
distractor_y = -50
# Run 'Before Experiment' code from code
triangle = "stimulus/triangle.png"
square = "stimulus/square.png"
noTrialArousal = "distractor abscent"
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'preliminary_experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/pushkarsingh/Documents/01 University/10 Stuti/GroupA_final_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    text_norm = visual.TextStim(win=win, name='text_norm',
        text="Welcome to the experiment.\n\npress 'spacebar' to continue.",
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_instruct = keyboard.Keyboard()
    # Run 'Begin Experiment' code from text_align
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm.alignText= 'left'
    
    # --- Initialize components for Routine "self_other_instruction" ---
    text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
        text="In this study, you will be shown two shapes (square and triangle) with two labels (you and stranger). You have to memorize this association. \n\n- You are represented by a Sqaure (You-Square)\n- There is a Stranger (an unknown person to you), who is represented by Triangle (Stranger-triangle)\n\nTake a few minutes to memorize this association. Let me know when you have memorized and ready to proceed to the experiment.\n\npress 'spacebar' to continue\n",
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_2 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from text_align_2
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm.alignText= 'left'
    
    # --- Initialize components for Routine "self_other_info" ---
    # Run 'Begin Experiment' code from info_shape_code
    triangle_path = "stimulus/triangle.png"
    square_path = "stimulus/square.png"
    
    # square = you, triangle =  stranger
    label_self = visual.TextStim(win=win, name='label_self',
        text='You',
        font='Open Sans',
        units='pix', pos=(right_position, bottom_position), height=letter_height, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    label_other = visual.TextStim(win=win, name='label_other',
        text='Stranger',
        font='Open Sans',
        units='pix', pos=(left_position, bottom_position), height=letter_height, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text = visual.TextStim(win=win, name='text',
        text="press 'spacebar' to contiue",
        font='Open Sans',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp = keyboard.Keyboard()
    square_image = visual.ImageStim(
        win=win,
        name='square_image', units='pix', 
        image=square_path, mask=None, anchor='center',
        ori=0.0, pos=(right_position, 0), size=(width, height),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    triangle_path = visual.ImageStim(
        win=win,
        name='triangle_path', units='pix', 
        image=triangle_path, mask=None, anchor='center',
        ori=0.0, pos=(left_position, 0), size=(triangle_width, triangle_height),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    
    # --- Initialize components for Routine "self_other_starting" ---
    text_norm_3 = visual.TextStim(win=win, name='text_norm_3',
        text='Your task is to judge whether the shape label pairing is correct or incorrect. If the shape label pairing is correct press the key which is labeled "correct" and if its incorrect press key labeled "Incorrect" on your keyboard.\n\npress \'spacebar\' to continue\n',
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_3 = keyboard.Keyboard()
    # Run 'Begin Experiment' code from text_align_3
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm.alignText= 'left'
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    label_text = ""
    shape_path= ""
    fixation = visual.ShapeStim(
        win=win, name='fixation', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=0.8,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    label = visual.TextStim(win=win, name='label',
        text='',
        font='Open Sans',
        units='pix', pos=(0, -150), height=letter_height, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_2 = keyboard.Keyboard()
    shape_1 = visual.ImageStim(
        win=win,
        name='shape_1', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, top_position), size=(width, height),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    
    # --- Initialize components for Routine "feedback" ---
    # Run 'Begin Experiment' code from code_2
    feedback_text = "miss"
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "thank_you" ---
    text_norm_7 = visual.TextStim(win=win, name='text_norm_7',
        text='Thank you for participating :))',
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_instruct.keys = []
    key_instruct.rt = []
    _key_instruct_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [text_norm, key_instruct]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm* updates
        
        # if text_norm is starting this frame...
        if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm.frameNStart = frameN  # exact frame index
            text_norm.tStart = t  # local t and not account for scr refresh
            text_norm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm.status = STARTED
            text_norm.setAutoDraw(True)
        
        # if text_norm is active this frame...
        if text_norm.status == STARTED:
            # update params
            pass
        
        # *key_instruct* updates
        waitOnFlip = False
        
        # if key_instruct is starting this frame...
        if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct.frameNStart = frameN  # exact frame index
            key_instruct.tStart = t  # local t and not account for scr refresh
            key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instruct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_allKeys.extend(theseKeys)
            if len(_key_instruct_allKeys):
                key_instruct.keys = _key_instruct_allKeys[-1].name  # just the last key pressed
                key_instruct.rt = _key_instruct_allKeys[-1].rt
                key_instruct.duration = _key_instruct_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "self_other_instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_instruct_2.keys = []
    key_instruct_2.rt = []
    _key_instruct_2_allKeys = []
    # keep track of which components have finished
    self_other_instructionComponents = [text_norm_2, key_instruct_2]
    for thisComponent in self_other_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "self_other_instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_2* updates
        
        # if text_norm_2 is starting this frame...
        if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_2.frameNStart = frameN  # exact frame index
            text_norm_2.tStart = t  # local t and not account for scr refresh
            text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_2.status = STARTED
            text_norm_2.setAutoDraw(True)
        
        # if text_norm_2 is active this frame...
        if text_norm_2.status == STARTED:
            # update params
            pass
        
        # *key_instruct_2* updates
        waitOnFlip = False
        
        # if key_instruct_2 is starting this frame...
        if key_instruct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct_2.frameNStart = frameN  # exact frame index
            key_instruct_2.tStart = t  # local t and not account for scr refresh
            key_instruct_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instruct_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct_2.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_2_allKeys.extend(theseKeys)
            if len(_key_instruct_2_allKeys):
                key_instruct_2.keys = _key_instruct_2_allKeys[-1].name  # just the last key pressed
                key_instruct_2.rt = _key_instruct_2_allKeys[-1].rt
                key_instruct_2.duration = _key_instruct_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in self_other_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "self_other_instruction" ---
    for thisComponent in self_other_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "self_other_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "self_other_info" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    self_other_infoComponents = [label_self, label_other, text, key_resp, square_image, triangle_path]
    for thisComponent in self_other_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "self_other_info" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *label_self* updates
        
        # if label_self is starting this frame...
        if label_self.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_self.frameNStart = frameN  # exact frame index
            label_self.tStart = t  # local t and not account for scr refresh
            label_self.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_self, 'tStartRefresh')  # time at next scr refresh
            # update status
            label_self.status = STARTED
            label_self.setAutoDraw(True)
        
        # if label_self is active this frame...
        if label_self.status == STARTED:
            # update params
            pass
        
        # *label_other* updates
        
        # if label_other is starting this frame...
        if label_other.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label_other.frameNStart = frameN  # exact frame index
            label_other.tStart = t  # local t and not account for scr refresh
            label_other.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label_other, 'tStartRefresh')  # time at next scr refresh
            # update status
            label_other.status = STARTED
            label_other.setAutoDraw(True)
        
        # if label_other is active this frame...
        if label_other.status == STARTED:
            # update params
            pass
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *square_image* updates
        
        # if square_image is starting this frame...
        if square_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square_image.frameNStart = frameN  # exact frame index
            square_image.tStart = t  # local t and not account for scr refresh
            square_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            square_image.status = STARTED
            square_image.setAutoDraw(True)
        
        # if square_image is active this frame...
        if square_image.status == STARTED:
            # update params
            pass
        
        # *triangle_path* updates
        
        # if triangle_path is starting this frame...
        if triangle_path.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            triangle_path.frameNStart = frameN  # exact frame index
            triangle_path.tStart = t  # local t and not account for scr refresh
            triangle_path.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(triangle_path, 'tStartRefresh')  # time at next scr refresh
            # update status
            triangle_path.status = STARTED
            triangle_path.setAutoDraw(True)
        
        # if triangle_path is active this frame...
        if triangle_path.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in self_other_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "self_other_info" ---
    for thisComponent in self_other_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "self_other_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "self_other_starting" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_instruct_3.keys = []
    key_instruct_3.rt = []
    _key_instruct_3_allKeys = []
    # keep track of which components have finished
    self_other_startingComponents = [text_norm_3, key_instruct_3]
    for thisComponent in self_other_startingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "self_other_starting" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_3* updates
        
        # if text_norm_3 is starting this frame...
        if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_3.frameNStart = frameN  # exact frame index
            text_norm_3.tStart = t  # local t and not account for scr refresh
            text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_3.status = STARTED
            text_norm_3.setAutoDraw(True)
        
        # if text_norm_3 is active this frame...
        if text_norm_3.status == STARTED:
            # update params
            pass
        
        # *key_instruct_3* updates
        waitOnFlip = False
        
        # if key_instruct_3 is starting this frame...
        if key_instruct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct_3.frameNStart = frameN  # exact frame index
            key_instruct_3.tStart = t  # local t and not account for scr refresh
            key_instruct_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_instruct_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct_3.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_3_allKeys.extend(theseKeys)
            if len(_key_instruct_3_allKeys):
                key_instruct_3.keys = _key_instruct_3_allKeys[-1].name  # just the last key pressed
                key_instruct_3.rt = _key_instruct_3_allKeys[-1].rt
                key_instruct_3.duration = _key_instruct_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in self_other_startingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "self_other_starting" ---
    for thisComponent in self_other_startingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "self_other_starting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        value = random()
        thisExp.addData("Arousal", "distractor absent")
        
        if value <= 1/4:
            label_text = "You"
            shape_path = triangle
            thisExp.addData("shape", "triangle")
            thisExp.addData("pair", "unmatch")
            thisExp.addData("Label", "You")
            c_resp = 'n'
        elif 1/4 < value <= 2/4:
            label_text = "You"
            shape_path = square
            thisExp.addData("shape", "square")
            thisExp.addData("pair", "match")
            thisExp.addData("Label", "You")
            c_resp = 'm'
        elif 2/4 < value <= 3/4:
            label_text = "Stranger"
            shape_path = triangle
            thisExp.addData("shape", "triangle")
            thisExp.addData("pair", "match")
            thisExp.addData("Label", "Stranger")
            c_resp = 'm'
        elif 3/4 < value <= 4/4:
            label_text = "Stranger"
            shape_path = square
            thisExp.addData("shape", "square")
            thisExp.addData("pair", "unmatch")
            thisExp.addData("Label", "Stranger")
            c_resp = 'n'
        else:
            print("we just broke math")
        label.setText(label_text)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        shape_1.setImage(shape_path)
        # keep track of which components have finished
        trialComponents = [fixation, label, key_resp_2, shape_1]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *label* updates
            
            # if label is starting this frame...
            if label.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                label.frameNStart = frameN  # exact frame index
                label.tStart = t  # local t and not account for scr refresh
                label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(label, 'tStartRefresh')  # time at next scr refresh
                # update status
                label.status = STARTED
                label.setAutoDraw(True)
            
            # if label is active this frame...
            if label.status == STARTED:
                # update params
                pass
            
            # if label is stopping this frame...
            if label.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > label.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    label.tStop = t  # not accounting for scr refresh
                    label.frameNStop = frameN  # exact frame index
                    # update status
                    label.status = FINISHED
                    label.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['n','m'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_2.keys == str(c_resp)) or (key_resp_2.keys == c_resp):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *shape_1* updates
            
            # if shape_1 is starting this frame...
            if shape_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                shape_1.frameNStart = frameN  # exact frame index
                shape_1.tStart = t  # local t and not account for scr refresh
                shape_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(shape_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                shape_1.status = STARTED
                shape_1.setAutoDraw(True)
            
            # if shape_1 is active this frame...
            if shape_1.status == STARTED:
                # update params
                pass
            
            # if shape_1 is stopping this frame...
            if shape_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > shape_1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    shape_1.tStop = t  # not accounting for scr refresh
                    shape_1.frameNStop = frameN  # exact frame index
                    # update status
                    shape_1.status = FINISHED
                    shape_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(c_resp).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        trials.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
            trials.addData('key_resp_2.duration', key_resp_2.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.500000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        #if key_resp_2.corr == 1:
        #    feedback_text = "correct"
        #else:
        #    feedback_text = "incorrect"
        
        # main logic for feedback
        if(key_resp_2.keys == "m"):
            if (c_resp == "m"):
                feedback_text = "correct"
            else:
                feedback_text = "incorrect"
        elif (key_resp_2.keys == "n"):
            if(c_resp == "n"):
                feedback_text = "correct"
            else:
                feedback_text = "incorrect"
        else:
            feedback_text = "miss"
        text_2.setText(feedback_text)
        # keep track of which components have finished
        feedbackComponents = [text_2]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "thank_you" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    thank_youComponents = [text_norm_7]
    for thisComponent in thank_youComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thank_you" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_7* updates
        
        # if text_norm_7 is starting this frame...
        if text_norm_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_7.frameNStart = frameN  # exact frame index
            text_norm_7.tStart = t  # local t and not account for scr refresh
            text_norm_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_7.status = STARTED
            text_norm_7.setAutoDraw(True)
        
        # if text_norm_7 is active this frame...
        if text_norm_7.status == STARTED:
            # update params
            pass
        
        # if text_norm_7 is stopping this frame...
        if text_norm_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_norm_7.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text_norm_7.tStop = t  # not accounting for scr refresh
                text_norm_7.frameNStop = frameN  # exact frame index
                # update status
                text_norm_7.status = FINISHED
                text_norm_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thank_youComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thank_you" ---
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    # Run 'End Experiment' code from load_variables
    def obfuscate_file(file_path):
        if file_path.endswith('.obfuscated'):
            print(f"File {file_path} is already obfuscated. Skipping.")
            return
    
        with open(file_path, 'rb') as file:
            content = file.read()
    
        obfuscated_content = base64.b64encode(content)
    
        obfuscated_file_path = file_path + '.obfuscated'
        with open(obfuscated_file_path, 'wb') as file:
            file.write(obfuscated_content)
    
        os.remove(file_path)
        print(f"File {file_path} has been obfuscated.")
    
    def obfuscate_data_folder(folder_path):
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    obfuscate_file(file_path)
    
    # Usage
    data_folder = 'data'
    obfuscate_data_folder(data_folder)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
