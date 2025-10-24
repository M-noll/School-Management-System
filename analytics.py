import json
import os
import heapq

class PerformanceAnalytics:
    def __init__(self, filename="analytics.json"):
        self.filename = filename
        self.student_scores = []  # Max-heap: (-score, student_id)
        self.load_scores()

    def add_student_score(self, student_id, score):
        # Python heapq is a min-heap; use negative score for max-heap
        heapq.heappush(self.student_scores, (-score, student_id))
        self.save_scores()

    def get_top_student(self):
        if self.student_scores:
            score, student_id = self.student_scores[0]
            return {"student_id": student_id, "score": -score}
        return None

    def get_top_n(self, n=3):
        # Get top n students without removing them
        top = heapq.nsmallest(n, self.student_scores)
        return [{"student_id": sid, "score": -s} for s, sid in top]

    def save_scores(self):
        # Convert heap to list for JSON
        serializable = [{"student_id": sid, "score": -s} for s, sid in self.student_scores]
        with open(self.filename, "w") as f:
            json.dump(serializable, f, indent=4)

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                scores = json.load(f)
                # rebuild max-heap
                self.student_scores = [(-rec["score"], rec["student_id"]) for rec in scores]
                heapq.heapify(self.student_scores)
        else:
            self.student_scores = []
