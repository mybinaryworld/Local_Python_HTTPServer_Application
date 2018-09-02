
import json
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer


class GetHandler(BaseHTTPRequestHandler):

    server = None

    def do_GET(self):
        """
        Manage post requests
        :return:
        """
        parsed_path = urlparse.urlparse(self.path)
        print "parsed_path:", parsed_path
        query_dict = {}
        query_string = parsed_path.query
        if query_string is not "":
            if query_string.__contains__("&"):
                query_list = query_string.split("&")
                for var in query_list:
                    if str(var).__contains__("="):
                        qparam = var.strip().split("=")
                        if len(qparam ) >1:
                            query_dict[qparam[0] ] =qparam[1]
            elif not query_string.__contains__("&") and not query_string.__contains__("="):
                qparam = query_string.strip().split("=")
                if len(qparam ) >1:
                    query_dict[qparam[0]] = qparam[1]

        client_values = {"client_address" :self.client_address, "headers" :self.headers, "command" :self.command, "path" :self.path,
                         "real_path" :parsed_path.path, "query" :query_dict, "request_version" :self.request_version}

        server_values = {"server_version" :self.server_version, "sys_version" :self.server_version, "protocol_version" :self.protocol_version}
        message = {"client_values": client_values, "server_values" :server_values}

        self.send_response(200)
        self.end_headers()

        # Here you can use switch case to distribute api data to different classes
        print message
        return


    def do_POST(self):
        """
        Manage post requests
        """
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        data = json.loads(post_body)
        print data
        return




    @staticmethod
    def start(hostname="", port=""):
        """
        This method starts the server as an application
        :param hostname: localhost, or your IPAddress
        :param port: Port you want your server to run on, default = 8082
        :return: Prints success/failure message
        """
        if GetHandler.server is not None:
            print "Server is already running ..."


        if hostname is not None and port is not 0:
            try:
                GetHandler.server = HTTPServer((hostname, port), GetHandler)
                print 'Starting server at http://%s:%s' % (hostname ,port)
                GetHandler.server.serve_forever()
            except Exception, e:
                print e.message



if __name__ == '__main__':

    GetHandler.start(hostname = "localhost", port= 8082)
