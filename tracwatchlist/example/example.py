# -*- coding: utf-8 -*-
#
# Copyright (c) 2008-2010 by Martin Scharrer <martin@scharrer-online.de>
# All rights reserved.
#
# The i18n support was added by Steffen Hoffmann <hoff.st@web.de>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# For a copy of the GNU General Public License see
# <http://www.gnu.org/licenses/>.

from  trac.core                 import  *
from  tracwatchlist.api         import  BasicWatchlist, IWatchlistProvider
from  tracwatchlist.translation import  add_domain, _, N_, T_, t_, tag_, gettext


class ExampleWatchlist(Component):
    """Example watchlist provider."""
    implements( IWatchlistProvider )

    def get_realms(self):
        return ('example',)

    def get_realm_label(self, realm, plural=False):
        return plural and 'examples' or 'example'

    def res_exists(self, realm, resid):
        return True

    def res_list_exists(self, realm, reslist):
        return []

    def res_pattern_exists(self, realm, pattern):
        return True

    def has_perm(self, realm, perm):
        return True

    def get_list(self, realm, wl, req):
        user = req.authname
        examplelist = []
        query = """
          SELECT resid
            FROM watchlist
           WHERE wluser=%s AND realm='example'
        """
        parms = (user,)
        for (name,) in self.env.db_query(query, parms):
            examplelist.append({'name':name})
        return examplelist
