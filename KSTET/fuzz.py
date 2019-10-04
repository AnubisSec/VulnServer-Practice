from boofuzz import *

host = "10.10.10.147"
port = 9999



def main():
	session = Session(target = Target(connection = SocketConnection(host, port , proto='tcp')), sleep_time=4)

	s_initialize("KSTET")

	s_string("KSTET", fuzzable = False)
	s_delim(" ", fuzzable = False)
	s_string("BLAH")

	session.connect(s_get("KSTET"))
	session.fuzz()


if __name__ == "__main__":
	main()