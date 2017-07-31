import os
basedir = os.path.abspath(os.path.dirname(__file__))


def get_env_variable(var_name, default=False):
    """
    Get the environment variable or return exception
    :param var_name: Environment Variable to lookup
    """
    try:
        return os.environ[var_name]
    except KeyError:
        import StringIO
        import ConfigParser
        env_file = os.environ.get('PROJECT_ENV_FILE', basedir + "/.env")
        try:
            config = StringIO.StringIO()
            config.write("[DATA]\n")
            config.write(open(env_file).read())
            config.seek(0, os.SEEK_SET)
            cp = ConfigParser.ConfigParser()
            cp.readfp(config)
            value = dict(cp.items('DATA'))[var_name.lower()]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            os.environ.setdefault(var_name, value)
            return value
        except (KeyError, IOError):
            if default is not False:
                return default
            from django.core.exceptions import ImproperlyConfigured
            error_msg = "Either set the env variable '{var}' or place it in your " \
                        "{env_file} file as '{var} = VALUE'"
            raise ImproperlyConfigured(error_msg.format(var=var_name, env_file=env_file))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'hello-flask-example'
    SQLALCHEMY_DATABASE_URI = get_env_variable('DATABASE_URL')
    APP_SETTINGS = get_env_variable('APP_SETTINGS')

    # UPLOAD_FOLDER = '/path/to/the/uploads'
    UPLOAD_FOLDER = '{}{}'.format(basedir, '/image')

    @staticmethod
    def init_app(app):
        pass



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
