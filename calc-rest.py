#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import socket


class calcServ(webapp.webApp):

    def parse(self, request):
        verb = request.split()[0]
        res = request.split()[1].split("/")[1]
        body = request.split()[-1]
        return(verb, res, body)

    def process(self, parsedRequest):
        (verb, res, body) = parsedRequest
        result = 0
        if (verb == "PUT"):
            self.oper = body
            return ("200 OK", "<html><body>Recibido: "
                    + body + "</body></html>")
        elif (verb == "GET"):
            try:
                if (len(self.operacion.split('+')) == 2):
                    result = (int(self.operacion.split("+")[0]) +
                              int(self.operacion.split("+")[1]))
                elif (len(self.operacion.split('-')) == 2):
                    result = (int(self.operacion.split("-")[0]) -
                              int(self.operacion.split("-")[1]))
                elif (len(self.operacion.split('*')) == 2):
                    result = (int(self.operacion.split("*")[0]) *
                              int(self.operacion.split("*")[1]))
                elif (len(self.operacion.split('/')) == 2):
                    result = (int(self.operacion.split("/")[0]) /
                              int(self.operacion.split("/")[1]))
                    return ("200 OK",
                            "<html><body>Resultado: " +
                            str(result) + "</body></html>")
            except ValueError:
                    return ("404 Not Found",
                            "<html><body>Valores incorrectos</body></html>")
            except AttributeError:
                    return ("404 Not Found",
                            "<html><body> Sin datos previos</body></html>")

if __name__ == "__main__":
    testsCalc = calcServ("localhost", 1234)
