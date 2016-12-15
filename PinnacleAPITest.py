# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:18:23 2016

@author: huliqun
@email: huliquns@126.com
"""

import logging
from workserver.util import LogUtil

from workserver.util import PinnacleAPI

if __name__ == '__main__':
    LogUtil.initLog()
    logger = logging.getLogger('serverLog')
#    print(PinnacleAPI.GetSportsV2(logger))
    
#    print(PinnacleAPI.GetLeaguesV2(15, logger))
#    print(PinnacleAPI.GetFixtures(15, logger=logger))
#    print(PinnacleAPI.GetSettledFixtures(15, logger=logger))
#    print(PinnacleAPI.GetSpecialFixtures(15, logger=logger))
#    print(PinnacleAPI.GetSettledSpecialFixtures(15, logger=logger))
#    print(PinnacleAPI.GetTeaserGroups('HONGKONG', logger=logger))
#    print(PinnacleAPI.GetOdds(15, logger=logger))
    print(PinnacleAPI.GetOddsParlay(15, logger=logger))

