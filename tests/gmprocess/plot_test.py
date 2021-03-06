#!/usr/bin/env python

# stdlib imports
import os.path
import matplotlib

# third party imports
from gmprocess.io.read import read_data
from gmprocess.plot import plot_arias, plot_durations, plot_moveout
from gmprocess.io.test_utils import read_data_dir


def test_plot():
    # read in data
    datafiles, _ = read_data_dir('cwb', 'us1000chhc')
    streams = []
    for filename in datafiles:
        streams += read_data(filename)
    # One plot arias
    axes = plot_arias(streams[3])
    assert len(axes) == 3

    # Multiplot arias
    axs = matplotlib.pyplot.subplots(len(streams), 3, figsize=(15, 10))[1]
    axs = axs.flatten()
    idx = 0
    for stream in streams:
        axs = plot_arias(
            stream, axes=axs, axis_index=idx, minfontsize=15,
            show_maximum=False, title="18km NNE of Hualian, Taiwan")
        idx += 3

    # One plot durations
    durations = [(0.05, 0.75),
                 (0.2, 0.8),
                 (0.05, .95)]
    axes = plot_durations(streams[3], durations)
    assert len(axes) == 3

    # Multiplot durations
    axs = matplotlib.pyplot.subplots(len(streams), 3, figsize=(15, 10))[1]
    axs = axs.flatten()
    idx = 0
    for stream in streams:
        axs = plot_durations(
            stream, durations, axes=axs, axis_index=idx,
            minfontsize=15, title="18km NNE of Hualian, Taiwan")
        idx += 3

    # Moveout plots
    epicenter_lat = 24.14
    epicenter_lon = 121.69
    plot_moveout(streams, epicenter_lat, epicenter_lon, 'BN1',
                 cmap='nipy_spectral_r', figsize=(15, 10), minfontsize=16,
                 normalize=True, scale=10)


if __name__ == '__main__':
    os.environ['CALLED_FROM_PYTEST'] = 'True'
    test_plot()
