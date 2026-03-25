import numpy as np

# ---------- BASIC INPUT ----------
name = input("Enter your name: ")
current_class = int(input("Enter your class (10-12): "))

subjects = []
core_subjects = []

# ---------- SUBJECT SETUP ----------
if current_class == 10:
    subjects = ["maths", "science", "social studies", "english"]
    core_subjects = ["maths", "science", "social studies"]

else:
    subjects = ["physics", "chemistry", "maths", "english"]
    core_subjects = ["physics", "chemistry", "maths"]

# ---------- MARKS ----------
marks = []
print("\nEnter marks out of 100:")
for sub in subjects:
    marks.append(int(input(f"{sub}: ")))

marks = np.array(marks)
core_marks = marks[[subjects.index(s) for s in core_subjects]]
avg_core = core_marks.mean()

# ---------- INTEREST ----------
interest = input(
    "\nPrimary Interest (tech / business / content / govt / medical): "
).lower()

# ---------- SKILLS ----------
skills = input(
    "Enter your skills (comma separated): "
).lower().split(",")

skills = [s.strip() for s in skills]

# ---------- CAREER MAP ----------
career_map = {
    "tech": ["python", "coding", "logic", "problem solving"],
    "business": ["communication", "marketing", "sales", "finance"],
    "content": ["writing", "editing", "creativity", "storytelling"],
    "govt": ["general knowledge", "analysis", "consistency"],
    "medical": ["biology", "memorization", "focus"]
}

# ---------- SCORING FUNCTIONS ----------
def interest_score(career):
    return 90 if career == interest else 60

def skill_score(career):
    relevant = career_map[career]
    match = len(set(skills) & set(relevant))
    if match >= 2:
        return 90
    elif match == 1:
        return 70
    else:
        return 40

def marks_score(career):
    if career == "medical" and "biology" in subjects:
        return avg_core
    if career == "tech" and "maths" in subjects:
        return avg_core
    return avg_core * 0.9

# ---------- FINAL SCORING ----------
career_scores = {}

for career in career_map:
    score = (
        interest_score(career) * 0.4 +
        marks_score(career) * 0.35 +
        skill_score(career) * 0.25
    )
    career_scores[career] = round(score, 2)

# ---------- TOP 3 CAREERS ----------
top_3 = sorted(
    career_scores.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

# ---------- OUTPUT ----------
print("\n----- Career Guidance Report -----")
print("Name:", name)
print("Class:", current_class)
print("Average Core Marks:", round(avg_core, 2))

print("\nTop Career Matches:")
for i, (career, score) in enumerate(top_3, 1):
    print(f"{i}. {career.title()}  → Score: {score}")

print("\nSuggested Focus:")
print("• Strengthen skills related to:", top_3[0][0])
print("• Improve weak subjects strategically")
print("• Build projects aligned with interest")

# ---------- SAVE DATA ----------
with open("students_data.txt", "a") as f:
    f.write(
        f"\n{name},{current_class},{avg_core},{interest},{skills},{top_3}"
    )

if __name__ == "__main__":
    main()
