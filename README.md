# toki-pona-translator
Simple translator, or rather dictionary for Toki Pona. Designed to be run quickly from your linux start menu.
## Instalation
1. Clone the repository `git clone https://github.com/qsus/toki-pona-translator` to your home directory.
2. Replace "USER" in .desktop file with your username in all entry keys. (Shell command: `sed -i "s/USER/yourUsername/g" "Toki Pona Translator.desktop"` Vim command: `:%s/USER/yourUsername/g`)
3. Install script by running `desktop-file-install "Toki Pona Translator.desktop"` (may require sudo). Alternatively, copy the file to `/usr/share/applications`.
