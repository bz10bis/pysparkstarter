__version__ = "0.0.1"
__author__ = "baptiste zegre"

def load_data(context, data):
    df = context.read \
        .format("csv") \
        .options(header='true', inferSchema='true') \
        .load(data)

    return df


def analyze(_context):
    context = _context
    dataframe = load_data(context, "/home/baptiste/PycharmProjects/debat_national/data")
    print(dataframe.head())