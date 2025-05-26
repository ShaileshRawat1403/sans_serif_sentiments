# Getting Started with REAPER

A complete, beginner-focused guide to installing and configuring REAPER—the lightweight, flexible, and powerful digital audio workstation.

---

## Why This Guide Exists

REAPER updates often, but its installation process stays consistent—this single guide covers download, installation, setup, and troubleshooting, with version-specific notes where they matter.

---

## System Requirements

### Windows
- Windows 7, 8, 10, or 11 (32- or 64-bit)  
- ~20 MB free disk space  
- Optional: ASIO-compatible audio interface for low-latency performance

### macOS
- macOS 10.5 and later (up to Sonoma)  
- Intel and Apple Silicon (M1/M2/M3) chips supported  
- Uses CoreAudio natively—no driver install required

> **Tip:** REAPER is exceptionally lightweight—most modern computers run it without issue.

---

## Download REAPER

1. Go to [reaper.fm](https://reaper.fm).  
2. Click **Download REAPER**.  
3. Select:
   - **Windows 64-bit** (most common)  
   - **macOS Universal** (Intel + Apple Silicon)

> **Note:** The version number you see may be newer—but these steps still apply.

---

## Install REAPER

### Windows
1. Open the downloaded `.exe`.  
2. Accept the license agreement.  
3. Choose an install location (default is fine).  
4. (Optional) Select **Portable Install** to keep settings together.  
5. Click **Install**.

### macOS
1. Open the downloaded `.dmg`.  
2. Drag the REAPER icon into **Applications**.  
3. Right-click the app and choose **Open** to bypass Gatekeeper.

> **Note:** On macOS Ventura and newer, you may need to allow REAPER under **System Settings → Security & Privacy**.

---

## Configure Audio Settings

1. Launch REAPER.  
2. Go to **Options → Preferences → Audio → Device**.

### Windows
- **ASIO** (best performance) for external audio interfaces  
- **WASAPI** for built-in speakers

### macOS
- **CoreAudio** auto-selects your device  
- Use the dropdowns to choose input/output

> **Tip:** If you hear no sound, double-check your device selection and increase the buffer size.

---

## Understand Theme & Layout

REAPER 7 introduced a modern UI:

- Floating track controls  
- Spacing and alignment tweaks  
- Improved routing panels

> **Note for v7.0 users:** Switch back to the classic theme at **Options → Themes → Default_6.0**.  
> **Note for v7.1+ users:** You’ll notice refined meter contrast and lane behavior.

---

## Troubleshooting

| Problem                   | Solution                                                |
|---------------------------|---------------------------------------------------------|
| No sound output           | Check **Preferences → Audio → Device** settings         |
| App won’t open (macOS)    | Right-click → **Open** or allow in Security & Privacy   |
| Track lanes are hidden    | Right-click TCP → **Enable Track Lanes**                |
| Audio glitches or pops    | Increase buffer size or adjust sample rate              |

---

## Version-Specific Notes

For theme and workflow details by release:

- [REAPER v7.0 Notes](../v7.0/index.md)  
- [REAPER v7.1+ Notes](../v7.1/index.md)

---

## What’s Next?

You’re ready to record and play:

1. **Insert a new track** (`Track → Insert new track`).  
2. **Drag in an audio file** and press ►.  
3. Explore **plugins**, **MIDI mapping**, and more in the next sections.

> This guide is part of a larger documentation portfolio built with clarity and care. Your feedback is welcome!
