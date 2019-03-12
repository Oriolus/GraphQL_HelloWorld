import logging
import logging.config
import yaml
from flask_app import create_app


with open('log.config.yaml', 'r') as log_conf:
    config = yaml.safe_load(log_conf)
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('Message')
logger.error('Error')

app = create_app()

if __name__ == '__main__':
    app.run()

