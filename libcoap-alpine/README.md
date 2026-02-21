## libcoap OpenSSL Alpine Image

This Docker image provides a lightweight build of libcoap, a C implementation of the Constrained Application Protocol (CoAP, RFC 7252), compiled from source on Alpine Linux with DTLS/TLS support via OpenSSL. libcoap is designed for constrained IoT environments and supports standards such as resource observation, block-wise transfers, PATCH/FETCH, CoAP over TCP/TLS/WebSockets, OSCORE, and other protocol extensions.

The library is widely used for CoAP-based client/server development and runs on both embedded systems and POSIX platforms.  It also includes CLI utilities such as coap-client, coap-server, and coap-rd for testing and interoperability.

### Features

- Multi-stage build (builder → minimal runtime).
- Based on Alpine 3.23.
- Compiled with:
  - -DENABLE_DTLS=ON
  - -DDTLS_BACKEND=openssl
  - Examples, tests, and docs disabled for smaller footprint.
- Includes OpenSSL and CA certificates.
- Provides libcoap shared libraries and CLI tools.
- Runs as a non‑root user.
- Default command: coap-client -h

### Use cases

- Developing and testing CoAP client/server applications.
- IoT, embedded systems and constrained-node environments.
- DTLS-secured CoAP communication.
- CI environments requiring a ready-to-use CoAP toolset

### Building the Docker Image

You can build the Docker image using either Docker Compose or the Docker CLI.

#### Using Docker CLI

```sh
# Build the image directly with Docker
# Run this command from the libcoap-alpine directory
# The -t flag sets the image name (e.g., 'libcoap-alpine:latest')
docker build -t libcoap-alpine:latest .
```

#### Using Docker Compose

```sh
# Build the image defined in compose/docker-compose.yml
# Run this command from the libcoap-alpine directory
cd compose
# This will build the 'libcoap' image using the Dockerfile in the parent directory
# The image will be tagged as 'libcoap-alpine_libcoap' by default
# (You can override the tag with the --tag option if needed)
docker compose build
```

### Example coap-server

```bash
$ docker run --rm -p 5683:5683/udp libcoap-alpine:openssl coap-server -A 0.0.0.0 -p 5683 -v 7
```

### Example coap-server CoAPS with PSK

```bash
docker run --rm -p 5683:5683/udp -p 5684:5684/udp oscargomezf/libcoap-alpine:openssl \
coap-server -A 0.0.0.0 -p 5683 -k mysecretpassword -i /config/psk-identity-map.txt -V 7 -v 7
```

### Examples CoAP coap-client

```bash
docker exec -it libcoap-alpine-runtime coap-client -m get coap://localhost/.well-known/core -v 7
</> General Info
	ct:	0
</async>
	ct:	0
</example_data> Example Data
	ct:	0
	obs:	
</time> Internal Clock
	rt:	ticks
	if:	clock
	ct:	0
	obs:	
```

```bash
docker exec -it libcoap-alpine-runtime coap-client -m get coap://localhost/time
Feb 21 14:54:39
```

```bash
docker exec -it libcoap-alpine-runtime coap-client -m post coap://localhost/new_resource -e "Hello, world!"
docker exec -it libcoap-alpine-runtime coap-client -m get coap://localhost/new_resource
Hello, world!
```

### Examples CoAPs coap-client

```bash
docker exec -it libcoap-alpine-runtime coap-client -m get -u sensor-1 -k a7f3c19d52e48b0fa9c4e2317bd08e6f coaps://localhost/.well-known/core -v 7
</> General Info
	ct:	0
</async>
	ct:	0
</example_data> Example Data
	ct:	0
	obs:	
</time> Internal Clock
	rt:	ticks
	if:	clock
	ct:	0
	obs:	
```

```bash
docker exec -it libcoap-alpine-runtime coap-client -m get -u sensor-1 -k a7f3c19d52e48b0fa9c4e2317bd08e6f coaps://localhost/time
Feb 21 14:54:39
```

```bash
docker exec -it libcoap-alpine-runtime coap-client -m post -u sensor-1 -k a7f3c19d52e48b0fa9c4e2317bd08e6f coaps://localhost/new_resource -e "Hello, world!"
docker exec -it libcoap-alpine-runtime coap-client -m get -u sensor-1 -k a7f3c19d52e48b0fa9c4e2317bd08e6f coaps://localhost/new_resource
Hello, world!
```
