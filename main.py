import miniupnpc

# Initialize UPnP
upnp = miniupnpc.UPnP()
try:
    upnp.discover()  # Discover UPnP-enabled devices
except Exception as e:
    if str(e) != "Success":
        raise  # Only ignore the "Success" exception

upnp.selectigd()  # Select the gateway (router)

# Get external IP address
external_ip = upnp.externalipaddress()
print(f"External IP: {external_ip}")

# Dynamically map a port (e.g., map port 8080 on your laptop to an external port)
external_port = 8080  # You can set this dynamically based on your app's need
internal_port = 8080  # The port on your laptop
internal_ip = upnp.lanaddr  # Your laptop's local IP address

# Map the port
upnp.addportmapping(external_port, 'TCP', internal_ip, internal_port, 'MyApp', '')

print(f"Port {external_port} forwarded to {internal_ip}:{internal_port}")