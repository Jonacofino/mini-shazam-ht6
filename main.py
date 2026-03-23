from src.database import SongDatabase
from src.recognize import record_and_recognize

db = SongDatabase()
db.index_directory("songs/")

while True:
    input("Press Enter to recognize a clip (or Ctrl+C to quit)...")
    best_song, best_score, all_scores = record_and_recognize(db)
    
    print(f"Best match: {best_song} (score: {best_score})")
    print(f"Hash table scores for all candidates: {db.table.stats()}")