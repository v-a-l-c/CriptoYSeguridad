FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    dsniff tcpdump tshark iproute2 iputils-ping dnsmasq curl \
    net-tools ca-certificates procps vim-tiny iptables dnsutils \
    python3 unzip \
    && rm -rf /var/lib/apt/lists/*

# bettercap (binario oficial; se usa SOLO para dns.spoof)
RUN curl -sL https://github.com/bettercap/bettercap/releases/latest/download/bettercap_linux_amd64.zip -o /tmp/bc.zip \
    && unzip -o /tmp/bc.zip -d /usr/local/bin/ && rm /tmp/bc.zip \
    && apt-get update && apt-get install -y --no-install-recommends \
    libusb-1.0-0 libnetfilter-queue1 libpcap0.8 \
    && rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]