# node_events.py

> A minor rewrite of the NodeJS EventEmitter in Python

[![PyPI Version][pypi-image]][pypi-url]
![License][license-image]
![Python Version][version-image]

## Installing

Via [PyPI][pypi-url]:

``` bash
pip install node_events
```

## Usage

``` python
from node_events import EventEmitter

myEmitter = EventEmitter()


def fn():
    print("An event occurred")


myEmitter.on('event', fn)
myEmitter.emit('event')

# Prints
#   An event occurred

```

## API

### <a id="eventemitter"></a> Class: `EventEmitter`

The `EventEmitter` class is defined and exposed publicly by the module:
``` python
from node_events import EventEmitter
```

#### EventEmitter.`addListener`(eventName, listener)

* `eventName`: &lt;string&gt;
* `listener`: &lt;function&gt;
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Alias for [`self.on(eventName, listener)`](#eventemitter_on)

Emits the `'addlistener:{eventName}'` event when called.

#### <a id="eventemitter_on"></a> EventEmitter.`on`(eventName, listener)

* `eventName`: &lt;string&gt; The name of the event.
* `listener`: &lt;function&gt; The callback function.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Appends the `listener` to the listeners array for the event named `eventName`. Multiple calls passing the same combination of eventName and listener will result in the listener being added, and called, multiple times.

Emits the `'addlistener:{eventName}'` event when called.

By default, event listeners are invoked in the order they are added. The [`emitter.prependListener()`](#eventemitter_prependlistener) method can be used as an alternative to add the event listener to the beginning of the listeners array.

Returns a reference to the `EventEmitter`, so that calls can be chained.

``` python
emitter = EventEmitter()

def appendListener():
  print('a')

def prependListener():
  print('b')

emitter.on('test', appendListener)
emitter.prependListener('test', appendListener)

emitter.emit('test')

# Prints
#   b
#   a
```

#### <a id="eventemitter_once"></a> EventEmitter.`once`(eventName, listener)

* `eventName`: &lt;string&gt; The name of the event.
* `listener`: &lt;function&gt; The callback function.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Adds a **one-time** `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.

Emits the `'addlistener:{eventName}'` event when called.

By default, event listeners are invoked in the order they are added. The [`emitter.prependOnceListener()`](#eventemitter_prependoncelistener) method can be used as an alternative to add the event listener to the beginning of the listeners array.

Returns a reference to the `EventEmitter`, so that calls can be chained.

``` python
emitter = EventEmitter()

def appendListener():
  print('a')

def prependListener():
  print('b')

emitter.once('test', appendListener)
emitter.prependOnceListener('test', appendListener)

emitter.emit('test')

# Prints
#   b
#   a
```

#### <a id="eventemitter_prependlistener"></a> EventEmitter.`prependListener`(eventName, listener)

* `eventName`: &lt;string&gt; The name of the event.
* `listener`: &lt;function&gt; The callback function.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Adds the `listener` function to the beginning of the listeners array for the event named `eventName`. Multiple calls passing the same combination of eventName and listener will result in the listener being added, and called, multiple times.

Emits the `'addlistener:{eventName}'` event when called.

``` python
emitter = EventEmitter()

def newConnection():
  print('someone connected!')

emitter.prependListener('connection', newConnection)
emitter.emit('connection')
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### <a id="eventemitter_prependoncelistener"></a> EventEmitter.`prependOnceListener`(eventName, listener)

* `eventName`: &lt;string&gt; The name of the event.
* `listener`: &lt;function&gt; The callback function.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Adds a **one-time** `listener` function for the event named `eventName` to the beginning of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.

Emits the `'addlistener:{eventName}'` event when called.

``` python
emitter = EventEmitter()

def newConnection():
  print('someone connected!')

emitter.prependOnceListener('connection', newConnection)
emitter.emit('connection')
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

#### <a id="eventemitter_removealllisteners"></a> EventEmitter.`removeAllListeners`([eventName])

* `eventName`: &lt;string&gt; The name of the event.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Removes all listeners, or those of the specified `eventName`.

Emits the `'rmlistener:{eventName}'` event when called.

Returns a reference to the EventEmitter, so that calls can be chained.

#### <a id="eventemitter_removelistener"></a> EventEmitter.`removeListener`(eventName, listener)

* `eventName`: &lt;string&gt;
* `listener`: &lt;function&gt;
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Removes the specified `listener` from the listener array for the event named `eventName`.

Emits the `'rmlistener:{eventName}'` event when called.

#### <a id="eventemitter_hasevent"></a> EventEmitter.`hasEvent`(eventName, raiseException)

* `eventName`: &lt;string&gt;
* `raiseException`: &lt;boolean&gt; (**Default**: `False`)
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Check if the event emitter has within itself an event named `eventName`, return a boolean for the operation.
if `raiseException` is True, raise an exception if the result of the check evaluates to `False`.

#### <a id="eventemitter_haslisteners"></a> EventEmitter.`hasListeners`(eventName)

* `eventName`: &lt;string&gt;
* `raiseException`: &lt;boolean&gt;
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Safely check that the core [EventListenerStack](#eventlistenerstack) has at least one listener.
Implements the [`EventListenerStack::hasListeners()`](#eventlistenerstack_haslisteners) inherently.

### <a id="eventlistener"></a> Class: `EventListener`(listener)

* `listener`: &lt;function&gt;

This class wraps the `listener` function with useful, sandboxed manipulative features

The `EventListener` class is defined and exposed publicly by the module:
``` python
from node_events import EventListener

def fn():
  print("test_fn")

EventListener(fn).respond()

# Prints
#   test_fn
```

#### <a id="eventlistener_listenercount"></a> EventListener.`listenerCount`<sub>(getter)</sub>

Number of times the function has been called

#### <a id="eventlistener_respond"></a> EventListener.`respond`(*data)

* `*data`: &lt;any&gt;

Send the `data` arguments to the encapsulated function in evaluation

#### <a id="eventlistener_verify"></a> EventListener.`verify`(fn)

* `fn`: &lt;function&gt;
* Returns: &lt;boolean&gt;

Check if `fn` matches with the encapsulated function
Useful in finding the instance amongst others by matching its core

### <a id="eventlistenerstack"></a> Class: `EventListenerStack`(eventName)

* `eventName`: &lt;string&gt;

Stacking layer of listeners for an event defined named `eventName`
Serves as an interfacing remote for series of grouped listeners

The `EventListenerStack` class is defined and exposed publicly by the module:
``` python
from node_events import EventListenerStack

def test_fn():
  print("hi from test_fn")

stack = EventListenerStack("event_name")
stack.attachListener(test_fn, 0)
stack.respond()

# Prints
#   hi from test_fn
```

#### <a id="eventlistenerstack_listeners"></a> EventListenerStack.`listeners`<sub>(getter)</sub>

Return a copy of the private listeners array.

#### <a id="eventlistenerstack_listenercount"></a> EventListenerStack.`listenerCount`<sub>(getter)</sub>

Return the number of listeners exist and are actively waiting for event firings

#### <a id="eventlistenerstack_respond"></a> EventListenerStack.`respond`(*data)

* `*data`: &lt;any&gt;
* Returns: &lt;boolean&gt;

Send the `data` arguments to all the listeners within the stack in the order of which they appear
Returns True if the stack has any active listeners who read the data else False

#### <a id="eventlistenerstack_verifyhaslistener"></a> EventListenerStack.`verifyHasListener`(fn)

* `fn`: &lt;function&gt;

Check if the stack has the listener `fn`

#### <a id="eventlistenerstack_attachlistener"></a> EventListenerStack.`attachListener`(fn, index)

* `fn`: &lt;function&gt;
* `index`: &lt;number&gt;

Attach the `fn` listener to the event stack.
The `index` parameter determines the index at which to place the function in the stack array
Note, function calls are based on orderly calls from the stack array

#### <a id="eventlistenerstack_detachlistener"></a> EventListenerStack.`detachListener`(fn)

* `fn`: &lt;function&gt;
* Returns: &lt;boolean&gt;

Detach the `fn` listener from the stack if it exists returning True otherwise return False

#### <a id="eventlistenerstack_detachalllisteners"></a> EventListenerStack.`detachAllListeners`()

Detach all the listeners within the stack

#### <a id="eventlistenerstack_haslisteners"></a> EventListenerStack.`hasListeners`()

Check if the stack has any listeners within

#### <a id="eventlistenerstack_extractinstanceof"></a> EventListenerStack.`extractInstanceOf`(fn)

* `fn`: &lt;function&gt;

Extract the [`EventListener`](#eventlistener) instance encapsulating the `fn` listener if it exists otherwise return `None`

## Development

### Building

Feel free to clone, use in adherance to the [license](#license) and perhaps send pull requests

``` bash
git clone https://github.com/miraclx/node_events.py.git
cd node_events.py
# hack on code
pip3 install . --user
```

## License

[Apache 2.0][license] © **Miraculous Owonubi** ([@miraclx][author-url]) &lt;omiraculous@gmail.com&gt;

[license]:  LICENSE 'Apache 2.0 License'
[author-url]: https://github.com/miraclx

[pypi-url]: https://pypi.org/project/node-events
[pypi-image]: https://img.shields.io/pypi/v/node-events.svg?color=red&label=node-events&style=popout-square
[license-image]: https://img.shields.io/pypi/l/node-events.svg?color=green&label=License&style=popout-square
[version-image]: https://img.shields.io/pypi/pyversions/node-events.svg?color=blue&label=PythonVersion&style=popout-square
