
class Timekeeper(object):
    def __init__(self, echo=False):
        self.points = list()
        self.echo = echo
        self._active = False

    def start(self):
        self._active = True
        self.mark('Timekeeper started', 'hidden')

    def finish(self, show_summ=False):
        self._false = True
        self.mark('Timekeeper finished', 'hidden')
        if show_summ:
            self.summarize()

    def mark(self, desc=None, label='default'):
        assert self._active
        self.points.append(Timepoint(desc, label))
        if self.echo and label != 'hidden':
            print("{} - {}".format(self.points[-1].dt, desc))

    def summarize(self, label=None, showall=False):
        if label is not None:
            pts = [p for p in self.points if p.label in [label, 'hidden']]
        else:
            pts = self.points

        prev = pts[0]
        for p in pts:
            if p.label != 'hidden' or showall:
                print("{}  -  {} (total: {})  -  {}  -  {}".format(
                    p.dt,
                    p.dt - prev.dt,
                    p.dt - pts[0].dt,
                    p.desc,
                    p.label
                ))
            prev = p


class Timepoint(object):
    def __init__(self, desc=None, label=None):
        self.value = time.time()
        self.desc = desc
        self.label = label
        self._dt = None

    @property
    def dt(self):
        if self._dt is None:
            self._dt = datetime.datetime.fromtimestamp(self.value)
        return self._dt

    def __repr__(self):
        return "<Timepoint value={} desc={} label={}>".format(self.value, self.desc, self.label)
