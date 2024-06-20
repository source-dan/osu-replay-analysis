## Reason for Creation
This osu! Replay Analyser was developed to enhance accessibility and transparency, sparked by recent controversies surrounding Dynamic Key Setting (DKS) usage. In a notable incident, suspicions arose around a player known as Cloutiful, who consistently achieved unusually low hold times during gameplay.  

The controversy gained traction when players and community members observed that Cloutiful's hold times consistently averaged around exactly 63 milliseconds, a rate deemed practically impossible under normal gameplay conditions. These suspicions led to investigations and community discussions, highlighting the need for tools that could analyse and scrutinise gameplay replays more effectively.

This software address these concerns by providing accessible software that parses and analyses `.osr` replay files from osu!. By enabling players and spectators to examine key press events and optionally compute hold times, the tool promotes fair play and integrity.




## How It Works

(__This software can be used to detect ReplayRidor, or any other form of replay riding/stealing. It can also be used to check for relax, DKS/Macros, or any other form of key-press/hit cheat.__)

This Python program is designed to parse and analyse `.osr` replay files from the game osu!. It extracts key press events and optionally calculates and visualises hold times for each key press event. Here’s how to use it:

1. **Installation**: Clone the repository or download the `init.py` file to your local machine.

2. **Dependencies**: Ensure you have Python 3.x installed along with the required libraries: `matplotlib` and `webbrowser`.

3. **Usage**:


   - **File Naming**: Ensure your replay file is named `replay.osr` and is placed in the same directory as `init.py`.
   - **Running the Program**: Open a terminal or command prompt, navigate to the directory containing `initr.py`, and run:
     ```bash
     python init.py
     ```
   - **Prompt**: Follow the prompts to specify the number of key presses or hold times to plot and choose whether to plot timestamps or hold times.

4. **Output**:
   - The program will generate plots (`key_presses.png` or `hold_times.png`) and open them in your default web browser.
   - Total counts of key presses or hold times will be displayed in the terminal.
  

**NOTE:** REPLAY INCLUDED IS MREKK'S 1500pp PLAY ON: Owari Tsumugishi Mono by Denkishiki Karen Ongaku Shuudan | Lasse's Extra: 

## Screenshots
1. Example of Key Presses Plot (`key_presses.png`):
   ![Key Presses Plot](https://i.ibb.co/rf5Yp5R/key-presses.png)

2. Example of Hold Times Plot (`hold_times.png`):
   ![Hold Times Plot](https://i.ibb.co/FsMbgTy/hold-times.png)

## Naming Convention
Ensure your replay file is named `replay.osr` for the program to correctly locate and analyze it.

## License
This project is licensed under the GNU General Public License (GPL) Version 3.0. See the [LICENSE](LICENSE) file for more details.

---

### Additional Notes
- **Accuracy**: The program aims to accurately parse and analyze key press events from `.osr` files.
- **Feedback**: We welcome feedback and contributions to improve the software's functionality and usability.
