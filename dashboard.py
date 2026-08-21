import pandas as pd

def analyze_football_match(data):
    """
    מקבל DataFrame של נתוני משחק כדורגל (למשל: שערים, בעיטות, מסירות, שליטה בכדור)
    ומייצר ניתוח על המשחק.
    """
    analysis = {}

    # ניתוח שערים
    if 'Goals' in data.columns:
        analysis['Total Goals'] = data['Goals'].sum()
        analysis['Goals by Team'] = data.groupby('Team')['Goals'].sum().to_dict()

    # ניתוח בעיטות לשער
    if 'Shots' in data.columns:
        analysis['Total Shots'] = data['Shots'].sum()
        analysis['Shots by Team'] = data.groupby('Team')['Shots'].sum().to_dict()

    # ניתוח מסירות
    if 'Passes' in data.columns:
        analysis['Total Passes'] = data['Passes'].sum()
        analysis['Passes by Team'] = data.groupby('Team')['Passes'].sum().to_dict()

    # ניתוח שליטה בכדור (אחוזים)
    if 'Possession' in data.columns:
        analysis['Possession % by Team'] = data.groupby('Team')['Possession'].mean().to_dict()

    return analysis

# דוגמה לשימוש
if __name__ == "__main__":
    # יצירת נתונים לדוגמה
    match_data = pd.DataFrame([
        {'Team': 'A', 'Goals': 2, 'Shots': 8, 'Passes': 320, 'Possession': 55},
        {'Team': 'B', 'Goals': 1, 'Shots': 6, 'Passes': 280, 'Possession': 45}
    ])
    report = analyze_football_match(match_data)
    for key, value in report.items():
        print(f"{key}: {value}")