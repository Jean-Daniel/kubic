import logging
import sys
from logging import StreamHandler

import pykapi.cli

if __name__ == "__main__":
    logging.root.addHandler(StreamHandler(sys.stderr))
    logging.root.setLevel(logging.INFO)
    pykapi.cli.main()
