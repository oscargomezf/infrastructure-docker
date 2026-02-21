# =========================
# Stage 1 — Builder
# =========================
FROM alpine:3.23 AS builder

# System build deps:
# - build-base: gcc, g++, make, etc.
# - cmake: build system
# - git: clone libcoap
# - pkgconfig: for dependency discovery
# - openssl-dev: OpenSSL headers/libs (DTLS backend)
RUN apk add --no-cache \
      build-base cmake git pkgconfig openssl-dev

WORKDIR /src

# Clone libcoap (you can pin a tag or branch; default here is 'main')
# For options and build steps see libcoap BUILDING and install docs.
# https://github.com/obgm/libcoap/blob/develop/BUILDING
# https://libcoap.net/install.html
RUN git clone --depth=1 --branch main https://github.com/obgm/libcoap.git

WORKDIR /src/libcoap
# Out-of-source build
RUN cmake -S . -B build \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DENABLE_DTLS=ON \
      -DDTLS_BACKEND=openssl \
      -DENABLE_EXAMPLES=ON \
      -DENABLE_TESTS=OFF \
      -DENABLE_DOCS=OFF
RUN cmake --build build -j
RUN cmake --install build

# Optionally strip to reduce size (debug symbols)
RUN find /usr -type f -name "*.a" -delete && \
    find /usr -type f -name "*.so*" -exec strip --strip-unneeded {} + || true && \
    find /usr/bin -type f -exec strip --strip-all {} + || true

# =========================
# Stage 2 — Runtime
# =========================
FROM alpine:3.23 AS runtime

# Runtime deps only: OpenSSL (for DTLS) and CA bundle (if you do HTTPS/TLS)
RUN apk add --no-cache openssl ca-certificates

# Copy libcoap and installed files from the builder stage
COPY --from=builder /usr /usr

# Optional: create a non-root user to run the tools/examples
RUN addgroup -S app && adduser -S app -G app
USER app

# Expose standard CoAP ports (UDP): 5683 (CoAP) and 5684 (CoAPS/DTLS)
EXPOSE 5683/udp 5684/udp
