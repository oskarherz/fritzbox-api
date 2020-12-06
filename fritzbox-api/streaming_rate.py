from typing import NamedTuple


class StreamingRate():
  downstream: int
  upstream: int
  name: str
  mode: str

  def __init__(self, from_dict: dict):
    self.upstream = from_dict['upstream']
    self.downstream = from_dict['downstream']
    self.name = from_dict['name']
    self.mode = from_dict['mode']

  def __repr__(self) -> str:
    return "StreamingRate(downstream={}, upstream={}, name='{}', mode='{}')".format(
      self.downstream,
      self.upstream,
      self.name,
      self.mode
    )
