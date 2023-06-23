from dataclasses import dataclass
from typing import Union, Callable





# @dataclass
# class EventProperty:
#     activeElement: str = 'activeElement'
#     addEventListener: str = 'addEventListener'
#     adoptNode: str = 'adoptNode'
#     anchors: str = 'anchors'
#     applets: str = 'applets'
#     baseURI: str = 'baseURI'
#     body: str = 'body'
#     charset: str = 'charset'
#     characterSet: str = 'characterSet'
#     close: str = 'close'
#     cookie: str = 'cookie'
#     createAttribute: str = 'createAttribute'
#     createComment: str = 'createComment'
#     createDocumentFragment: str = 'createDocumentFragment'
#     createElement: str = 'createElement'
#     createEvent: str = 'createEvent'
#     createTextNode: str = 'createTextNode'
#     defaultView: str = 'defaultView'	
#     designMode: str = 'designMode'
#     doctype: str = 'doctype'	
#     documentElement: str = 'documentElement'
#     documentMode: str = 'documentMode'
#     documentURI	: str = 'documentURI'
#     domain: str = 'domain'
#     domConfig: str = 'domConfig'
#     embeds: str = 'embeds'
#     execCommand: str = 'execCommand'
#     forms: str = 'forms'
#     getElementById: str = 'getElementById'
#     getElementsByClassName: str = 'getElementsByClassName'
#     getElementsByName: str = 'getElementsByName'
#     getElementsByTagName: str = 'getElementsByTagName'
#     hasFocus: str = 'hasFocus'
#     head: str = 'head'
#     images: str = 'images'
#     implementation: str = 'implementation'
#     importNode: str = 'importNode'
#     inputEncoding: str = 'inputEncoding'
#     lastModified: str = 'lastModified'
#     links: str = 'links'	
#     normalize: str = 'normalize'
#     normalizeDocument: str = 'normalizeDocument'
#     open: str = 'open'
#     querySelector: str = 'querySelector'
#     querySelectorAll: str = 'querySelectorAll'
#     readyState: str = 'readyState'	
#     referrer: str = 'referrer'	
#     removeEventListener: str = 'removeEventListener'
#     renameNode: str = 'renameNode'
#     scripts: str = 'scripts'
#     strictErrorChecking: str = 'strictErrorChecking'
#     title: str = 'title'
#     URL: str = 'URL'
#     write: str = 'write'
#     writeln: str = 'writeln'




@dataclass
class Event:
    occurs: Callable = None
    abort: Callable = None
    afterprint: Callable = None
    animationend: Callable = None
    animationiteration: Callable = None
    animationstart: Callable = None
    beforeprint: Callable = None
    beforeunload: Callable = None
    blur: Callable = None
    canplay: Callable = None
    canplaythrough: Callable = None
    change: Callable = None
    click: Callable = None
    contextmenu: Callable = None
    copy: Callable = None
    cut: Callable = None
    dblclick: Callable = None
    drag: Callable = None
    dragend: Callable = None
    dragenter: Callable = None
    dragleave: Callable = None
    dragover: Callable = None
    dragstart: Callable = None
    drop: Callable = None
    durationchange: Callable = None
    ended: Callable = None
    error: Callable = None
    focus: Callable = None
    focusin: Callable = None
    focusout: Callable = None
    fullscreenchange: Callable = None
    fullscreenerror: Callable = None
    hashchange: Callable = None
    input: Callable = None
    invalid: Callable = None
    keydown: Callable = None
    keypress: Callable = None
    keyup: Callable = None
    load: Callable = None
    loadeddata: Callable = None
    loadedmetadata: Callable = None
    loadstart: Callable = None
    message: Callable = None
    mousedown: Callable = None
    mouseenter: Callable = None
    mouseleave: Callable = None
    mousemove: Callable = None
    mouseover: Callable = None
    mouseout: Callable = None
    mouseup: Callable = None
    mousewheel: Callable = None
    offline: Callable = None
    online: Callable = None
    open: Callable = None
    pagehide: Callable = None
    pageshow: Callable = None
    paste: Callable = None
    pause: Callable = None
    play: Callable = None
    playing: Callable = None
    popstate: Callable = None
    progress: Callable = None
    ratechange: Callable = None
    resize: Callable = None
    reset: Callable = None
    scroll: Callable = None
    search: Callable = None
    seeked: Callable = None
    seeking: Callable = None
    select: Callable = None
    show: Callable = None
    stalled: Callable = None
    storage: Callable = None
    submit: Callable = None
    suspend: Callable = None
    timeupdate: Callable = None
    toggle: Callable = None
    touchcancel: Callable = None
    touchend: Callable = None
    touchmove: Callable = None
    touchstart: Callable = None
    transitionend: Callable = None
    unload: Callable = None
    volumechange: Callable = None
    waiting: Callable = None
    wheel: Callable = None
