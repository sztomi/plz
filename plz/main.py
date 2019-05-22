import sys

from pathlib import Path

from plz.env import Env


def find_command(command):
  spath = Path(Env.scripts_path())
  command = Path(command)
  to_try = (
    spath / command,
    spath / (str(command) + ".py"),
    spath / (str(command) + ".cmd"),
    spath / (str(command) + ".exe"),
    spath / (str(command) + ".bat"),
  )
  for item in to_try:
    if item.exists():
      if item.suffix == ".py":
        return sys.executable, str(item)
      else:
        return (str(item),)
  raise RuntimeError(f"Could not find command {command}")


def main():
  if Env.scripts_path() == None:
    print("ERROR: set $PLZ_SCRIPTS_PATH!")
    sys.exit(1)

  from argparse import ArgumentParser, REMAINDER
  parser = ArgumentParser()
  parser.add_argument("command")
  parser.add_argument("cli", nargs=REMAINDER)
  args = parser.parse_args()

  command = find_command(args.command)
  import subprocess
  proc = subprocess.run([*command, *args.cli])
  sys.exit(proc.returncode)

