from math import sqrt

from kivy.lang import Builder
from kivy.metrics import Metrics
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
    """
<ScreenSandBox>
    size_hint: None, None
    size:
        [ \
            self.screen_width * self.scale, \
            self.screen_height * self.scale \
        ]

    """
)


class ScreenSandBox(BoxLayout):
    """
    The size of the layout is calculated automatically
    based on screen ratio and scale
    """

    diagonal_inches = NumericProperty()
    """
    screen diagonal size in inches
    """
    screen_width = NumericProperty()
    """
    screen width in pixel
    """
    screen_height = NumericProperty()
    """
    screen height in pixel
    """
    scale = NumericProperty(1)
    """
    use scale to change the size of the layout. default is 1
    """

    _default_dpi = None
    _default_density = None
    _default_fontscale = None

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._default_dpi = Metrics.dpi
        self._default_density = Metrics.density
        self._default_fontscale = Metrics.fontscale

    def __enter__(self):
        density = self.fakeDensity()
        dpi = self.fakeDpi()
        fontscale = 1
        self.set_metrics(density, dpi, fontscale)
        return self

    def __exit__(self, *args):
        self.revert_metrics()

    def set_metrics(self, density=None, dpi=None, fontscale=None):
        """
        changes the density, dpi and fontscale in MetricsBase
        """
        if density:
            Metrics.density = density
        if dpi:
            Metrics.dpi = dpi
        if fontscale:
            Metrics.fontscale = fontscale

    def revert_metrics(self):
        """
        reverts density, dpi and fontscale to default values
        """
        Metrics.density = self._default_density
        Metrics.dpi = self._default_dpi
        Metrics.fontscale = self._default_fontscale

    def ratio(self):
        """
        screen ratio
        """
        return self.screen_width / self.screen_height

    def physical_size(self):
        """
        physical size of the screen in inch
        """
        ratio = self.ratio()
        diagonal = self.diagonal_inches
        idx = sqrt(diagonal ** 2 / (ratio ** 2 + 1))
        size = (idx * ratio, idx)
        return size

    def diagonal_px(self):
        """
        diagonal screen size in pixel
        """
        return sqrt(self.screen_width ** 2 + self.screen_height ** 2)

    def dpi(self):
        """
        screen dpi
        """
        return self.diagonal_px() / self.diagonal_inches

    def density(self):
        """
        screen density
        """
        return self.dpi() / 96

    def fakeDensity(self):
        """
        new density in scaled screen
        """
        real_density = self.density()
        real_width = self.screen_width
        fake_width = self.width
        return (fake_width * real_density) / real_width

    def fakeDpi(self):
        """
        new dpi in scaled screen
        """
        real_dpi = self.dpi()
        real_width = self.screen_width
        fake_width = self.width
        return (fake_width * real_dpi) / real_width
