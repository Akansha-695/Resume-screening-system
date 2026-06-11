import streamlit as st
import tempfile
import pandas as pd

from parsers.resume_parser import ResumeParser
from parsers.jd_parser import JDParser
from extractors.keyword_extractor import KeywordExtractor
from matcher.scorer import Scorer


# Initialize modules
resume_parser = ResumeParser()
jd_parser = JDParser()

extractor = KeywordExtractor(
    "data/skills_taxonomy.json"
)

scorer = Scorer()


# Page title
st.title("AI Resume Screening System")


# Job Description input
jd_text = st.text_area(
    "Paste Job Description",
    height=250
)


# Upload message
st.markdown(
    """
    <div style="
        padding:10px;
        border-radius:10px;
        background-color:#1e1e1e;
        color:#ffffff;
        margin-bottom:10px;
    ">
    📄 Only PDF and DOCX files are supported.
    </div>
    """,
    unsafe_allow_html=True
)


# File uploader
uploaded_files = st.file_uploader(
    "Upload Resumes",
    accept_multiple_files=True
)


# Screen button
if st.button("Screen Resumes"):

    # Validate JD
    if not jd_text.strip():

        st.warning(
            "Please enter a Job Description."
        )

    # Validate uploads
    elif not uploaded_files:

        st.warning(
            "Please upload at least one resume."
        )

    # Invalid file validation
    elif any(
        file.name.split(".")[-1].lower()
        not in ["pdf", "docx"]
        for file in uploaded_files
    ):

        st.error(
            "Only PDF and DOCX files are allowed to upload."
        )

    else:

        results = []

        # Parse JD
        jd_data = jd_parser.parse_jd(
            jd_text
        )

        # Process resumes
        for uploaded_file in uploaded_files:

            file_extension = (
                uploaded_file.name
                .split(".")[-1]
                .lower()
            )

            try:

                # Save temporary file
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix="." + file_extension
                ) as tmp_file:

                    tmp_file.write(
                        uploaded_file.read()
                    )

                    file_path = tmp_file.name

                # Extract text
                text = resume_parser.extract_text(
                    file_path
                )

                # Extract skills
                skills = extractor.extract_skills(
                    text
                )

                # Calculate score
                score = scorer.calculate_score(
                    skills,
                    jd_data
                )

                # Save result
                results.append({

                    "Name": uploaded_file.name,

                    "Score": score,

                    "Skills": ", ".join(skills)

                })

            except Exception as e:

                st.error(
                    f"Error processing "
                    f"{uploaded_file.name}: {e}"
                )

        # Show results
        if results:

            df = pd.DataFrame(results)

            df = df.sort_values(
                by="Score",
                ascending=False
            )

            st.subheader(
                "Candidate Rankings"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No valid resumes processed."
            )
