from abc import ABCMeta, abstractmethod


class MaskGenerator(metaclass=ABCMeta):

    @abstractmethod
    def generate_mask(self, imageObj):
        return
