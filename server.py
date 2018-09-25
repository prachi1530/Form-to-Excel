from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import time
import pandas as pd
import ast
import pdb


class S(BaseHTTPRequestHandler):
	def get_df(self):
		try:
			df = pd.read_excel("mainDatabase.xlsx")
		except:
			df = pd.DataFrame(columns=['Email'])
		return df

	def process_data(self, data):
		try:
			df = self.get_df()
			data = ast.literal_eval(data)
			email = data['email']
			df.loc[len(df)] = [email]
			df.to_excel("mainDatabase.xlsx",index = False)
			return True
		except:
			print "Error processing data!"
			return False

	def verify_email(self, data):
		try:
			data = ast.literal_eval(data)
			email = data['email']
			df = self.get_df()
			email_list = list(df['Email'])
			if email_list:
				if email in email_list:
					return True
			return False
		except:
			print "Error in verifying email!"
			return False

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		self.wfile.write("<html><body><h1>Server Started!!!</h1></body></html>")

	def do_HEAD(self):
		self._set_headers()

	def do_POST(self):
		response_status = -1
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		email_verification = self.verify_email(post_data)
		print "email_verification:", email_verification
		if email_verification:
			response_status = 0
		elif not email_verification:
			save_data = self.process_data(post_data)
			print "save_data:", save_data
			if save_data:
				response_status = 1
		self._set_headers()
		self.wfile.write(str(response_status))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Server started...")
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
