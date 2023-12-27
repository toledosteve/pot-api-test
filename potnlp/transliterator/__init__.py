from .base import Transliterator
from .mappings import Mappings

__version__ = "0.1.0"
__all__ = [Transliterator]

WNALP_LWS = Mappings.wnalp_to_lws.value
LWS_WNALP = Mappings.lws_to_wnalp.value
BWAKA_WNALP = Mappings.bwaka_to_wnalp.value

