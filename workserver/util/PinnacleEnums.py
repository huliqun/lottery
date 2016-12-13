# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:17:46 2016

@author: Administrator
"""

BET_STATUS = [['ACCEPTED',               'Bet was accepted.'],
              ['CANCELLED',              'Bet is cancelled as per Pinnacle Sports betting rules.'],
              ['LOSE',                   'The bet is settled as lose.'],
              ['PENDING_ACCEPTANCE',     'This status is reserved only for live bets. If a live bet is placed during danger zone or live delay is applied, it will be in PENDING_ACCEPTANCE , otherwise in ACCEPTED status. From this status bet can go to ACCEPTED or REJECTED status.'],
              ['REFUNDED',               'When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status.'],
              ['REJECTED',               'Bet was rejected. Bet can be rejected only if it was previously in PENDING_ACCEPTANCE status.'],
              ['WON',                    'The bet is settled as won.'],
             ]
             
BET_TYPE = [['MONEYLINE', ],
            ['TEAM_TOTAL_POINTS', ],
            ['SPREAD', ],
            ['TOTAL_POINTS', ],
           ]
           
BETLIST_TYPE = [['SETTLED',              'Settled bets'],
                ['RUNNING',              'Running bets'],
                ['CANCELLED',            'Cancelled bets'],
                ]
BOOLEAN = [['FALSE', ],
            ['TRUE', ]
           ]
           
BOOLEAN2 = [['0', 'FALSE'],
            ['TRUE', 'TRUE'],
           ]
           
EVENT_STATUS = [['H',                    'This status indicates that the lines are temporarily unavailable for betting.'],
                ['I',                    'This status indicates that one or more lines have a red circle (a lower maximum bet amount).'],
                ['O',                    'This is the starting status of a game. It means that the lines are open for betting.'],
                ]

FEED_ODDS_FORMAT_TYPE = [['0',       'American odds format'],
                         ['1',       'Decimal odds format'],
                         ['2',       'HongKong odds format'],
                         ['3',       'Indonesian odds format'],
                         ['4',       'Malay odds format'],
                         ['5',       'Fraction odds format'],
                         ]
                         
FEED_STATUS_RESPONSE = [['fail',       'There was an error'],
                        ['OK',         'Feed has response'],
                       ]
                       
GETLINE_RESPONSE_STATUS = [['NOT_EXISTS',       'Line not offered anymore'],
                           ['SUCCESS',          'OK'],
                          ]
                          
INRUNNING_STATE = [['1',       'First half in progress'],
                   ['2',       'Half time in progress'],
                   ['3',       'Second half in progress'],
                   ['4',       'End of regular time'],
                   ['5',       'First half extra time in progress'],
                   ['6',       'Extra time half time in progress'],
                   ['7',       'Second half extra time in progress'],
                   ['8',       'End of extra time'],
                   ['9',       'End of Game'],
                   ['10',      'Game is temporary suspended'],
                   ['11',      'Penalties in progress'],
                  ]
                  
LEG_BET_TYPE = [['MONEYLINE', ] ,
            ['SPREAD', ],
            ['TOTAL_POINTS', ],
           ]
           
LEG_BET_STATUS = [['CANCELLED',           'The leg is canceled- the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. '],
                  ['LOSE',                'The leg is a push - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss'],
                  ['PUSH',                'This status is reserved only for live bets. If a live bet is placed during danger zone or live delay is applied, it will be in PENDING_ACCEPTANCE , otherwise in ACCEPTED status. From this status bet can go to ACCEPTED or REJECTED status.'],
                  ['REFUNDED',            'The leg is refunded - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. '],
                  ['REJECTED',            'The leg is rejected - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. '],
                  ['WON',                 'The leg is a won or a push-won. When Push-won happens, the half of the stake on the leg will be pushed to the next leg, and the other half is won. This can happen only when the leg is placed on a quarter points handicap.'],
                 ]

LIVE_STATUS = [['0',       'No live betting will be offered on this event.'],
               ['1',       'Live betting event.'],
               ['2',       'Live betting will be offered on this event.'],
               ]
               
ODDS_FORMAT = [['AMERICAN', ] ,
               ['DECIMAL',  ] ,
               ['HONGKONG', ] ,
               ['INDONESIAN', ] ,
               ['MALAY', ] ,
               ]            

PARLAY_LINES_STATUS = [['PROCESSED_WITH_ERROR',       'Parlay contains error(s).'],
                       ['VALID',                      '	Parlay is valid.'],
                       ]
                       
PARLAY_RESTRICTION = [['0',       'Allowed to parlay, without restrictions.'],
                      ['1',       'Not allowed to parlay this event.'],
                      ['2',       'Allowed to parlay, with the restrictions. You can not have more than one leg from the same event in the parlay. All events with the same rot number are treated as the same event.'],
                      ]
                      
PLACE_PARLAY_BET_ERROR_CODE = [['ABOVE_MAX_BET_AMOUNT',         'Stake is above allowed maximum amount'],
                               ['ALL_BETTING_CLOSED',           'Betting is not allowed at this moment'],
                               ['BELOW_MIN_BET_AMOUNT',         'Stake is below allowed minimum amount'],
                               ['BLOCKED_BETTING',              'Customer is an agent'],
                               ['BLOCKED_CLIENT',               'Client is no longer active'],
                               ['INSUFFICIENT_FUNDS',           'Bet is submitted by a client with insufficient funds'],
                               ['INVALID_COUNTRY',              'Client country is not allowed for betting'],
                               ['INVALID_LEGS',                 'One or more legs are invalid'],
                               ['INVALID_ODDS_FORMAT',          'If a bet was submitted with the odds format that is not allowed for the client'],
                               ['INVALID_ROUND_ROBIN_OPTIONS',  'Round robin options are invalid (i.e. does not match with number of legs)'],
                               ['ROUND_ROBIN_DISALLOWED',       'Round robin is disallowed for one of the leagues'],
                               ['TOO_MANY_LEGS',                'Maximum of 10 legs can be specified'],
                               ['TOO_FEW_LEGS',                 'At least 2 legs are required for Parlay'],
                               ]
                               
PLACE_PARLAY_BET_RESPONSE_STATUS = [['ACCEPTED',                'Accepted'],
                                    ['PENDING_ACCEPTANCE',      'Pending Acceptance.'],
                                    ['PROCESSED_WITH_ERROR',    'Processed with error'],
                                    ]
                                    
PLACE_PARLAY_LEG_ERROR_CODE = [['CANNOT_PARLAY_LIVE_GAME',                'The wager is placed on Live game'],
                               ['CORRELATED',                             'The leg is correlated with another one'],
                               ['EVENT_NO_LONGER_AVAILABLE_FOR_BETTING',  'The event is no longer offered for Parlays'],
                               ['EVENT_NOT_OFFERED_FOR_PARLAY',           'The event is not offered for Parlays'],
                               ['INVALID_EVENT',                          'Live betting is not allowed at this moment'],
                               ['INVALID_LEG_BET_TYPE',                   'Leg bet type is not accepted for Parlays, Accepted values are: SPREAD, MONEYLINE, TOTAL_POINTS'],
                               ['INVALID_PARLAY_BET',                     'The leg did not validated due to error on Parlay Bet. Check the error PlaceParlayBet response for error details'],
                               ['LINE_CHANGED',                           'Bet is submitted on a line that has changed'],
                               ['LINE_DOES_NOT_BELONG_TO_EVENT',          'LineId does not match the EventId specified in the request'],
                               ['LISTED_PITCHERS_SELECTION_ERROR',        'If bet was submitted with pitcher1MustStart and/or pitcher2MustStart parameters with values that are not allowed'],
                               ['ODDS_NO_LONGER_OFFERED_FOR_PARLAY_1',    'Due to line change odds are not offered for Parlay anymore'],
                               ['ODDS_NO_LONGER_OFFERED_FOR_PARLAY_2',    'Due to line change odds are not offered for Parlay anymore'],
                               ['ODDS_NO_LONGER_OFFERED_FOR_PARLAY_3',    'Due to line change odds are not offered for Parlay anymore'],
                               ['OFFLINE_EVENT',                          'Bet is submitted on an event that is offline or with incorrect lineId'],
                               ['PAST_CUTOFFTIME',                        'Bet is submitted on a game after the betting cutoff time'],
                               ['SYSTEM_ERROR_1',                         'Unexpected error or System error'],
                               ['SYSTEM_ERROR_2',                         'Unexpected error or System error'],
                               ['SYSTEM_ERROR_3',                         'Unexpected error or System error'],
                               ]
                               
PLACE_PARLAY_LEG_RESPONSE_STATUS = [['PROCESSED_WITH_ERROR',                'Processed with error'],
                                    ['VALID',                               'Valid leg'],
                                    ]
                                    
PLACE_TEASER_BET_CODE = [['BLOCKED_BETTING',                ''],
                         ['DUPLICATED_REQUEST',             ''],
                         ['RESUBMIT_REQUEST',               'The ticket hast to be resubmitted'],
                         ['UNEXPECTED_ERROR',               ''],
                         ]                                    
                                    
PLACE_TEASER_BET_ERROR_CODE = [['ABOVE_MAX_BET_AMOUNT',                'Bet is above the maximum allowed'],
                               ['ALL_BETTING_CLOSED',                  'The wagering is disabled in the system (not related to a customer)'],
                               ['BELOW_MIN_BET_AMOUNT',                'Bet is below the minimum allowed'],
                               ['BLOCKED_BETTING',                     'Customer is an agent'],
                               ['BLOCKED_CLIENT',                      'Customer is inactive in the system'],
                               ['DOUBLE_HIT',                          'The website submitted the same bet more than once'],
                               ['DUPLICATE_CLIENT_REFERENCE_ID',       'The teaser unique id and/or one of the leg unique id are the same'],
                               ['INCOMPLETE_CUSTOMER_BETTING_PROFILE', 'The customer does not exist'],
                               ['INSUFFICIENT_FUNDS',                  'The risk amount is above the customer’s available balance'],
                               ['INVALID_COUNTRY',                     'Current location is proscribed'],
                               ['INVALID_CUSTOMER_PROFILE',            'EITHER the customer does not exist OR the customer business rules are not verified'],
                               ['INVALID_LEGS',                        'One or more legs are not verified'],
                               ['INVALID_REQUEST',                     'Teaser request is not valid'],
                               ['ODDS_FORMAT_MISMATCH',                'Agent customer’s odds format differs from wager request odds format'],
                               ['RESUBMIT_REQUEST',                    'The ticket hast to be resubmitted'],
                               ['TEASER_DOES_NOT_EXIST',               'Teaser does not exist in the system'],
                               ['SAME_EVENT_ONLY_REQUIRED',            'Legs required to be for the same game only. Specified in the Teaser Specifications'],
                               ['SYSTEM_ERROR_1',                      'Teasers and TeaserLegs have only one generic SystemError (not 1, 2, 3) which can be anything from DB error to the error we could not map or Undefined'],
                               ['SYSTEM_ERROR_2',                      'Teasers and TeaserLegs have only one generic SystemError (not 1, 2, 3) which can be anything from DB error to the error we could not map or Undefined. In this case the betting api is mapped to Undefined'],
                               ['SYSTEM_ERROR_3',                      'Teasers and TeaserLegs have only one generic SystemError (not 1, 2, 3) which can be anything from DB error to the error we could not map or Undefined. In this case the betting api is mapped to Teaser Pay Card does not exist in the system'],
                               ['TOO_FEW_LEGS',                        'Legs count is below Min Picks specified in the Teaser Specifications'],
                               ['TOO_MANY_LEGS',                       'Legs count is above Max Picks specified in the Teaser Specifications'],
                               ['UNKNOWN',                             'An unknown error has occured'],
                               ['WAGERING_SUSPENDED',                  'The customer wagering is suspended'],
                               ]
                               
PLACE_TEASER_BET_LEG_STATUS = [['PROCESSED_WITH_ERROR',                'Teaser contains error(s)'],
                               ['VALID',                               'Teaser is valid'],
                               ]
                               
PLACE_TEASER_BET_STATUS = [['ACCEPTED',                                'Bet has been successfully placed'],
                           ['PROCESSED_WITH_ERROR',                    'Teaser contains error(s)'],
                           ['VALID',                                   'Teaser is valid'],
                           ]
                           
PLACEBET_ERROR_CODE = [['ALL_BETTING_CLOSED',                          'Betting is not allowed at this moment. This may happen during system maintenance'],
                       ['ALL_LIVE_BETTING_CLOSED',                     'Live betting is not allowed at this moment. This may happen during system maintenance'],
                       ['ABOVE_EVENT_MAX',                             'Bet cannot be placed because client exceeded allowed maximum of risk on a line'],
                       ['ABOVE_MAX_BET_AMOUNT',                        'Stake is above allowed maximum amount'],
                       ['BELOW_MIN_BET_AMOUNT',                        'Stake is below allowed minimum amount'],
                       ['BLOCKED_BETTING',                             'Customer is an agent'],
                       ['BLOCKED_CLIENT',                              'Client is no longer active'],
                       ['INSUFFICIENT_FUNDS',                          'Bet is submitted by a client with insufficient funds'],
                       ['INVALID_COUNTRY',                             'Client country is not allowed for betting'],
                       ['INVALID_EVENT',                               'Invalid eventid'],
                       ['INVALID_ODDS_FORMAT',                         'If a bet was submitted with the odds format that is not allowed for the client'],
                       ['LINE_CHANGED',                                'Bet is submitted on a line that has changed'],
                       ['LISTED_PITCHERS_SELECTION_ERROR',             'If bet was submitted with pitcher1MustStart and/or pitcher2MustStart parameters in Place Bet request with values that are not allowed.'],
                       ['OFFLINE_EVENT',                               'Bet is submitted on a event that is offline (event status is H) or the submitted line is not offered at the moment due to points/handicap change or the submitted bet type is just not offered at the moment.'],
                       ['PAST_CUTOFFTIMEs',                            'Bet is submitted on a game after the betting cutoff time'],
                       ['RED_CARDS_CHANGED',                           'Bet is submitted on a live soccer event with changed red card count'],
                       ['SCORE_CHANGED',                               'Bet is submitted on a live soccer event with changed score'],
                       ['TIME_RESTRICTION',                            'Bet is submitted within too short of a period from the same bet previously placed by a client'],
                       ]
                       
PLACEBET_RESPONSE_STATUS = [['ACCEPTED',                                'Accepted'],
                            ['PENDING_ACCEPTANCE',                      'Pending Acceptance. This is for bets with the live delay or in danger zone'],
                            ['PROCESSED_WITH_ERROR',                    'Processed with error'],
                            ]
                            
PLACE_SPECIAL_BET_ERROR_CODE = [['ALL_BETTING_CLOSED',                      'Betting is not allowed at this moment. This may happen during system maintenance.'],
                                ['ABOVE_MAX_BET_AMOUNT',                    'Stake is above allowed maximum amount'],
                                ['BELOW_MIN_BET_AMOUNT',                    'Stake is below allowed minimum amount'],
                                ['BLOCKED_BETTING',                         'Customer is an agent'],
                                ['BLOCKED_CLIENT',                          'Client is no longer active'],
                                ['INSUFFICIENT_FUNDS',                      'Bet is submitted by a client with insufficient funds'],
                                ['INVALID_COUNTRY',                         'Client country is not allowed for betting'],
                                ['LINE_CHANGED',                            'Bet is submitted on a line that has changed'],
                                ['PAST_CUTOFFTIME',                         'Bet is submitted on a game after the betting cutoff time'],
                                ['SYSTEM_ERROR_1',                          'Unexpected error or System error'],
                                ['SYSTEM_ERROR_2',                          'Unexpected error or System error'],
                                ['RESUBMIT_REQUEST',                        'The ticket hast to be resubmitted'],
                                ['DUPLICATE_UNIQUE_REQUEST_ID',             'UniqueRequestId must be inque for each bet'],
                                ['INVALID_REQUEST',                         'Special bet request is not valid'],
                                ['UNIQUE_REQUEST_ID_REQUIRED',              'UniqueRequestId is missing'],
                                ['RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED', 'Self-imposed risk limit exceeded'],
                                ['RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED', 'Self-imposed loss limit exceeded'],
                                ['INCOMPLETE_CUSTOMER_BETTING_PROFILE',     'Customer profile could not be loaded, please contact CSD'],
                                ['WAGERING_SUSPENDED',                      'The customer wagering is suspended'],
                                ['CONTEST_NOT_FOUND',                       'Incorrect contest id provided or contest is no longer available'],
                                ['CONTEST_FUNCTIONALITY_IS_DISABLED',       'Contest functionality is disabled'],
                                ]
                                
PLACE_SPECIAL_BET_RESPONSE_STATUS = [['ACCEPTED',                      'Accepted'],
                                     ['PROCESSED_WITH_ERROR',          'Processed with error'],
                                     ]
                                     
ROUND_ROBIN_OPTIONS = [['Parlay',                      'Single parlay that include all wagers (No Round Robin)'],
                       ['TwoLegRoundRobin',            'Multiple parlays having 2 wagers each (round robin style). Can be used if number of legs is greater or equal to 3'],
                       ['ThreeLegRoundRobin',          'Multiple parlays having 3 wagers each (round robin style). Can be used if number of legs is greater or equal to 3'],
                       ['FourLegRoundRobin',           'Multiple parlays having 4 wagers each (round robin style). Can be used if number of legs is greater or equal to 4'],
                       ['FiveLegRoundRobin',           'Multiple parlays having 5 wagers each (round robin style). Can be used if number of legs is greater or equal to 5'],
                       ['SixLegRoundRobin',            'Multiple parlays having 6 wagers each (round robin style). Can be used if number of legs is greater or equal to 6'],
                       ['SevenLegRoundRobin',          'Multiple parlays having 7 wagers each (round robin style). Can be used if number of legs is greater or equal to 7'],
                       ['EightLegRoundRobin',          'Multiple parlays having 8 wagers each (round robin style). Can be used if number of legs is  equal to 8'],
                       ]
                       
SIDE_TYPE = [['OVER',],
             ['UNDER',],
            ]
            
TEAM_TYPE = [['Draw',                          'Draw. This is used for MONEYLINE bet type only.'],
             ['Team1',                         'Team 1'],
             ['Team2',                         'Team 2'],
            ]
            
TEASER_LINES_ERROR_CODE = [['INVALID_LEGS',                          'One or more of the legs is invalid.'],
                           ['SAME_EVENT_ONLY_REQUIRED',              'Teaser specified requires that all legs are from the same event.'],
                           ['TEASER_DISABLED',                       'Teaser has been disabled and cannot be bet on.'],
                           ['TEASER_DOES_NOT_EXIST',                 'The teaser identifier could requeted could not be found.'],
                           ['TOO_FEW_LEGS',                          'You do not meet the minimum number of legs requirement for the teaser specified.'],
                           ['TOO_MANY_LEGS',                         'You are above the maximum number of legs for the teaser specified.'],
                           ['UNKNOWN',                               'An unknown error has occured.'],
                          ]            
            
TEASER_LINES_LEG_ERROR_CODE = [['EVENT_NOT_FOUND',                   'The event specified could not be found.'],
                               ['POINTS_NO_LONGER_AVAILABLE',        'The points requested are no longer available. This means that the lines a moved.'],
                               ['UNKNOWN',                           'An unknown error has occured.'],
                               ['WAGER_TYPE_NOT_VALID_FOR_TEASER',   'The specified wager type is not valid for teasers.'],
                               ]
                               
TEASER_LINES_STATUS = [['PROCESSED_WITH_ERROR',                      'Teaser contains error(s).'],
                       ['VALID',                                     'Teaser is valid.'],
                       ]
                       
TEASER_REQUEST_CODE = [['INVALID_REQUEST_DATA',                      'Generic error code indicating that there is something wrong in the request. Refer to associated message containing further details'],
                       ] 
                       
WIN_RISK_TYPE = [['RISK',                      'Stake is risk amount'],
                 ['WIN',                       'Stake is win amount'],
                 ]                       
                      
YES_NO_TYPE = [['No',],
               ['Yes',],
               ]  

SETTLEMENT_STATUS = [['1',                     'Event period is settled'],
                     ['2',                     'Event period is re-settled'],
                     ['3',                     'Event period is cancelled'],
                     ['4',                     'Event period is re-settled as cancelled'],
                     ['5',                     'Event is deleted'],
                    ]
                    
SPECIAL_BET_TYPE = [['MULTI_WAY_HEAD_TO_HEAD',],
                    ['SPREAD',],
                    ['OVER_UNDER',],
                    ]
                    
BETLIST_BET_TYPE = [['MONEYLINE',],
                    ['TEAM_TOTAL_POINTS',],
                    ['SPREAD',],
                    ['TOTAL_POINTS',],
                    ['SPECIAL',],
                    ['PARLAY',],
                    ['TEASER',],
                    ]