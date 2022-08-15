from abc import ABC, abstractmethod

"""
Command Interface
"""

class Run(ABC):
  @abstractmethod
  def process(self):
      pass
