# ── Type-descriptor base ────────────────────────────────────────────────────

class Descriptor:
    """Base descriptor that records the attribute name via __set_name__."""
    expected_type = object

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f'{self.name}: expected {self.expected_type.__name__}, '
                f'got {type(value).__name__}'
            )
        obj.__dict__[self.name] = value


class String(Descriptor):
    expected_type = str

class Integer(Descriptor):
    expected_type = int

class Float(Descriptor):
    expected_type = float


# ── Class decorator applied by the metaclass ────────────────────────────────

def typed(cls):
    """
    Collect all Descriptor instances declared on the class and store their
    names in cls._attributes so Structure.__setattr__ can validate them.
    """
    cls._attributes = [
        name for name, val in cls.__dict__.items()
        if isinstance(val, Descriptor)
    ]
    return cls


# ── Metaclass ────────────────────────────────────────────────────────────────

class structuretype(type):
    def __new__(mcs, name, bases, methods):
        cls = super().__new__(mcs, name, bases, methods)
        cls = typed(cls)          # apply the decorator at class-creation time
        return cls


# ── Abstract base ────────────────────────────────────────────────────────────

class Structure(metaclass=structuretype):
    """
    Base class that locks attribute assignment to declared descriptors only.
    Subclasses declare fields as class-level Descriptor instances.
    """
    def __setattr__(self, name, value):
        # Gather all declared attributes from the entire MRO
        all_attrs = set()
        for klass in type(self).__mro__:
            all_attrs.update(getattr(klass, '_attributes', []))

        if name not in all_attrs:
            raise AttributeError(f'No attribute {name!r} allowed on {type(self).__name__}')
        super().__setattr__(name, value)


# ── Concrete class ───────────────────────────────────────────────────────────

class Holding(Structure):
    name   = String()
    date   = String()
    shares = Integer()
    price  = Float()

    def __init__(self, name, date, shares, price):
        self.name   = name
        self.date   = date
        self.shares = shares
        self.price  = price

    def __repr__(self):
        return (f'Holding(name={self.name!r}, date={self.date!r}, '
                f'shares={self.shares}, price={self.price})')


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    h = Holding('ACME', '2026-07-18', 100, 490.10)
    print('Created:', h)

    # Type error — shares must be int
    print('\n[Test] Assigning a string to shares ...')
    try:
        h.shares = 'hundred'
    except TypeError as e:
        print(f'  TypeError caught: {e}')

    # Attribute error — unknown field
    print('\n[Test] Assigning to unknown attribute ...')
    try:
        h.unknown = 42
    except AttributeError as e:
        print(f'  AttributeError caught: {e}')

    print('\n_attributes on Holding:', Holding._attributes)
