from blueman.services.meta import SerialService
from blueman.Sdp import DIALUP_NET_SVCLASS_ID


class DialupNetwork(SerialService):
    __svclass_id__ = DIALUP_NET_SVCLASS_ID
    __icon__ = "modem"
    __priority__ = 50
