# -*- coding: utf-8 -*-

import jpush as jpush
from workserver.util import GLBConfig

def pushMessage(alias, message):
    # alias : UserID
    # message : 需要推送的消息
    _jpush = jpush.JPush(GLBConfig.APP_KEY, GLBConfig.MASTER_SECRET)
    
    push = _jpush.create_push()
    push.audience = jpush.audience(
                jpush.alias(alias)
            )
    push.notification = jpush.notification(alert=message)
    push.platform = jpush.all_
    push.send()
