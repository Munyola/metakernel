# Copyright (c) Metakernel Development Team.
# Distributed under the terms of the Modified BSD License.

from metakernel import Magic, option


class PlotMagic(Magic):

    @option(
        '-s', '--size', action='store',
        help='Pixel size of plots, "width,height"'
    )
    @option(
        '-f', '--format', action='store', default='png',
        help='Plot format (png, svg or jpg).'
    )
    @option(
        '-b', '--backend', action='store', default='inline',
        help='Backend selection'
    )
    @option(
        '-r', '--resolution', action='store', default=96,
        help='Resolution in pixels per inch'
    )
    def line_plot(self, backend=None, size=None, format=None, resolution=96):
        """
        %plot [options] backend - configure plotting for the session.

        This line magic will configure the plot settings for this
        language.

        Examples:
            %plot --backend=qt --format=png
            %plot -b inline -s 640,480

        Note: not all languages may support the %plot magic, and not all
        options may be supported.
        """
        self.kernel.update_plot_settings(backend, size, format, resolution)
        self.kernel.handle_plot_settings()


def register_magics(kernel):
    kernel.register_magics(PlotMagic)
