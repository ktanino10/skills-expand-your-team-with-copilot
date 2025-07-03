# Example: Issue Template Usage

This document shows examples of how teachers might use the issue templates.

## Example 1: Adding a New Activity

**Template Used:** 🎯 Add New Activity/Club

**Teacher Input:**
- Activity Name: "Photography Club"
- Description: "Learn photography techniques, develop film, and participate in photo contests around the school"
- Category: "Arts"
- Max Participants: "15"
- Schedule Days: ✅ Thursday
- Start Time: "3:30 PM"
- End Time: "5:00 PM"
- Teacher Sponsor: "Ms. Rodriguez"
- Special Requirements: "Needs access to darkroom facilities"

**Result:** Copilot agent adds Photography Club to the system with proper formatting and schedule structure.

---

## Example 2: Modifying an Existing Activity

**Template Used:** ✏️ Modify Existing Activity

**Teacher Input:**
- Activity: "Chess Club"
- Changes Needed: ✅ Schedule (days and/or times)
- New Schedule Days: ✅ Tuesday, ✅ Thursday
- New Start Time: "7:00 AM"
- New End Time: "8:00 AM"
- Reason: "Room conflict with Drama Club on Mondays and Fridays"

**Result:** Copilot agent updates Chess Club schedule from Mon/Fri to Tue/Thu with new times.

---

## Example 3: Bulk Student Management

**Template Used:** 👥 Student Management

**Teacher Input:**
- Operation: "Bulk student enrollment"
- Target Activity: "Math Club"
- Student List:
  ```
  alice@mergington.edu
  bob@mergington.edu
  charlie@mergington.edu
  diana@mergington.edu
  ```
- Reason: "Students transferred from canceled Advanced Math class"

**Result:** Copilot agent adds all 4 students to Math Club, checking capacity limits.

---

## Example 4: Bug Report

**Template Used:** 🐛 Bug Report

**Teacher Input:**
- Problem: "Students getting 'Authentication required' error when trying to sign up"
- Steps to Reproduce:
  1. Student goes to activities page
  2. Clicks "Register" for any activity
  3. Enters email address
  4. Clicks submit
  5. Gets error message
- Expected: "Student should be registered successfully"
- Area Affected: "Student registration/signup"
- Urgency: "High"

**Result:** Copilot agent investigates authentication flow and fixes the bug.

---

## What Makes These Templates Effective

1. **Structured Input**: Required fields ensure all necessary information is provided
2. **Clear Options**: Dropdown menus prevent typos and invalid entries
3. **Context**: Reason fields help the agent understand the request
4. **Developer Guidance**: Each template includes technical implementation details
5. **Validation**: Required fields prevent incomplete requests

## Benefits for Teachers

- **No Technical Knowledge Required**: Just fill out forms
- **Consistent Results**: Structured templates ensure proper implementation
- **Quick Processing**: All required information is provided upfront
- **Automatic Assignment**: Issues are automatically assigned to Copilot agent
- **Clear Communication**: Templates enforce clear problem descriptions

## Benefits for Copilot Agent

- **Complete Context**: All necessary information is provided
- **Clear Requirements**: Acceptance criteria are defined
- **Implementation Hints**: Technical guidance is included
- **Structured Data**: Consistent format makes parsing easier
- **Validation**: Required fields prevent incomplete requests