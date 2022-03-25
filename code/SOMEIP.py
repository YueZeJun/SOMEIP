from scapy.all import *
from scapy.fields import *
from scapy.packet import *

"""SOMEIP PACKAGE DEFINITION"""


class _SOMEIP_MessageId(Packet):
    """MessageId subpacket."""
    name = 'MessageId'
    fields_desc = [
        # Service ID
        ShortField('srv_id', 0),
        # identify it is a method or event
        BitEnumField('sub_id', 0, 1, {0: 'METHOD_ID', 1: 'EVENT_ID'}),
        # the RPC call to a method of an application
        ConditionalField(BitField('method_id', 0, 15), lambda pkt: pkt.sub_id == 0),
        # identify an event
        ConditionalField(BitField('event_id', 0, 15), lambda pkt: pkt.sub_id == 1)
    ]

    def extract_padding(self, p):
        return '', p


class _SOMEIP_RequestId(Packet):
    """ RequestId subpacket."""
    name = 'RequestId'
    fields_desc = [
        ShortField('client_id', 0),
        ShortField('session_id', 0)]

    # In case Session Handling is not active, the Session ID shall be set to 0x00
    # When the Session ID reaches 0xFFFF, it shall start with 0x0001 again.

    def extract_padding(self, p):
        return '', p


class SOMEIP(Packet):
    """ SOME/IP Packet."""
    # Default values
    PROTOCOL_VERSION = 0x01
    INTERFACE_VERSION = 0x01

    # Lenght offset (without payload)
    LEN_OFFSET = 0x08

    # SOME/IP TYPE VALUES
    TYPE_REQUEST = 0x00  # A request expecting a response
    TYPE_REQUEST_NO_RET = 0x01  # A fire&forget request
    TYPE_NOTIFICATION = 0x02  # A request of a notification/event callback expecting no response
    TYPE_REQUEST_ACK = 0x40  # Acknowledgment for REQUEST
    TYPE_REQUEST_NO_RET_ACK = 0x41  # Acknowledgment for REQUEST_NO_RETURN (informational)
    TYPE_NOTIFICATION_ACK = 0x42  # Acknowledgment for NOTIFICATION (informational)
    TYPE_RESPONSE = 0x80  # The response message
    TYPE_ERROR = 0x81  # The response containing an error
    TYPE_RESPONSE_ACK = 0xc0  # The Acknowledgment for RESPONSE (informational)
    TYPE_ERROR_ACK = 0xc1  # Acknowledgment for ERROR (informational)

    # SOME/IP-TP TYPE VALUES
    TYPE_REQUEST_SEGMENT = 0x20  # A TP request expecting a response (even void)
    TYPE_REQUEST_NO_RET_SEGMENT = 0x21  # A TP fire&forget request
    TYPE_NOTIFICATION_SEGMENT = 0x22  # A TP request of a notification/event callback expecting no response
    TYPE_RESPONSE_SEGMENT = 0xa0  # The TP response message
    TYPE_ERROR_SEGMENT = 0xa1  # The TP response containing an error
    SOMEIP_TP_TYPES = frozenset({TYPE_REQUEST_SEGMENT, TYPE_REQUEST_NO_RET_SEGMENT, TYPE_NOTIFICATION_SEGMENT,
                                 TYPE_RESPONSE_SEGMENT, TYPE_ERROR_SEGMENT})
    # The 3rd highest bit of the Message Type (=0x20) shall be called TP-Flag and shall be set to 1 to signal
    # that the current SOME/IP message is a segment
    SOMEIP_TP_TYPE_BIT_MASK = 0x20

    # PS :
    # For all messages an optional acknowledgment (ACK) exists. These care defined for
    # transport protocols (i.e. UDP) that do not acknowledge a received message. ACKs
    # are only transported when the interface specification requires it. Only the usage of the
    # REQUEST_ACK is currently specified in this document. All other ACKs are currently
    # informational and do not need to be implemented

    # SOME/IP RETURN CODES
    # Message Type Allowed Return Codes
    # REQUEST N/A set to 0x00 (E_OK)
    # REQUEST_NO_RETURN N/A set to 0x00 (E_OK)
    # NOTIFICATION N/A set to 0x00 (E_OK)
    # RESPONSE See Return Codes in [TR_SOMEIP_00191]
    # ERROR See Return Codes in [TR_SOMEIP_00191]. Shall not be 0x00 (E_OK)
    RET_E_OK = 0x00  # No error occurred
    RET_E_NOT_OK = 0x01  # An unspecified error occurred
    RET_E_UNKNOWN_SERVICE = 0x02  # The requested Service ID is unknown
    RET_E_UNKNOWN_METHOD = 0x03  # The requested Method ID is unknown. Service ID is known.
    RET_E_NOT_READY = 0x04  # Service ID and Method ID are known. Application not running.
    RET_E_NOT_REACHABLE = 0x05  # System running the service is not reachable (internal error code only)
    RET_E_TIMEOUT = 0x06  # A timeout occurred (internal error code only).
    RET_E_WRONG_PROTOCOL_V = 0x07  # Version of SOME/IP protocol not supported
    RET_E_WRONG_INTERFACE_V = 0x08  # Interface version mismatch
    RET_E_MALFORMED_MSG = 0x09  # eserialization error, so that payload cannot be deserialized.
    RET_E_WRONG_MESSAGE_TYPE = 0x0a  # An unexpected message type was received (e.g. REQUEST_NO_RETURN for a method defined as REQUEST.)
    RET_E_E2E_REPEATED = 0x0b  # Repeated E2E calculation error
    RET_E_E2E_WRONG_SEQUENCE = 0x0c  # Wrong E2E sequence error
    RET_E_E2E = 0x0d  # Not further specified E2E error
    RET_E_E2E_NOT_AVAILABLE = 0x0e  # E2E not available
    RET_E_E2E_NO_NEW_DATA = 0x0f  # No new data for E2E calculation present.

    # SOME/IP-TP More Segments Flag
    SOMEIP_TP_LAST_SEGMENT = 0
    SOMEIP_TP_MORE_SEGMENTS = 1

    _OVERALL_LEN_NOPAYLOAD = 16  # UT

    name = 'SOME/IP'

    fields_desc = [
        PacketField('msg_id', _SOMEIP_MessageId(), _SOMEIP_MessageId),  # MessageID
        IntField('len', None),
        # Length   contain the length in Byte starting from Request  until the end of the SOME/IP message
        PacketField('req_id', _SOMEIP_RequestId(), _SOMEIP_RequestId),  # RequestID
        ByteField('proto_ver', PROTOCOL_VERSION),  # Protocol version
        ByteField('iface_ver', INTERFACE_VERSION),  # Interface version
        ByteEnumField('msg_type', TYPE_REQUEST, {  # -- Message type --
            TYPE_REQUEST: 'REQUEST',  # 0x00
            TYPE_REQUEST_NO_RET: 'REQUEST_NO_RETURN',  # 0x01
            TYPE_NOTIFICATION: 'NOTIFICATION',  # 0x02
            TYPE_REQUEST_ACK: 'REQUEST_ACK',  # 0x40
            TYPE_REQUEST_NO_RET_ACK: 'REQUEST_NO_RETURN_ACK',  # 0x41
            TYPE_NOTIFICATION_ACK: 'NOTIFICATION_ACK',  # 0x42
            TYPE_RESPONSE: 'RESPONSE',  # 0x80
            TYPE_ERROR: 'ERROR',  # 0x81
            TYPE_RESPONSE_ACK: 'RESPONSE_ACK',  # 0xc0
            TYPE_ERROR_ACK: 'ERROR_ACK',  # 0xc1
            TYPE_REQUEST_SEGMENT: 'TP_REQUEST',  # 0x20
            TYPE_REQUEST_NO_RET_SEGMENT: 'TP_REQUEST_NO_RETURN',  # 0x21
            TYPE_NOTIFICATION_SEGMENT: 'TP_NOTIFICATION',  # 0x22
            TYPE_RESPONSE_SEGMENT: 'TP_RESPONSE',  # 0xa0
            TYPE_ERROR_SEGMENT: 'TP_ERROR',  # 0xa1
        }),
        ByteEnumField('retcode', 0, {  # -- Return code --
            RET_E_OK: 'E_OK',  # 0x00
            RET_E_NOT_OK: 'E_NOT_OK',  # 0x01
            RET_E_UNKNOWN_SERVICE: 'E_UNKNOWN_SERVICE',  # 0x02
            RET_E_UNKNOWN_METHOD: 'E_UNKNOWN_METHOD',  # 0x03
            RET_E_NOT_READY: 'E_NOT_READY',  # 0x04
            RET_E_NOT_REACHABLE: 'E_NOT_REACHABLE',  # 0x05
            RET_E_TIMEOUT: 'E_TIMEOUT',  # 0x06
            RET_E_WRONG_PROTOCOL_V: 'E_WRONG_PROTOCOL_VERSION',  # 0x07
            RET_E_WRONG_INTERFACE_V: 'E_WRONG_INTERFACE_VERSION',  # 0x08
            RET_E_MALFORMED_MSG: 'E_MALFORMED_MESSAGE',  # 0x09
            RET_E_WRONG_MESSAGE_TYPE: 'E_WRONG_MESSAGE_TYPE',  # 0x0a
            RET_E_E2E_REPEATED: 'E_E2E_REPEATED',  # 0x0b
            RET_E_E2E_WRONG_SEQUENCE: 'E_E2E_WRONG_SEQUENCE',  # 0x0c
            RET_E_E2E: 'E_E2E',  # 0x0d
            RET_E_E2E_NOT_AVAILABLE: 'E_E2E_NOT_AVAILABLE',  # 0x0e
            RET_E_E2E_NO_NEW_DATA: 'E_E2E_NO_NEW_DATA',  # 0x0f
        }),
        # The Offset field shall be set to the offset n bytes of the transported segment in the original message
        # Please be aware that the value provided within the Offset Field is given in units of 16 bytes
        # The Offset Value of 87 correspond to 1392 bytes Payload.
        ConditionalField(BitField('offset', 0, 28), lambda pkt: pkt.msg_type in SOMEIP.SOMEIP_TP_TYPES),
        ConditionalField(BitField('reserved', 0, 3), lambda pkt: pkt.msg_type in SOMEIP.SOMEIP_TP_TYPES),
        # The More Segments Flag shall be set to 1 for all segments but the last segment.
        # For the last segment it shall be set to 0.
        ConditionalField(BitEnumField('more_segments', 0, 1, {SOMEIP_TP_LAST_SEGMENT: 'Last_Segment',
                                                              SOMEIP_TP_MORE_SEGMENTS: 'More_Segments'
                                                              }), lambda pkt: pkt.msg_type in SOMEIP.SOMEIP_TP_TYPES)
    ]

    def post_build(self, p, pay):
        length = self.len
        # length computation : RequestID + PROTOVER_IFACEVER_TYPE_RETCODE + PAYLOAD
        if length is None:
            length = self.LEN_OFFSET + len(pay)
            p = p[:4] + struct.pack('!I', length) + p[8:]
        return p + pay
