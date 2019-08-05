
DIST_NAME = "pretty-plz"

def get_version():
  import pkg_resources
  return pkg_resources.get_distribution(DIST_NAME).version


def print_version():
  print(f"{DIST_NAME} v{get_version()}")
