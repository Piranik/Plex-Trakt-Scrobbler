import sys


import m_sync
sys.modules['interface.m_sync'] = m_sync

import m_main
sys.modules['interface.m_main'] = m_main

import resources
sys.modules['interface.resources'] = resources
