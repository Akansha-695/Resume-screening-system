import json
import re


class KeywordExtractor:

    def __init__(self, taxonomy_path):

        with open(taxonomy_path, "r") as file:
            self.skills_taxonomy = json.load(file)

    def extract_skills(self, text):

        text_lower = text.lower()

        found_skills = set()

        for category, skills_dict in self.skills_taxonomy.items():

            for skill_name, variations in skills_dict.items():

                for variation in variations:

                    pattern = r"\b" + re.escape(variation) + r"\b"

                    if re.search(pattern, text_lower):

                        found_skills.add(skill_name)
                        break

        return found_skills
