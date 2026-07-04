FROM dnlnash/jenuxos:jenux-base-rootfs
RUN pacman --noconfirm --overwrite \* -Syu
RUN pacman --noconfirm --overwrite \* -S python python-requests
RUN rm -rf /var/cache/pacman/pkg/*
COPY . /build
WORKDIR /build
CMD ["/build/chromeos_install"]
