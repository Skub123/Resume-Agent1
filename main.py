from resume_parser import parse_resume
from optimizer import optimize_resume
from scorer import score_resume

def run_agent(resume_path: str, job_description: str):
    resume_text = parse_resume(resume_path)

    optimized_resume = optimize_resume(resume_text, job_description)
    ats_score = score_resume(optimized_resume, job_description)

    print("\n===== OPTIMIZED RESUME =====\n")
    print(optimized_resume)

    print("\n===== ATS SCORE =====")
    print(f"{ats_score}%")

if __name__ == "__main__":
    resume_path = "resume.pdf"  # change if needed
    job_description = input("Paste Job Description:\n")
    run_agent(resume_path, job_description)
