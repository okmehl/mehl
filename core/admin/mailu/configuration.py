import os

from socrate import system

DEFAULT_CONFIG = {
    # Specific to the admin UI
    'SUBNET': '10.0.0.0/8',
    'BABEL_DEFAULT_LOCALE': 'en',
    'BABEL_DEFAULT_TIMEZONE': 'UTC',
    'BOOTSTRAP_SERVE_LOCAL': True,
    'RATELIMIT_STORAGE_URL': '',
    'QUOTA_STORAGE_URL': '',
    'DEBUG': False,
    'DOMAIN_REGISTRATION': False,
    'TEMPLATES_AUTO_RELOAD': True,
    # Database settings
    'DB_FLAVOR': 'mysql',
    'DB_USER': 'mailu',
    'DB_PW': None,
    'DB_HOST': 'database',
    'DB_NAME': 'mailu',
    'SQLITE_DATABASE_FILE':'data/main.db',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////data/main.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    # Statistics management
    'INSTANCE_ID_PATH': '/data/instance',
    'STATS_ENDPOINT': '18.{}.stats.mailu.io',
    # Common configuration variables
    'SECRET_KEY': 'changeMe',
    'DOMAIN': 'mailu.io',
    'HOSTNAMES': 'mail.mailu.io,alternative.mailu.io,yetanother.mailu.io',
    'POSTMASTER': 'postmaster',
    'TLS_FLAVOR': 'mail',
    'AUTH_RATELIMIT': '10/minute;1000/hour',
    'AUTH_RATELIMIT_SUBNET': True,
    'DISABLE_STATISTICS': False,
    # Mail settings
    'DMARC_RUA': None,
    'DMARC_RUF': None,
    'WELCOME': False,
    'WELCOME_SUBJECT': 'Dummy welcome topic',
    'WELCOME_BODY': 'Dummy welcome body',
    'DKIM_SELECTOR': 'dkim',
    'DKIM_PATH': '/dkim/{domain}.{selector}.key',
    'DEFAULT_QUOTA': 1000000000,
    # Web settings
    'SITENAME': 'Mehl',
    'WEBSITE': 'https://mehl.io',
    'WEB_ADMIN': '/admin',
    'WEB_WEBMAIL': '/webmail',
    'WEBMAIL': 'none',
    'RECAPTCHA_PUBLIC_KEY': '',
    'RECAPTCHA_PRIVATE_KEY': '',
    # Advanced settings
    'PASSWORD_SCHEME': 'PBKDF2',
    'LOG_LEVEL': 'WARNING',
    # Host settings
    'IMAP_SERVICE': 'imap',
    'LMTP_SERVICE': 'imap:2525',
    'POP3_SERVICE': 'imap',
    'SMTP_SERVICE': 'smtp',
    'AUTHSMTP_SERVICE': 'smtp',
    'ADMIN_SERVICE': 'admin',
    'WEBMAIL': 'none',
    'WEBMAIL_SERVICE': 'webmail',
    'WEBDAV_SERVICE': 'webdav:5232',
    'REDIS_SERVICE': 'redis',
    'FRONT_SERVICE': 'front',
    'ANTISPAM_MILTER_SERVICE': 'antispam:11332',
    'ANTISPAM_WEBUI_SERVICE': 'antispam:11334',
    'ANTIVIRUS_SERVICE': 'antivirus:3310'
}

class ConfigManager(dict):
    """ Naive configuration manager that uses environment only
    """

    DB_TEMPLATES = {
        'sqlite': 'sqlite:////{SQLITE_DATABASE_FILE}',
        'postgresql': 'postgresql://{DB_USER}:{DB_PW}@{DB_HOST}/{DB_NAME}',
        'mysql': 'mysql://{DB_USER}:{DB_PW}@{DB_HOST}/{DB_NAME}'
    }

    def __init__(self):
        self.config = dict()

    def __coerce_value(self, value):
        if isinstance(value, str) and value.lower() in ('true','yes'):
            return True
        elif isinstance(value, str) and value.lower() in ('false', 'no'):
            return False
        return value

    def init_app(self, app):
        self.config.update(app.config)
        # get environment variables
        self.config.update({
            key: self.__coerce_value(os.environ.get(key, value))
            for key, value in DEFAULT_CONFIG.items()
        })
        
        # automatically set the sqlalchemy string
        if self.config['DB_FLAVOR']:
            template = self.DB_TEMPLATES[self.config['DB_FLAVOR']]
            self.config['SQLALCHEMY_DATABASE_URI'] = template.format(**self.config)

        self.config['RATELIMIT_STORAGE_URL'] = 'redis://{0}/2'.format(self.config['REDIS_SERVICE'])
        self.config['QUOTA_STORAGE_URL'] = 'redis://{0}/1'.format(self.config['REDIS_SERVICE'])
        # update the app config itself
        app.config = self

    def setdefault(self, key, value):
        if key not in self.config:
            self.config[key] = value
        return self.config[key]

    def get(self, *args):
        return self.config.get(*args)

    def keys(self):
        return self.config.keys()

    def __getitem__(self, key):
        return self.config.get(key)

    def __setitem__(self, key, value):
        self.config[key] = value

    def __contains__(self, key):
        return key in self.config
