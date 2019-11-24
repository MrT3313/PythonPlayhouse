# Welcome to Lambda TL Feedback!
Mapped to Lambda Dashboard export available as of 11/23/19

## Data Used:
    - Date Submitted: col title === Submitted At (Simple Date)
    - Student Name: col title === Student 
    - Student TL Rating: col title === TL Rating
    - Student Written Feedback: col title === TL Feedback

## Language
Python3

## Get Started
1. Download the `TL_Feedback` directory
2. Go to your dashboard: [Lambda TL Dashboard](https://www.dashboards.lambdaschool.com)
3. Navigate to: Overview > Student Feedback
4. At the bottom left of the component click the export button. This will give you a `.csv` of your data
5. Find the absolute path to your downloaded `.csv` data. You can do this by clicking and dragging from your file explorer / finder into an open terminal window
6. In your terminal navigate into the `TL_Feedback` directory and run `python3 __mainFunction__.py`
7. Follow prompts

## ACTIONS
    1. Get Unique Students
    2. REPL Query TL for students added part way through your section 
        # Notes: I believe that you currently are able to see (and get as your export) all of the retros for that student currently in the system. 
            #  AKA: reviews are mapped to the CURRENT TL not a specific TL??
    3. Update Unique Students

## Print
    # [x] overall avg rating
    # [] Individual Students
        # 1. Name
        # 2. List of written feedback
        # 3. List of TL grades
        # 4. Avg TL grade from unique student

## Export 
    # standard excel file --> .xlsx