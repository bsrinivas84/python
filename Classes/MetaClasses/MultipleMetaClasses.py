import sys

# --- Formatter Registry ---
_formatters = {}

def register_formatter(name, cls):
    _formatters[name] = cls


# --- Metaclass: auto-registers subclasses that define a 'name' attribute ---
class TableMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        cls = super().__new__(mcs, clsname, bases, clsdict)
        if 'name' in clsdict:                        # only concrete subclasses
            register_formatter(clsdict['name'], cls)
        return cls


# --- Abstract base using the metaclass ---
class TableFormatter(metaclass=TableMeta):
    def __init__(self, outfile=None):
        self.outfile = outfile or sys.stdout

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


# --- Concrete formatters (auto-registered via metaclass) ---

class TextTableFormatter(TableFormatter):
    name = 'text'

    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)
        print('-' * (self.width + 1) * len(headers), file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(str(item), self.width), end=' ', file=self.outfile)
        print(file=self.outfile)


class CSVTableFormatter(TableFormatter):
    name = 'csv'

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    name = 'html'

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for item in rowdata:
            print('<td>{}</td>'.format(item), end='')
        print('</tr>')


# --- Factory: create a formatter by name ---
def create_formatter(name, **kwargs):
    if name not in _formatters:
        raise ValueError(f"Unknown formatter '{name}'. Available: {list(_formatters)}")
    return _formatters[name](**kwargs)


# --- Demo ---
if __name__ == '__main__':
    headers = ['Name', 'Shares', 'Price']
    rows = [
        ['ACME',  '100', '490.10'],
        ['IBM',    '50',  '91.23'],
        ['Google', '75', '1298.45'],
    ]

    for fmt_name in ('text', 'csv', 'html'):
        print(f'\n=== {fmt_name.upper()} ===')
        formatter = create_formatter(fmt_name)
        formatter.headings(headers)
        for r in rows:
            formatter.row(r)

    print(f'\nRegistered formatters: {list(_formatters.keys())}')
