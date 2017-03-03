from core.base.corebaseclassfactory import CoreBaseClassFactory
from core.utils.log import Log

from kivy.uix.label import Label


class GUILabel(Label):
    _nameIndex = 0
    _namePrefix = "kivy.guilabel"

    def __init__(self):
        super(GUILabel, self).__init__()
        self.sc = None
        self.context = None
        self.callbacks = {}
        self.name = self.generateName()
        CoreBaseClassFactory.construct(self)

    def get_name(self):
        return self.name

    def serviceAddCallback(self, params):
        CoreBaseClassFactory.serviceAddCallback(self, params);

    def serviceAddCallbacks(self, params):
        CoreBaseClassFactory.serviceAddCallbacks(self, params)

    def serviceRemoveCallback(self, params):
        CoreBaseClassFactory.serviceRemoveCallback(self, params);

    def serviceRemoveCallbacks(self, params):
        CoreBaseClassFactory.serviceRemoveCallbacks(self, params);

    def createCallBack(self, group):
        return CoreBaseClassFactory.createCallBack(self, group);

    def log(self, message):
        Log.add(message)

    def log(self, *messages):
        m = ""
        for message in messages:
            m += str(message)
            m += " "
        Log.add(m)

    def generateName(self):
        GUILabel._nameIndex += 1
        return GUILabel._namePrefix + str(GUILabel._nameIndex)