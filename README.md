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

The EventEmitter class is defined and exposed by the module:
``` python
from node_events import EventEmitter
```

#### EventEmitter.`addListener`(eventName, listener)

* `eventName`: &lt;string&gt;
* `listener`: &lt;function&gt;
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Alias for [`self.on(eventName, listener)`](#eventemitter_on)

#### <a id="eventemitter_on"></a> EventEmitter.`on`(eventName, listener)

* `eventName`: &lt;string&gt; The name of the event.
* `listener`: &lt;function&gt; The callback function.
* Returns: &lt;[EventEmitter](#eventemitter)&gt;

Appends the `listener` to the listeners array for the event named `eventName`. Multiple calls passing the same combination of eventName and listener will result in the listener being added, and called, multiple times.
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

``` python
emitter = EventEmitter()

def newConnection():
  print('someone connected!')

emitter.prependOnceListener('connection', newConnection)
emitter.emit('connection')
```

Returns a reference to the `EventEmitter`, so that calls can be chained.

## Development

### Building

Feel free to clone, use in adherance to the [license](#license) and perhaps send pull requests

``` bash
git clone https://github.com/miraclx/node_events.py.git
cd node_events.py
# hack on code
python3 setup.py bdist_wheel
pip3 install dist/*.whl --user
```

## License

[Apache 2.0][license] © **Miraculous Owonubi** ([@miraclx][author-url]) &lt;omiraculous@gmail.com&gt;

[license]:  LICENSE 'Apache 2.0 License'
[author-url]: https://github.com/miraclx

[pypi-url]: https://pypi.org/project/node-events
[pypi-image]: https://img.shields.io/pypi/v/node-events.svg?color=red&label=node-events&style=popout-square
[license-image]: https://img.shields.io/pypi/l/node-events.svg?color=green&label=License&style=popout-square
[version-image]: https://img.shields.io/pypi/pyversions/node-events.svg?color=blue&label=PythonVersion&style=popout-square
