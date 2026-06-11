class JDParser:

    def parse_jd(self, jd_text):

        jd_text = jd_text.lower()

        required = []
        preferred = []

        lines = jd_text.split("\n")

        current_section = None

        for line in lines:

            line = line.strip()

            if "required skills" in line:
                current_section = "required"

            elif "preferred skills" in line:
                current_section = "preferred"

            elif line.startswith("-"):

                skill = line.replace("-", "").strip()

                if current_section == "required":
                    required.append(skill)

                elif current_section == "preferred":
                    preferred.append(skill)

        return {
            "required": required,
            "preferred": preferred
        }
