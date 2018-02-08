import asyncio
import logging

import time
from chromewhip import Chrome
from chromewhip.protocol import page, dom
import subprocess
# see logging from chromewhip
logging.basicConfig(level=logging.DEBUG)

HOST = '127.0.0.1'
PORT = 9222

p = subprocess.Popen(["google-chrome", "--remote-debugging-port=9222", "--incognito"], stdout=subprocess.PIPE)
time.sleep(3)

loop = asyncio.get_event_loop()
c = Chrome(host=HOST, port=PORT)

loop.run_until_complete(c.connect())

tab = c.tabs[0]

loop.run_until_complete(tab.enable_page_events())

cmd = page.Page.navigate(url='http://myip.dnsomatic.com/')

# send_command will return once the frameStoppedLoading event is received THAT matches
# the frameId that it is in the returned command payload.
await_on_event_type = page.FrameStoppedLoadingEvent

result = loop.run_until_complete(tab.send_command(cmd, await_on_event_type=await_on_event_type))

# send_command always returns a dict with keys `ack` and `event`
# `ack` contains the payload on response of a command
# `event` contains the payload of the awaited event if `await_on_event_type` is provided
ack = result['ack']['result']
event = result['event']
assert ack['frameId'] == event.frameId

cmd = page.Page.setDeviceMetricsOverride(width=800,
                                         height=600,
                                         deviceScaleFactor=0.0,
                                         mobile=False)

loop.run_until_complete(tab.send_command(cmd))

result = loop.run_until_complete(tab.send_command(dom.DOM.getDocument()))

dom_obj = result['ack']['result']['root']

# Python types are determined by the `types` fields in the JSON reference for the
# devtools protocol, and `send_command` will convert if possible.
assert isinstance(dom_obj, dom.Node)

print(dom_obj.nodeId)
print(dom_obj.nodeName)
