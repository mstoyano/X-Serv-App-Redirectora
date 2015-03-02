#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class Serv_Redirect(webapp.webApp):

    def process(self, parsedRequest):

        rand = str(random.randint(0, 10000000))
        Answ = '<html><head><meta http-equiv="Refresh" content="3; url='
        Answ = Answ + rand + '"/>' + '<body>This is a redirection to: '
        Answ = Answ + '<b>http://localhost:1234/' + rand + '</b></body></html>'

        return("307 Temporary Redirect", Answ)

if __name__ == "__main__":
    serv = Serv_Redirect("localhost", 1234)
