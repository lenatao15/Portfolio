import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Profile, Skill, Experience, Education, Certification, Project

def populate():
    # Profile
    Profile.objects.all().delete()
    profile = Profile.objects.create(
        name="Olena Makarova",
        about_me="""I’m a Master of Science in Information Systems student at Baylor University with a concentration in Business Analysis (GPA: 4.0). 

My background is a mix of sociology and technology, which means I don’t just look at data — I try to understand the human story behind it. I enjoy organizing messy information, finding patterns, and turning chaos into something structured and useful.

I’ve worked in both administrative and data-focused roles, where I developed strong attention to detail, problem-solving skills, and the ability to work across teams. I’m especially interested in roles where I can combine analytical thinking with real-world impact.""",
        email="Olena_makarova1@baylor.edu",
        phone="(707) 413-5847",
        linkedin="https://www.linkedin.com/in/olena-makarova-a10687198/"
    )

    # ... (skipping some lines for brevity in instruction, will apply actual replacement)

    # Skills
    Skill.objects.all().delete()
    skills = [
        ('technical', 'Data Analysis & Data Cleaning'),
        ('technical', 'SQL'),
        ('technical', 'Python'),
        ('technical', 'Tableau'),
        ('technical', 'Microsoft Excel'),
        ('technical', 'Lucidchart'),
        ('technical', 'Visio'),
        ('technical', 'Data Modeling'),
        ('technical', 'Basic Video Editing'),
        ('analytical', 'Trend Analysis'),
        ('analytical', 'Data Interpretation'),
        ('analytical', 'Problem Solving'),
        ('analytical', 'Workflow Optimization'),
        ('soft', 'Communication'),
        ('soft', 'Cross-functional Collaboration'),
        ('soft', 'Attention to Detail'),
        ('soft', 'Organization'),
        ('soft', 'Adaptability'),
        ('language', 'Ukrainian', 'Native'),
        ('language', 'Russian', 'Native'),
        ('language', 'English', 'Fluent'),
        ('language', 'Chinese', 'Pre-intermediate'),
        ('language', 'Japanese', 'Beginner'),
    ]
    for s in skills:
        if len(s) == 3:
            Skill.objects.create(category=s[0], name=s[1], proficiency=s[2])
        else:
            Skill.objects.create(category=s[0], name=s[1])

    # Experience
    Experience.objects.all().delete()
    Experience.objects.create(
        job_title="Property Records Analyst",
        company="Total Tax Certificate",
        location="Waco, TX",
        start_date="April 2025",
        end_date="Present",
        description="- Analyzed and organized large volumes of property and tax records\n- Transformed raw public data into structured, client-ready datasets\n- Identified discrepancies and resolved data issues\n- Compiled information from multiple sources into clean Excel reports\n- Supported accurate and timely property tax reporting"
    )
    Experience.objects.create(
        job_title="Project Administrator",
        company="Stantec",
        location="Petaluma, CA",
        start_date="April 2023",
        end_date="December 2024",
        description="- Processed expense reports, invoices, and purchase orders with high accuracy\n- Improved financial tracking through systematic review processes\n- Maintained and audited company databases to ensure data integrity\n- Acted as a liaison between HR, finance, and project teams\n- Helped streamline workflows and reduce delays in project operations\n- Implemented digital document organization systems"
    )

    # Education
    Education.objects.all().delete()
    Education.objects.create(
        institution="Baylor University",
        location="Waco, TX",
        degree="Master of Science in Information Systems",
        graduation_date="Expected June 2026",
        gpa="4.0",
        details="Concentration: Business Analysis"
    )
    Education.objects.create(
        institution="Kyiv National University of Culture and Arts",
        location="Kyiv, Ukraine",
        degree="Bachelor of Sociology",
        graduation_date="July 2018",
        details="Focus: Sociology and Data Analysis"
    )

    # Certifications
    Certification.objects.all().delete()
    Certification.objects.create(name="HRCI Human Resource Associate Specialization Certificate")

    # Projects
    Project.objects.all().delete()
    
    projects_data = [
        {
            "title": "Chatbot Project",
            "summary": "An intelligent conversational agent designed to improve customer support responsiveness.",
            "business_problem": "Customer support teams were overwhelmed with repetitive queries, leading to long wait times.",
            "tools_used": "Python, OpenAI API, Flask",
            "key_features": "Natural language understanding, automated FAQ resolution, seamless human handoff.",
            "role": "Lead Developer - responsible for backend logic and API integration.",
            "biggest_challenge": "Handling ambiguous user intent without losing conversation context.",
            "what_you_learned": "Learned the importance of prompt engineering and structured conversation flows.",
            "github_link": "https://github.com/lenatao15/chatbot-project",
            "image": "projects/chatbot.png"
        },
        {
            "title": "n8n Agent Workflow Project",
            "summary": "Automated business processes using low-code workflow automation.",
            "business_problem": "Manual data entry between CRM and project management tools was causing errors and delays.",
            "tools_used": "n8n, PostgreSQL, Google Sheets API",
            "key_features": "Real-time data synchronization, automated email notifications, error logging.",
            "role": "Workflow Architect - designed the end-to-end automation logic.",
            "biggest_challenge": "Managing complex branching logic for different lead categories.",
            "what_you_learned": "Gained deep understanding of webhooks and API authentication methods.",
            "github_link": "https://github.com/lenatao15/n8n-workflow",
            "image": "projects/n8n.png"
        },
        {
            "title": "LangChain Agent Project",
            "summary": "A sophisticated AI agent capable of multi-step reasoning and tool usage.",
            "business_problem": "Users needed a way to query structured databases using natural language.",
            "tools_used": "Python, LangChain, SQLite, Streamlit",
            "key_features": "SQL agent for database queries, memory retention, document retrieval.",
            "role": "AI Engineer - implemented the LangChain reasoning engine.",
            "biggest_challenge": "Ensuring the agent didn't hallucinate SQL queries for complex joins.",
            "what_you_learned": "Mastered chain-of-thought prompting and vector store integration.",
            "github_link": "https://github.com/lenatao15/langchain-agent",
            "image": "projects/langchain.png"
        },
        {
            "title": "Google AI Studio Media Project",
            "summary": "Leveraging Gemini models for automated media analysis and content generation.",
            "business_problem": "Content creators lacked tools to quickly summarize and categorize large video libraries.",
            "tools_used": "Google AI Studio, Gemini API, Node.js",
            "key_features": "Video summarization, sentiment analysis, automated thumbnail captioning.",
            "role": "Integration Specialist - connected Gemini API to the media processing pipeline.",
            "biggest_challenge": "Optimizing token usage for long-form video content processing.",
            "what_you_learned": "Explored the capabilities of multimodal models in media contexts.",
            "github_link": "https://github.com/lenatao15/google-ai-media",
            "image": "projects/google_ai.png"
        },
        {
            "title": "Machine Learning Project (scikit-learn)",
            "summary": "Predictive model for identifying patterns in sociology-tech data.",
            "business_problem": "Identifying key factors that influence technology adoption in diverse social groups.",
            "tools_used": "Python, Scikit-learn, Pandas, Matplotlib",
            "key_features": "Data preprocessing, feature engineering, Random Forest classification.",
            "role": "Data Scientist - performed data cleaning and model training.",
            "biggest_challenge": "Dealing with highly imbalanced classes in the social dataset.",
            "what_you_learned": "Learned advanced data imputation and cross-validation techniques.",
            "github_link": "https://github.com/lenatao15/ml-sociology",
            "image": "projects/ml.png"
        },
        {
            "title": "Campus SkillSwap Django Project",
            "summary": "A community-driven platform for students to exchange skills and knowledge.",
            "business_problem": "Students lacked a central hub to find peers for collaborative learning.",
            "tools_used": "Django, Bootstrap, SQLite",
            "key_features": "User profiles, skill matching algorithm, messaging system.",
            "role": "Full Stack Developer - built both the database schema and the frontend.",
            "biggest_challenge": "Implementing an efficient search and filtering system for skills.",
            "what_you_learned": "Deepened knowledge of Django's ORM and template inheritance.",
            "github_link": "https://github.com/lenatao15/campus-skillswap",
            "image": "projects/skillswap.png"
        }
    ]

    for proj in projects_data:
        Project.objects.create(**proj)

    print("Database populated successfully with required projects!")

if __name__ == '__main__':
    populate()
