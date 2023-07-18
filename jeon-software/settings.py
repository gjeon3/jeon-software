from os import environ

SESSION_CONFIGS = [
    dict(
        name='All',
        app_sequence=['Introduction','Risk','Quiz','Practice','Auction_T1','Survey','Out'],
        num_demo_participants=2,
    ),
    dict(
        name='Out',
        app_sequence=['Out'],
        num_demo_participants=2,
    ),
    dict(
        name='Risk',
        app_sequence=['Risk'],
        num_demo_participants=2,
    ),
    dict(
        name='Auction_T1',
        app_sequence=['Auction_T1'],
        num_demo_participants=2,
    ),
    dict(
        name='Introduction',
        app_sequence=['Introduction'],
        num_demo_participants=2,
    ),
    dict(
        name='Quiz',
        app_sequence=['Quiz'],
        num_demo_participants=1,
    ),
    dict(
        name='Practice',
        app_sequence=['Practice'],
        num_demo_participants=1,
    ),
    dict(
        name='Survey',
        app_sequence=['Survey'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['own_risk',
                        'bid_1','is_winner_1','opponent_bid_1',
                      'entry_2','bid_2','is_winner_2',
                      'computer_3','bid_3','is_winner_3',
                      'entry_4','bid_4','is_winner_4',
                      'task_selected','event_selected',]
SESSION_FIELDS = []

ROOMS = [
    dict(
        name='test',
        display_name='test',
        participant_label_file='_rooms/excenlab.txt',
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3229434338352'
