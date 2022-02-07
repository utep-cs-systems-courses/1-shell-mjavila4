#! /usr/bin/env python3

import os, sys, re
from Prompt import Prompt
from Library import Library

prompt = Prompt()
Library.add('foo', Library.foo)
Library.get('foo')


