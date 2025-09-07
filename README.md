# Task_06_Deep_Fake


## Overview
This project is based on my earlier basketball dataset analysis (WNBA 2018–2022) and I turned it into a “deep fake” style interview. The main focus is on the process: analyzing the data, creating a narrative, and then presenting the results in an interview format.

## Workflow
1. Looked at the dataset in Python using pandas.  
2. Found the most improved teams (2018 → 2022), top 3 teams by total wins, and stats that correlated with win percentage.  
3. Wrote a Q&A interview script based on those results.  
4. Created an audio version with two different voices using ElevenLabs and joined the clips.  
5. Collected everything here in one repo.  

## Key Results
1. The team that showed the biggest improvement from 2018 to 2022 was the Chicago Sky. Their win percentage went from 0.382 to 0.722, which is about a +0.340 jump.  
2. Close behind them were the Las Vegas Aces (+0.298) and the New York Liberty (+0.238).  
3. Over the full stretch of five seasons, the Connecticut Sun and Seattle Storm tied for the most wins with 105 each, and the Las Vegas Aces were just behind with 103.  
4. Looking at stats that connect most strongly with winning, the top ones were wins themselves (0.902953), field goal percentage (0.738814), points per game (0.712392), three-point percentage (0.686892), and field goals made (0.668774).  
5. On the negative side, losses (−0.903176) were the strongest, followed by personal fouls (−0.602896), turnovers (−0.337999), offensive rebounds (−0.158467) and even three-point attempts (−0.070337), which were linked with weaker win percentages.  

## Files in This Repo
- `script.txt` → the final interview script  
- `prompts_used.txt` → prompt I used to generate the script  
- `analyse_basketball.py` → Python analysis script  
- `most_improved.csv`, `top3_total_wins.csv`, `corr_with_win_percent.csv` → output data  
- `Final_output.mp3` → audio interview (interviewer + coach)  
- `README.md` → this file

## Audio File
The final interview is available as `Final_output.mp3`.  
You can listen by clicking the file in this repository and then selecting **View raw** or the **Download** button to play it.

