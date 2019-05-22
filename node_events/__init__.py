# -*- coding: utf-8 -*-

"""
                node_events.py:
A mini-python-rewrite of the NodeJS EventEmitter
based on a simple implementation of its eventloop
"""

__author__ = "Miraculous Owonubi"
__copyright__ = "Copyright 2019"
__credits__ = ["Miraculous Owonubi"]
__license__ = "Apache-2.0"
__version__ = "0.5.0"
__maintainer__ = "Miraculous Owonubi"
__email__ = "omiraculous@gmail.com"
__status__ = "Development"


class EventListenerStack():
    def __init__(self,  event):
        self.__event = event
        self.__listeners = []

    def respond(self, data):
        if self.hasListeners():
            for listener in self.listeners:
                listener.respond(data)
            return True
        return False

    def verifyHasListener(self, fn):
        return bool(self.extractInstanceOf(fn))

    def attachListener(self, fn, index):
        if not self.verifyHasListener(fn):
            self.__listeners.insert(index, EventListener(fn))

    def detachListener(self, fn):
        listener = self.extractInstanceOf(fn)
        if (listener):
            self.__listeners.remove(listener)
            return True
        else:
            return False

    def detachAllListeners(self):
        for listener in self.listeners:
            self.detachListener(listener)

    @property
    def listeners(self):
        return list(self.__listeners)

    @property
    def rawListeners(self):
        return self.__listeners

    @property
    def listenerCount(self):
        return len(self.__listeners)

    def hasListeners(self):
        return bool(self.listenerCount)

    def extractInstanceOf(self, fn):
        result = None
        for listener in self.listeners:
            if listener.verify(fn):
                result = listener
        return result


class EventListener():
    def __init__(self, listener):
        self.listener = self.__listener = listener
        self._called_times = 0

    def respond(self, data):
        self._called_times += 1
        self.__listener(data)

    def verify(self, fn):
        return self.__listener == fn


class EventEmitter:
    def __init__(self):
        self.__listeners = {}

    def __onceWrap(self, event, listener):
        def wrapped_fn(data):
            self.removeListener(event, wrapped_fn)
            listener(data)
        return wrapped_fn

    def __addListener(self, event, listener, prepend):
        if not self.hasEvent(event):
            self.__listeners[event] = EventListenerStack(event)
        stack = self.getStackOf(event)
        stack.attachListener(listener, 0 if prepend else stack.listenerCount)
        return self

    def on(self, event, listener):
        return self.__addListener(event, listener, False)

    def prependListener(self, event, listener):
        return self.__addListener(event, listener, True)

    def once(self, event, listener):
        return self.__addListener(event, self.__onceWrap(event, listener), False)

    def prependOnceListener(self, event, listener):
        return self.__addListener(event, self.__onceWrap(event, listener), True)

    def emit(self, event, data):
        return self.hasEvent(event) and self.getStackOf(event).respond(data)

    def off(self, *args):
        return self.removeListener(*args)

    def removeListener(self, event, listener):
        if self.hasEvent(event, True):
            self.getStackOf(event).detachListener(listener)

    def removeAllListeners(self, event):
        if self.hasEvent(event, True):
            self.getStackOf(event).detachAllListeners()
        del self.__listeners[event]

    def hasEvent(self, event, raiseException=False):
        status = event in self.__listeners and type(
            self.__listeners[event]) is EventListenerStack
        if not status and raiseException:
            raise Exception(
                "Event: %s doesn't exist within EventEmitter instance" % event)
        return status

    def hasListeners(self, event):
        return self.hasEvent(event) and self.getStackOf(event).hasListeners()

    def getStackOf(self, event):
        return self.__listeners[event] if self.hasEvent(event) else None

    @property
    def rawListeners(self):
        return self.__listeners


if __name__ == "__main__":
    raise Exception(
        "This is a library not meant to be executed as a standalone script")
