#!/usr/bin/python

##################################################

class IGarageDoorState(object):

  def __init__(self):
    print self.__class__.__name__
  def pressButton(self):
    raise NotImplementedError
  def wait(self):
    raise NotImplementedError
  def bogus(self):
    raise NotImplementedError

##################################################

class GarageDoorClosedState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorOpeningState())
  def wait(self,action):
    return

##################################################

class GarageDoorClosingState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorClosingPausedState())
  def wait(self,action):
    action.changeState(GarageDoorClosedState())

##################################################

class GarageDoorClosingPausedState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorClosingState())
  def wait(self,action):
    return

##################################################

class GarageDoorOpeningState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorOpeningPausedState())
  def wait(self,action):
    action.changeState(GarageDoorOpenState())

##################################################

class GarageDoorOpeningPausedState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorOpeningState())
  def wait(self,action):
    return

##################################################

class GarageDoorOpenState(IGarageDoorState):

  def pressButton(self,action):
    action.changeState(GarageDoorClosingState())
  def wait(self,action):
    return

##################################################

class GarageAction(object):

  def pressButton(self):
    self.currentState.pressButton(self)
  def wait(self):
    self.currentState.wait(self)
  def changeState(self,newState):
    self.currentState = newState

  currentState = GarageDoorClosedState()

##################################################


garageOpener = GarageAction()
garageOpener.pressButton() # --> opening
garageOpener.wait()        # --> open
garageOpener.wait()        # --> nothing
garageOpener.pressButton() # --> closing
garageOpener.pressButton() # --> closing, paused
garageOpener.wait()        # --> nothing
garageOpener.wait()        # --> nothing
garageOpener.pressButton() # --> closing
garageOpener.pressButton() # --> closing, paused
garageOpener.pressButton() # --> closing
garageOpener.wait()        # --> closed
garageOpener.pressButton() # --> opening
garageOpener.wait()        # --> open

