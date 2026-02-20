#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# /**
#  * @file script.py
#  * @author Oscar Gomez Fuente <oscargomezf@gmail.com>
#  * @modified Oscar Gomez Fuente <oscargomezf@gmail.com>
#  * @date 2025-01-18 19:07:53 
#  * @version 0cbec51
#  * @section DESCRIPTION
#  *     Script example for testing Dockerfile.
#  */
# -----------------------------------------------------------------------------

import sys
import platform
import os

def main():
	print("[INFO] script.py is running inside the container 🎉")
	print("------------------------------------------------------------")
	print(f"[INFO] Python version: {sys.version.split()[0]}")
	print(f"[INFO] OS: {platform.system()} {platform.release()}")
	print(f"[INFO] Current working directory: {os.getcwd()}")
	print("Directory contents:")
	for f in os.listdir("."):
		print(" -", f)

if __name__ == "__main__":
	main()
