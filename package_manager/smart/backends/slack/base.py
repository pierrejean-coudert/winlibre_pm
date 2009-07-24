#
# Copyright (c) 2004 Conectiva, Inc.
#
# Written by Gustavo Niemeyer <niemeyer@conectiva.com>
#
# This file is part of Smart Package Manager.
#
# Smart Package Manager is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# Smart Package Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Smart Package Manager; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
from smart.backends.slack.pm import SlackPackageManager
from slackver import checkdep, vercmp, splitrelease
from smart.util.strtools import isGlob
from smart.cache import *
import fnmatch
import string
import os, re

__all__ = ["SlackPackage", "SlackProvides", "SlackUpgrades"]

class SlackPackage(Package):

    __slots__ = ()

    packagemanager = SlackPackageManager

    def coexists(self, other):
        if not isinstance(other, SlackPackage):
            return True
        return False

    def matches(self, relation, version):
        if not relation:
            return True
        return checkdep(self.version, relation, version)

    def search(self, searcher):
        myname = self.name
        myversion = self.version
        ratio = 0
        ic = searcher.ignorecase
        for nameversion, cutoff in searcher.nameversion:
            _, ratio1 = globdistance(nameversion, myname, cutoff, ic)
            _, ratio2 = globdistance(nameversion,
                                     "%s-%s" % (myname, myversion), cutoff, ic)
            _, ratio3 = globdistance(nameversion, "%s-%s" %
                                     (myname, splitrelease(myversion)[0]),
                                     cutoff, ic)
            ratio = max(ratio, ratio1, ratio2, ratio3)
        if ratio:
            searcher.addResult(self, ratio)

    def __lt__(self, other):
        rc = cmp(self.name, other.name)
        if type(other) is SlackPackage:
            if rc == 0 and self.version != other.version:
                rc = vercmp(self.version, other.version)
        return rc == -1

class SlackProvides(Provides): __slots__ = ()

class SlackDepends(Depends):

    __slots__ = ()

    def matches(self, prv):
        if not isinstance(prv, SlackProvides) and type(prv) is not Provides:
            return False
        if not self.version or not prv.version:
            return True
        return checkdep(prv.version, self.relation, self.version)

class SlackUpgrades(SlackDepends,Upgrades): __slots__ = ()

def enablePsyco(psyco):
    psyco.bind(SlackPackage.coexists)
    psyco.bind(SlackPackage.matches)
    psyco.bind(SlackPackage.search)
    psyco.bind(SlackPackage.__lt__)
    psyco.bind(SlackDepends.matches)

hooks.register("enable-psyco", enablePsyco)

# vim:ts=4:sw=4:et
