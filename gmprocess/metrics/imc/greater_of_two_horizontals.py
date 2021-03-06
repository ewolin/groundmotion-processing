# third party imports
import numpy as np

# local imports
from gmprocess.metrics.exception import PGMException


def calculate_greater_of_two_horizontals(stream, **kwargs):
    """Return GREATER_OF_TWO_HORIZONTALS value for given input Stream.

    NB: The input Stream should have already been "processed",
    i.e., filtered, detrended, tapered, etc.)

    Args:
        stream (Obspy Stream): Stream containing one or Traces of
            acceleration data in gals.
        kwargs (**args): Ignored by this class.

    Returns:
        float: GREATER_OF_TWO_HORIZONTALS (float).
    """
    horizontal_vals = []
    for trace in stream:
        # Group all of the max values from traces without
        # Z in the channel name
        if 'Z' not in trace.stats['channel'].upper():
            horizontal_vals += [np.abs(trace.max())]
    if len(horizontal_vals) > 2:
        raise PGMException('More than two horizontal channels.')
    elif len(horizontal_vals) < 2:
        raise PGMException('Less than two horizontal channels.')
    greater_pgm = np.max(np.asarray(horizontal_vals))
    return greater_pgm
