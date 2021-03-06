# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime
from chromewhip.protocol import dom as DOM

# Animation: Animation instance.
class Animation(ChromeTypeBase):
    def __init__(self,
                 id: Union['str'],
                 name: Union['str'],
                 pausedState: Union['bool'],
                 playState: Union['str'],
                 playbackRate: Union['float'],
                 startTime: Union['float'],
                 currentTime: Union['float'],
                 type: Union['str'],
                 source: Optional['AnimationEffect'] = None,
                 cssId: Optional['str'] = None,
                 ):

        self.id = id
        self.name = name
        self.pausedState = pausedState
        self.playState = playState
        self.playbackRate = playbackRate
        self.startTime = startTime
        self.currentTime = currentTime
        self.type = type
        self.source = source
        self.cssId = cssId


# AnimationEffect: AnimationEffect instance
class AnimationEffect(ChromeTypeBase):
    def __init__(self,
                 delay: Union['float'],
                 endDelay: Union['float'],
                 iterationStart: Union['float'],
                 iterations: Union['float'],
                 duration: Union['float'],
                 direction: Union['str'],
                 fill: Union['str'],
                 easing: Union['str'],
                 backendNodeId: Optional['DOM.BackendNodeId'] = None,
                 keyframesRule: Optional['KeyframesRule'] = None,
                 ):

        self.delay = delay
        self.endDelay = endDelay
        self.iterationStart = iterationStart
        self.iterations = iterations
        self.duration = duration
        self.direction = direction
        self.fill = fill
        self.backendNodeId = backendNodeId
        self.keyframesRule = keyframesRule
        self.easing = easing


# KeyframesRule: Keyframes Rule
class KeyframesRule(ChromeTypeBase):
    def __init__(self,
                 keyframes: Union['[KeyframeStyle]'],
                 name: Optional['str'] = None,
                 ):

        self.name = name
        self.keyframes = keyframes


# KeyframeStyle: Keyframe Style
class KeyframeStyle(ChromeTypeBase):
    def __init__(self,
                 offset: Union['str'],
                 easing: Union['str'],
                 ):

        self.offset = offset
        self.easing = easing


class Animation(PayloadMixin):
    """ 
    """
    @classmethod
    def disable(cls):
        """Disables animation domain notifications.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls):
        """Enables animation domain notifications.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def getCurrentTime(cls,
                       id: Union['str'],
                       ):
        """Returns the current time of the an animation.
        :param id: Id of animation.
        :type id: str
        """
        return (
            cls.build_send_payload("getCurrentTime", {
                "id": id,
            }),
            cls.convert_payload({
                "currentTime": {
                    "class": float,
                    "optional": False
                },
            })
        )

    @classmethod
    def getPlaybackRate(cls):
        """Gets the playback rate of the document timeline.
        """
        return (
            cls.build_send_payload("getPlaybackRate", {
            }),
            cls.convert_payload({
                "playbackRate": {
                    "class": float,
                    "optional": False
                },
            })
        )

    @classmethod
    def releaseAnimations(cls,
                          animations: Union['[]'],
                          ):
        """Releases a set of animations to no longer be manipulated.
        :param animations: List of animation ids to seek.
        :type animations: []
        """
        return (
            cls.build_send_payload("releaseAnimations", {
                "animations": animations,
            }),
            None
        )

    @classmethod
    def resolveAnimation(cls,
                         animationId: Union['str'],
                         ):
        """Gets the remote object of the Animation.
        :param animationId: Animation id.
        :type animationId: str
        """
        return (
            cls.build_send_payload("resolveAnimation", {
                "animationId": animationId,
            }),
            cls.convert_payload({
                "remoteObject": {
                    "class": Runtime.RemoteObject,
                    "optional": False
                },
            })
        )

    @classmethod
    def seekAnimations(cls,
                       animations: Union['[]'],
                       currentTime: Union['float'],
                       ):
        """Seek a set of animations to a particular time within each animation.
        :param animations: List of animation ids to seek.
        :type animations: []
        :param currentTime: Set the current time of each animation.
        :type currentTime: float
        """
        return (
            cls.build_send_payload("seekAnimations", {
                "animations": animations,
                "currentTime": currentTime,
            }),
            None
        )

    @classmethod
    def setPaused(cls,
                  animations: Union['[]'],
                  paused: Union['bool'],
                  ):
        """Sets the paused state of a set of animations.
        :param animations: Animations to set the pause state of.
        :type animations: []
        :param paused: Paused state to set to.
        :type paused: bool
        """
        return (
            cls.build_send_payload("setPaused", {
                "animations": animations,
                "paused": paused,
            }),
            None
        )

    @classmethod
    def setPlaybackRate(cls,
                        playbackRate: Union['float'],
                        ):
        """Sets the playback rate of the document timeline.
        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        return (
            cls.build_send_payload("setPlaybackRate", {
                "playbackRate": playbackRate,
            }),
            None
        )

    @classmethod
    def setTiming(cls,
                  animationId: Union['str'],
                  duration: Union['float'],
                  delay: Union['float'],
                  ):
        """Sets the timing of an animation node.
        :param animationId: Animation id.
        :type animationId: str
        :param duration: Duration of the animation.
        :type duration: float
        :param delay: Delay of the animation.
        :type delay: float
        """
        return (
            cls.build_send_payload("setTiming", {
                "animationId": animationId,
                "duration": duration,
                "delay": delay,
            }),
            None
        )



class AnimationCanceledEvent(BaseEvent):

    js_name = 'Animation.animationCanceled'
    hashable = ['id']
    is_hashable = True

    def __init__(self,
                 id: Union['str', dict],
                 ):
        if isinstance(id, dict):
            id = str(**id)
        self.id = id

    @classmethod
    def build_hash(cls, id):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AnimationCreatedEvent(BaseEvent):

    js_name = 'Animation.animationCreated'
    hashable = ['id']
    is_hashable = True

    def __init__(self,
                 id: Union['str', dict],
                 ):
        if isinstance(id, dict):
            id = str(**id)
        self.id = id

    @classmethod
    def build_hash(cls, id):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AnimationStartedEvent(BaseEvent):

    js_name = 'Animation.animationStarted'
    hashable = ['animationId']
    is_hashable = True

    def __init__(self,
                 animation: Union['Animation', dict],
                 ):
        if isinstance(animation, dict):
            animation = Animation(**animation)
        self.animation = animation

    @classmethod
    def build_hash(cls, animationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
