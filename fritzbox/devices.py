class Device():
  mac: str
  ipv4: str
  ipv6: str
  UID: str
  classes: str
  port: str
  name: str
  model: str
  state: str
  url: str
  type: str

  def __init__(
    self,
    mac: str = None,
    ipv4: str = None,
    ipv6: str = None,
    UID: str = None,
    classes: str = None,
    port: str = None,
    name: str = None,
    model: str = None,
    state: str = None,
    url: str = None,
    type: str = None
  ):
    self.mac = mac
    self.ipv4 = ipv4
    self.ipv6 = ipv6
    self.UID = UID
    self.classes = classes
    self.port = port
    self.name = name
    self.model = model
    self.state = state
    self.url = url
    self.type = type

  def __repr__(self) -> str:
    return 'Device(name={}, mac={}, ipv4={}, ipv6={})'.format(
      self.name,
      self.mac,
      self.ipv4,
      self.ipv6
    )
