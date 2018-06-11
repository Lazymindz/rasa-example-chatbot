from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def run_model_init(domain_file="example_domain.yml",
                          training_data_file='data/stories.md',
                          model_path='models/dialouge'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy()])

    training_data = agent.load_data(training_data_file)

    agent.train(training_data,
                augmentation_factor= 50,
                epochs = 500,
                batch_size = 10,
                validation_split = 0.2)

    agent.persist(model_path)


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    run_model_init()
