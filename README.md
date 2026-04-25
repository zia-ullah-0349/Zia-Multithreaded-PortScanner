# ZIA Multithreaded Port Scanner ⚡🛡️

>>**"Me Ziaullah..."** 🚀.

>>**"Instructor Dr Muhammad Kazim"

A fast multithreaded TCP port scanner with banner grabbing, built in Python for educational purposes. This project demonstrates the evolution from a basic scanner to a professional tool.

**⚠️ Disclaimer:** This tool is for educational purposes only. Only scan systems you own or have explicit permission to test. Unauthorized scanning is illegal.

---

🚀 Versions & Features

**01 - Speed Base** ✅
The first multithreaded version. The foundation of the project.
- **File:** `multithreaded_scanner_v01.py`
- **Features:**
    - Scans ports 1-100 using `threading` and `Queue`
    - Fixed 50 threads for high speed
    - Basic banner grabbing on open ports
- **Speed:** ~100 ports in 2-3 seconds

**V02 - Range Master** ✅
Added flexibility for the user.
- **File:** `multithreaded_scanner_v02.py`
- **Upgrades:**
    - **Custom Port Range:** User can now input `Start Port` and `End Port`
    - Can scan any range, e.g., `1-1024` or `20-25,80,443`
- **Usage:**
  Start Port: 1
  End Port: 1000

---

🛠️ How to Run

1. **Clone the repo:**
    ```bash
    git clone https://github.com/zia-ullah-0349/Zia-Multithreaded-PortScanner
2. *Run a specific version:*
    multithreaded_scanner_v01.py
3. *Enter Target:* Use `scanme.nmap.org` for legal testing.

---

📈 Roadmap - Coming Soon

- [ ] *V03 - Speed Control:* User-defined thread count
- [ ] *V04- Smart Display:* Progress bar + timer
- [ ] *V05 - Service Name:* Detect service like HTTP, SSH
- [ ] *V06 - File Save:* Export results to `.txt` or `.csv`
- [ ] *V07 - Final Boss:* Colors and look
--
