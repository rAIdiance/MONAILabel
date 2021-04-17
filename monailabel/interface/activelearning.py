import logging
import random

logger = logging.getLogger(__name__)


class ActiveLearning:
    def next(self, strategy, images):
        images.sort()
        if strategy == "first":
            image = images[0]
        elif strategy == "last":
            image = images[-1]
        else:
            image = random.choice(images)

        logger.info(f"Strategy: {strategy}; Selected Image: {image}")
        return image