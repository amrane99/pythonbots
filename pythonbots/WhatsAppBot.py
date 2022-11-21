# ------------------------------------------------------------------------------
# WhatsApp bot to pass messages about the training, or inform when experiments 
# are done.
# ------------------------------------------------------------------------------

import pywhatkit

class WhatsAppBot():
    r"""Initialize a WhatsApp Bot"""
    def __init__(self, group_id):
        r"""Provide group id to send a message to"""
        self.group_id = group_id

    def send_msg(self, msg):
        r"""Send a message in string form"""
        pywhatkit.sendwhatmsg_to_group_instantly(self.group_id, msg, wait_time=7, tab_close=True, close_time=0)