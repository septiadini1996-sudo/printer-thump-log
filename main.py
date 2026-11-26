# SPDX-License-Identifier: MIT
"""The office printer, finally answering back.

Writes the printer's one-line status report to /output/entry.txt.
The line is the machine's own status readout: three flat fields, no
sentence at all. The printer answers every thump it has ever taken
with the arithmetic of how little thumping has ever achieved — the
comeback is a counted zero, which is the only language a printer
that has logged every sheet it ever fed would use.
"""

LINE = "STATUS: PAPER JAM. THUMPS RECEIVED: 4,096. JAMS CLEARED BY THUMPING: 0."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
