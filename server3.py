import socket

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5001

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))

    while True:
  # Path to the uptime data file (modify as needed)
      DATA_FILE_PATH = "/home/ubuntu/uptime_data.tsv"
# Open the uptime data file

      data = []
      with open(DATA_FILE_PATH, 'r') as file:
          
          for line in file:
              
      # Split the line based on the tab delimiter
              data.append(line.strip().split('\t'))


# Example usage


# Access data
# Access the timestamp and uptime elements
      timestamp, uptime = data[1]

# Concatenate the formatted string
      output_string = "Timestamp: " + timestamp + ", Uptime: " + uptime
      data, addr = server.recvfrom(1024)
      data = data.decode("utf-8")
      print(data)

      if data == "!EXIT":
          print("Client disconnected.")
          break

      print(f"Client: {data}")

      data = data.upper()
      data = data.encode("utf-8")
      server.sendto(output_string.encode("utf-8"), addr)