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
coap-server -A 0.0.0.0 -p 5683 -k mysecretpassword -u myidentity -V 5684 -v 7
```

### Example coap-client

```bash
docker run --rm oscargomezf/libcoap-alpine:openssl coap-client -m get coap://ip_address/time
```

### Example coap-client

```bash
docker run --rm libcoap-alpine:openssl oscargomezf/coap-client  -m post coap://ip_address/new_resource -e "Hello, world!"
docker run --rm libcoap-alpine:openssl oscargomezf/coap-client -m get coap://ip_address/new_resource
Hello, world!
```

