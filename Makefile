SCRIPT_DIR := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
BD := $(SCRIPT_DIR)/build
O5GS_DIR := $(SCRIPT_DIR)/open5gs

LIBSVF := $(BD)/libsvfd.so

all: $(LIBSVF)

clean:
	rm -rf $(BD)

$(BD):
	mkdir -p $@

$(BD)/o5gs: | $(BD)
	meson setup $@ $(O5GS_DIR) --reconfigure --optimization=2 -Dc_std=gnu11

$(LIBSVF): $(BD)/o5gs
	ninja -C $^
	cp $^/src/svf/libsvfd.so $@
	patchelf --add-rpath '$$ORIGIN/o5gs/lib/sbi:$$ORIGIN/o5gs/lib/crypt:$$ORIGIN/o5gs/lib/proto:$$ORIGIN/o5gs/lib/core:$$ORIGIN/o5gs/lib/app:$$ORIGIN/o5gs/lib/sbi/openapi' $@

.PHONY: clean $(LIBSVF)
