# regdump

This package include core functions to parse or dump the register values
according to the register profile (usually got from chip's datasheet).

# run test code

```
cd src
python3 -m unittest regdump/profile_test.py
```

# using regdump to interprete the register values

Install the tool:

```
python3 setup.py install
```

## Using the tool
```
usage: regdump [-h] -p PROFILE value

positional arguments:
  value       register value to be intepreted

optional arguments:
  -h, --help  show this help message and exit
  -p PROFILE  the profile define the register bitmap
```

example:

```
$ regdump -p regdump/src/rga2_alpha_ctrl0.reg 0x90
sw_mask_endian (ROP4 mask endian swap)
        bit 20 len 1
        0b0 (Big endian)
sw_dst_global_alpha (Global alpha value of DST(Agd))
        bit 12 len 8
        0
sw_src_global_alpha (Global alpha value of SRC(Ags) Fading value in fading mod)
        bit 4 len 8
        9
sw_rop_mode (ROP mode select)
        bit 2 len 2
        0b00 (ROP 2)
sw_alpha_rop_sel (Alpha or ROP select)
        bit 1 len 1
        0b0 (Alpha)
sw_alpha_rop_e (Alpha or ROP enable)
        bit 0 len 1
        0b0 (Disable)
```
