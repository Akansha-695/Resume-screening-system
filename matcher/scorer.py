class Scorer:
    def calculate_score(self, resume_skills, jd_data):

        required_skills = jd_data["required"]
        preferred_skills = jd_data["preferred"]

        required_matches = len(
            set(required_skills) & set (resume_skills)
        )

        preferred_matches = len(
            set(preferred_skills) & set(resume_skills)
        )

        required_score = required_matches * 10
        preferred_score = preferred_matches * 5

        total_score = required_score + preferred_score

        return min(total_score, 100)
    
