# Deep_Fake_interview_project

## Overview
This project is based on my earlier basketball dataset analysis (WNBA 2018–2022) and I turned it into a “deep fake” style interview. The main focus is on the process: analyzing the data, creating a narrative, and then presenting the results in an interview format.

## Workflow
1. Looked at the dataset in Python using pandas.  
2. Found the most improved teams (2018 → 2022), top 3 teams by total wins, and stats that correlated with win percentage.  
3. Wrote a Q&A interview script based on those results.  
4. Created an audio version with two different voices using ElevenLabs and joined the clips.  
5. Collected everything here in one repo.  

## Key Results
- **Most Improved Team (2018 → 2022):** Chicago Sky (0.382 → 0.722, +0.340)  
- **Runner-Ups:** Las Vegas Aces (+0.298), New York Liberty (+0.238)  
- **Top 3 Teams by Wins:** Connecticut Sun (105), Seattle Storm (105), Las Vegas Aces (103)  
- **Positive Correlations with Win%:** Wins (0.902953), FG% (0.738814), PPG (0.712392), 3PT% (0.686892), FGM (0.668774)  
- **Negative Correlations with Win%:** Losses (−0.903176), PF (−0.602896), TOV (−0.337999), OREB (−0.158467), 3PT Attempts (−0.070337)  

## Files in This Repo
- `script.txt` → the final interview script  
- `prompts_used.txt` → prompt I used to generate the script  
- `analyse_basketball.py` → Python analysis script  
- `most_improved.csv`, `top3_total_wins.csv`, `corr_with_win_percent.csv` → output data  
- `Final_Output.mp3` → audio interview (interviewer + coach)  
- `README.md` → this file
