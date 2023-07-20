# plugin.program.wireguard-switch
Kodi plugin for toggle wireguard vpn connection

## Requirements
script that can be run by kodi

### For example on linux:

File which turns on vpn
```bash
#vpn-on.sh
/usr/bin/wg-quick up /home/speker/wireguard-config.conf
```
File which call file above with no need to enter password
```bash
#vpn-on-nopass.sh
#!/bin/sh
sudo /path/to/vpn-on.sh
```

For no password `/path/to/vpn-on.sh` should be in sudoers config with `:nopass` for user which runs kodi
