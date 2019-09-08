from abc import ABCMeta, abstractmethod

class ICManagerState:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def doPrintState(self): raise NotImplementedError

    @abstractmethod
    def doLaunch(self): raise NotImplementedError

    @abstractmethod
    def doConfigure(self): raise NotImplementedError

    @abstractmethod
    def doStart(self): raise NotImplementedError

    @abstractmethod
    def doTerminate(self): raise NotImplementedError

    @abstractmethod
    def doFinished(self): raise NotImplementedError

class CManagerDormantState(ICManagerState):
    def doPrintState(self):
        print('Current State: DORMANT')
    def doLaunch(self):
        return CManagerCreatingState()
    def doConfigure(self):
        return self
    def doStart(self):
        return self
    def doTerminate(self):
        return self
    def doFinished(self):
        return self

class CManagerCreatingState(ICManagerState):
    def doPrintState(self):
        print('Current State: CREATING')
    def doLaunch(self):
        return self
    def doConfigure(self):
        return CManagerReadyState()
    def doStart(self):
        return self
    def doTerminate(self):
        return self
    def doFinished(self):
        return self

class CManagerReadyState(ICManagerState):
    def doPrintState(self):
        print('Current State: READY')
    def doLaunch(self):
        return self
    def doConfigure(self):
        return self
    def doStart(self):
        return CManagerRunningState()
    def doTerminate(self):
        return self
    def doFinished(self):
        return self

class CManagerRunningState(ICManagerState):
    def doPrintState(self):
        print('Current State: RUNNING')
    def doLaunch(self):
        return self
    def doConfigure(self):
        return self
    def doStart(self):
        return self
    def doTerminate(self):
        return CManagerTerminatingState()
    def doFinished(self):
        return self

class CManagerTerminatingState(ICManagerState):
    def doPrintState(self):
        print('Current State: TERMINATING')
    def doLaunch(self):
        return self
    def doConfigure(self):
        return self
    def doStart(self):
        return self
    def doTerminate(self):
        return self
    def doFinished(self):
        return  CManagerDormantState()

class CManager:
  currentState = CManagerDormantState()

  def printState(self):
      self.currentState.doPrintState()

  def launch(self):
      self.currentState = self.currentState.doLaunch()

  def configure(self):
      self.currentState = self.currentState.doConfigure()

  def start(self):
      self.currentState = self.currentState.doStart()

  def terminate(self):
      self.currentState = self.currentState.doTerminate()
      
  def finished(self):
      self.currentState = self.currentState.doFinished()


cm = CManager()
cm.printState()
cm.configure() # ignored
cm.terminate() # ignored
cm.finished()  # ignored
cm.start()     # ignored
cm.launch()
cm.printState()
cm.configure()
cm.printState()
cm.start()
cm.printState()
cm.terminate()
cm.printState()
cm.finished()
cm.printState()