# Getting Started with REAPER

A complete, beginner-focused guide to installing and configuring REAPER—the lightweight, flexible, and powerful digital audio workstation.

---

## Why This Guide Exists

REAPER updates often, but installation steps stay consistent. This guide covers:

- **Download** REAPER  
- **Install** on Windows or macOS  
- **Configure** audio settings  
- **Troubleshoot** common issues  

Version-specific notes are included where they matter.

---

## System Requirements

| Platform    | Requirements                                                                 |
|-------------|-------------------------------------------------------------------------------|
| **Windows** | • Windows 7 or later (32- or 64-bit)  <br> • ~20 MB free disk space  <br> • (Optional) ASIO-compatible audio interface |
| **macOS**   | • macOS 10.5+ (up to Sonoma)  <br> • Universal build for Intel & Apple Silicon  <br> • CoreAudio (no extra drivers required) |

> **Tip:** REAPER is exceptionally lightweight—most modern systems run it without issue.

---

## Download REAPER

```text
1. Visit https://reaper.fm  
2. Click “Download REAPER”  
3. Select your OS:
   - Windows 64-bit  
   - macOS Universal  
```

> **Note:** Version numbers may change, but these steps remain valid.

---

## Install REAPER

### Windows

```bash
# Run the installer
./REAPER_installer.exe
```

1. Double-click the downloaded `.exe`.  
2. Accept the license agreement.  
3. Choose an install location (default is fine).  
4. (Optional) Enable **Portable Install** to keep settings contained.  
5. Click **Install**.

### macOS

```bash
# Mount and install
open REAPER.dmg
cp -R /Volumes/REAPER/REAPER.app /Applications/
```

1. Mount the downloaded `.dmg`.  
2. Drag **REAPER.app** into **Applications**.  
3. Right-click **REAPER.app** → **Open** to bypass Gatekeeper.

> **Note (Ventura+):** You may need to allow REAPER under **System Settings → Security & Privacy**.

---

## Configure Audio Settings

Launch REAPER and go to:

```text
Options → Preferences → Audio → Device
```

- **Windows**  
  - **ASIO** (low-latency) for external interfaces  
  - **WASAPI** for built-in speakers  

- **macOS**  
  - **CoreAudio** auto-detects devices  

> **Tip:** If you hear no sound, verify the selected device and increase the buffer size.

---

## Understand Theme & Layout

REAPER 7’s default theme includes:

- Floating track controls  
- Revised icons & spacing  
- Enhanced routing panels  

> **Note (v7.0):** Revert to the classic theme at **Options → Themes → Default_6.0**  
> **Note (v7.1+):** Expect refined meter contrast & lane behavior

---

## Troubleshooting

| Issue                   | Solution                                               |
|-------------------------|--------------------------------------------------------|
| No audio output         | Check **Preferences → Audio → Device** settings        |
| App won’t launch (macOS)| Right-click **Open** or allow in **Security & Privacy** |
| Hidden track lanes      | Right-click TCP → **Enable Track Lanes**                |
| Audio glitches or pops  | Increase buffer size or adjust sample rate             |

---

## Version-Specific Notes

- [REAPER v7.0 Theme & Layout](../v7.0/index.md)  
- [REAPER v7.1+ Refinements](../v7.1/index.md)

---

## What’s Next

1. **Insert** a new track: _Track → Insert new track_  
2. **Drag** an audio file into the timeline  
3. **Press** ▶️ to play  

Explore plugins, MIDI mapping, and more in the next guides.

> **Feedback welcome:** Open an issue or submit a pull request to improve this guide.  
`
