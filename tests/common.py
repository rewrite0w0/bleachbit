# vim: ts=4:sw=4:expandtab

## BleachBit
## Copyright (C) 2009 Andrew Ziem
## http://bleachbit.sourceforge.net
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.



"""
Common code for unit tests
"""



import os



def destructive_tests(title):
    """Return true if allowed to run destructive tests.  If false print notice."""
    if os.getenv('DESTRUCTIVE_TESTS') == 'T':
        return True
    print 'warning: skipping test(s) for %s because env. var. DESTRUCTIVE_TESTS not set' % title
    return False
