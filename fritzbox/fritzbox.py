from typing import List
from enum import Enum

import requests

import fritzbox.utils as utils
from fritzbox.utils import LoginFailedException
from fritzbox.devices import Device


DEFAULT_URL = 'http://fritz.box/'


class Page(str, Enum):
  LOGIN_PAGE = 'login_sid.lua'
  LOGOUT_PAGE = 'index.lua'
  DEVICES_PAGE = 'data.lua'

class fritzbox():

  url: str
  password: str
  sid: str

  def __init__(self, url = DEFAULT_URL, password: str = None):
    self.url = url
    self.password = password

  def __enter__(self):
    return self.login(self.password)

  def _exit__(self, type, value, traceback):
    if type is not None:
      self.logout()


  def page(self, page: str):
    return self.url + page

  def login(self, password: str):
    challenge_res = requests.get(self.page(Page.LOGIN_PAGE))
    challenge = utils.get_field_from_xml(xml = challenge_res.content, field = 'Challenge')

    login_hash = utils.build_login_hash(challenge, password)
    login_res = requests.post(
      url = self.page(Page.LOGIN_PAGE),
      data = { 'response': login_hash, 'username': '' }
    )

    sid = utils.get_field_from_xml(xml = login_res.content, field = 'sid')

    if sid == '0000000000000000': 
      raise LoginFailedException(login_res)

    self.sid = sid
    return self


  def get_devices(self, active = True, passive = True) -> List[Device]:
    payload = {
      'xhr': 1,
      'sid': self.sid,
      'lang': 'de',
      'page': 'netDev',
      'xhrId': 'all'
    }

    res = requests.post(
      url = self.page(Page.DEVICES_PAGE),
      data = payload
    )

    devices = []
    active_devices = list(res.json()['data']['active'])
    passive_devices = list(res.json()['data']['passive'])

    if active: devices += active_devices
    if passive: devices += passive_devices

    return devices


  def logout(self) -> bool:
    payload = {
      'xhr': 1,
      'sid': self.sid,
      'logout': 1
    }

    res = requests.post(
      url = self.page(Page.LOGOUT_PAGE),
      data = payload
    )

    return res.status_code == 200
