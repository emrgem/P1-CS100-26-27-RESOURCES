"""
Lesson 6 Activity: Code Cleanup
CS100: Roadmap to Computing

This program WORKS. It is just badly written. Clean it up without
changing a single thing it prints.
"""

ticketPrice=12.50
snackPrice=4.25
studentCount=5
total=0
total=total+studentCount*12.50
total=total+studentCount*4.25
perPerson=total/studentCount
print("=" * 34)
print("        FIELD TRIP TOTAL")
print("=" * 34)
print(f"Students: {studentCount}")
print(f"Tickets: ${studentCount * 12.50:.2f}")
print(f"Snacks: ${studentCount * 4.25:.2f}")
print("-" * 34)
print(f"Total: ${total:.2f}")
print(f"Per person: ${perPerson:.2f}")
print("=" * 34)


# =============================================================
# YOUR CHECKLIST
# =============================================================
# 1. Add the required header comment: name, assignment, date
# 2. Add a docstring at the top saying what this program does
# 3. Rename every variable to snake_case
# 4. Put spaces around = + * / so it can be read
# 5. 12.50 and 4.25 appear twice each. Make them named constants.
# 6. Replace total = total + x with the shorter form
# 7. Add comments that explain WHY, not what
#
# RULE: the output must be EXACTLY the same when you are done.
# Run it before and after and compare.