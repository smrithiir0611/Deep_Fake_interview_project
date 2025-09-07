import pandas as pd

CSV_FILE = "teamstats.csv"   # <- change if your file has a different name
BASE_YEAR = 2018
END_YEAR  = 2022

# --- Load ---
df = pd.read_csv(CSV_FILE)

# --- Sanity checks: make sure required cols exist (using your exact names) ---
required = {
    "season","team","gp","w","l","win_percent","ppg","fgm","fga","fg_percent",
    "threepoint_fgm","threepoint_fga","threepoint_fg_percent","ftm","fta","ft_percent",
    "oreb","dreb","reb","ast","tov","stl","blk","pf","pfd","position"
}
missing = [c for c in ["season","team","gp","w","win_percent"] if c not in df.columns]
if missing:
    raise ValueError(f"CSV is missing required columns: {missing}")

# --- If there are duplicate rows per team-season, collapse to team-season level ---
agg_funcs = {
    "gp":"sum","w":"sum","l":"sum","win_percent":"mean","ppg":"mean","fgm":"mean","fga":"mean","fg_percent":"mean",
    "threepoint_fgm":"mean","threepoint_fga":"mean","threepoint_fg_percent":"mean","ftm":"mean","fta":"mean","ft_percent":"mean",
    "oreb":"mean","dreb":"mean","reb":"mean","ast":"mean","tov":"mean","stl":"mean","blk":"mean","pf":"mean","pfd":"mean"
}
team_year = (
    df.groupby(["team","season"], as_index=False)
      .agg(agg_funcs)
)

# --- 1) Improvement from 2018 -> 2022 using win_percent ---
base = team_year[team_year["season"] == BASE_YEAR][["team","win_percent"]].rename(columns={"win_percent": f"winpct_{BASE_YEAR}"})
end  = team_year[team_year["season"] == END_YEAR][["team","win_percent"]].rename(columns={"win_percent": f"winpct_{END_YEAR}"})
improve = (
    end.merge(base, on="team", how="inner")
       .assign(improvement=lambda d: d[f"winpct_{END_YEAR}"] - d[f"winpct_{BASE_YEAR}"])
       .sort_values("improvement", ascending=False, ignore_index=True)
)

# --- 2) Top 3 teams by total wins across all years ---
total_wins = (
    team_year.groupby("team", as_index=False)["w"].sum()
             .rename(columns={"w":"total_wins"})
             .sort_values("total_wins", ascending=False, ignore_index=True)
)

# --- 3) Correlations with WIN% ---
# Correlate win_percent with other numeric stats (exclude identifiers & win_percent itself)
num = team_year.select_dtypes("number").copy()
if "season" in num.columns:   num = num.drop(columns=["season"])
pos_corr = num.corr(numeric_only=True)["win_percent"].drop(labels=["win_percent"], errors="ignore").sort_values(ascending=False)
neg_corr = pos_corr.sort_values(ascending=True)

# --- PRINT ANSWERS YOU NEED ---
print("\n=== MOST IMPROVED (win% change from 2018 to 2022) ===")
if not improve.empty:
    print(improve.head(10).to_string(index=False))
    print("\nTop 1 most improved team:")
    print(improve.iloc[0][["team", f"winpct_{BASE_YEAR}", f"winpct_{END_YEAR}", "improvement"]].to_string())
    print("\nRunner-ups (next 2):")
    if len(improve) >= 3:
        print(improve.iloc[1:3][["team","improvement"]].to_string(index=False))
    else:
        print("Not enough teams with both 2018 and 2022.")
else:
    print("No teams have both 2018 and 2022 data — check the 'season' values.")

print("\n=== TOP 3 TEAMS BY TOTAL WINS (2018–2022) ===")
print(total_wins.head(3).to_string(index=False))

print("\n=== STRONGEST POSITIVE CORRELATIONS WITH WIN% ===")
print(pos_corr.head(5).to_string())

print("\n=== STRONGEST NEGATIVE CORRELATIONS WITH WIN% ===")
print(neg_corr.head(5).to_string())

# --- Save CSVs for your README/repo ---
improve.to_csv("most_improved.csv", index=False)
total_wins.head(3).to_csv("top3_total_wins.csv", index=False)
pos_corr.to_frame("corr_with_win_percent").to_csv("corr_with_win_percent.csv")
print("\nSaved: most_improved.csv, top3_total_wins.csv, corr_with_win_percent.csv")
