# Pretf

Pretf is a tool for generating Terraform configuration with Python. This is Infrastructure as Code, not Infrastructure as Configuration Language!

Terraform is good at managing resources, and the configuration language HCL is quite nice, but it is very easy to run into limitations of that language. Luckily, Terraform also supports configuration as JSON files. Pretf allows you to write Python code, with for-loops and everything, that outputs simple JSON files for Terraform to use.

## Overview

Here is what happens when you run `pretf`:

1. It loads `pretf.json` from the current directory, containing configuration such as:
  * `source` - set this to load files from directories other than the current directory, otherwise the current directory is used
  * `remove` - set this to clean up old files (e.g. delete previously generated `*.tf.json` files)
  * `params` - set this to pass parameters into the Python functions
2. It imports `*.tf.py` files, runs the `main()` function, and writes the result to `*.tf.json`
3. It runs `terraform` with any provided command line arguments

This works as a transparent wrapper for Terraform. Your python code generates the Terraform configuration and then Terraform uses it.

## Project status

This is in very early development. Things are not yet implemented. The API is likely to change as I experiment with different use-cases and try things out.
