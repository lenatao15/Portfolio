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
        about_me="""I’m originally from Ukraine and currently pursuing my degree in Information Systems in the U.S. Moving to a new country challenged me to adapt quickly to a new language, culture, and academic system.

Along the way, I’ve developed not only technical skills in data and systems, but also resilience, independence, and the ability to learn fast in unfamiliar environments.

Outside of work, I enjoy painting, traveling, and music — creative outlets that help me stay balanced and curious.""",
        email="Olena_makarova1@baylor.edu",
        phone="(707) 413-5847",
        linkedin="https://www.linkedin.com/in/olena-makarova-a10687198/",
        github="https://github.com/lenatao15/"
    )

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
        gpa="",
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
    Certification.objects.create(
        name="IBM Build an AI Agent Certificate",
        description="Mastered the architecture and deployment of intelligent AI agents. This certification from IBM focuses on designing multi-step agentic workflows, prompt engineering, and integrating AI models into practical business applications to enhance decision-making and productivity.",
        static_image_path="portfolio/images/certifications/BuildAnAIAgent.PNG"
    )
    Certification.objects.create(
        name="IBM Enterprise Design Thinking Certificate",
        description="Developed a deep understanding of human-centered design principles within a large-scale corporate environment. Learned how to facilitate collaborative problem-solving, identify user needs through empathy mapping, and iterate on solutions that align business goals with user experience.",
        static_image_path="portfolio/images/certifications/IBM_enterprice_design_thinking.PNG"
    )
    Certification.objects.create(
        name="IBM Risk Management Certificate",
        description="Explored the methodologies and frameworks used to identify, assess, and mitigate risks in a business context. The course covered quantitative and qualitative risk analysis, strategy formulation, and the implementation of controls to protect organizational assets and ensure business continuity.",
        static_image_path="portfolio/images/certifications/RiskManagement.PNG"
    )
    Certification.objects.create(
        name="HRCI Human Resource Associate Specialization Certificate",
        description="Gained foundational knowledge in human resource management, including recruitment, employee relations, and compliance. This specialized certificate from HRCI validates expertise in the core functions of HR and the legal frameworks governing the workplace.",
        static_image_path="portfolio/images/certifications/HRCI.PNG"
    )

    # Projects
    Project.objects.all().delete()
    
    projects_data = [
        {
            "title": "Chatbot Project",
            "summary": "An intelligent conversational agent created using Chatbase to improve customer support responsiveness.",
            "business_problem": "Customer support teams were overwhelmed with repetitive queries, leading to long wait times.",
            "tools_used": "Chatbase, GPT-4, Custom Knowledge Base",
            "key_features": "Trained on specific business documentation, real-time natural language understanding, and automated FAQ resolution.",
            "role": "Lead Architect - responsible for data curation, model training via Chatbase, and UI integration.",
            "biggest_challenge": "Refining the knowledge base to ensure high accuracy in technical responses.",
            "what_you_learned": "Mastered the process of creating custom AI assistants through Chatbase, focusing on data-driven response generation.",
            "github_link": "",
            "icon_class": "bi-chat-dots-fill",
            "static_image_1": "portfolio/video/chatbase.png"
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
            "github_link": "",
            "demo_link": "https://docs.google.com/forms/d/e/1FAIpQLSeEDjPBJRxDx7y1x_tWTPIGi6OjiMHO0WYfAqr8fK5ZxQ9MDA/viewform?usp=dialog",
            "icon_class": "bi-diagram-3-fill",
            "static_image_1": "portfolio/video/Orchestrator.png",
            "static_image_2": "portfolio/video/emailJack.png"
        },
        {
            "title": "LangChain (HandyMan) Project",
            "summary": "A sophisticated AI agent capable of multi-step reasoning and tool usage for service automation.",
            "business_problem": "Users needed a way to query structured databases and automate service coordination using natural language.",
            "tools_used": "Python, LangChain, SQLite, Streamlit",
            "key_features": "SQL agent for database queries, service listings, user reviews, and booking management.",
            "role": "AI Engineer & Lead Developer - implemented the LangChain reasoning engine and architected the service flow.",
            "biggest_challenge": "Implementing a real-time availability calendar while ensuring the agent didn't hallucinate SQL queries.",
            "what_you_learned": "Mastered chain-of-thought prompting and improved proficiency in complex relational database design.",
            "github_link": "https://github.com/lenatao15/Handyman",
            "icon_class": "bi-robot"
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
            "github_link": "",
            "icon_class": "bi-play-btn-fill",
            "video_static_path": "portfolio/video/joker.mp4"
        },
        {
            "title": "Machine Learning Project (LearningLog)",
            "summary": "A collection of predictive modeling scripts focused on California housing prices and vehicle fuel efficiency.",
            "business_problem": "Predicting complex outcomes like housing market trends and fuel consumption requires clean data and robust regression models. These projects demonstrate the practical application of Linear Regression to real-world datasets.",
            "tools_used": "Python, Scikit-learn, Pandas, Matplotlib, Hugging Face Datasets",
            "key_features": """ml2.py: California Housing Prediction
  This script performs a multiple linear regression to predict median house values in    
  California.
   * Data Exploration: Used pandas to analyze the California Housing dataset, printing   
     shapes, feature names, and descriptive statistics.
   * Modeling: Split the data into training (75%) and testing (25%) sets, then trained a 
     LinearRegression model.
   * Insights: Calculated the coefficients for each feature (e.g., MedInc, HouseAge),    
     showing how much each factor impacts the price.
   * Visualization: Created a scatter plot comparing Expected vs. Predicted prices with a
     diagonal line to visualize model accuracy.

  ml3.py: Auto MPG Prediction
  This script applies linear regression to the \"Auto MPG\" dataset to predict vehicle fuel  
  efficiency.
   * Data Loading: Utilized the datasets library to fetch the Auto MPG dataset from Hugging
     Face.
   * Modeling: Trained a LinearRegression model on vehicle characteristics to predict miles
     per gallon (MPG).
   * Validation: Compared actual MPG values against predicted ones and printed a sample of 
     the results (e.g., Actual: 28.00 Predicted: 29.15).
   * Visualization: Generated a plot of Actual vs. Predicted MPG to assess how closely the 
     model's predictions align with reality.""",
            "role": "Lead Data Scientist - developed the full pipeline from data fetching to visualization for both projects.",
            "biggest_challenge": "Managing data from different sources (local CSV vs. Hugging Face API) and ensuring consistent feature scaling for regression accuracy.",
            "what_you_learned": "Strengthened my understanding of linear regression coefficients and learned how to leverage multimodal datasets for predictive analytics.",
            "github_link": "https://github.com/lenatao15/LearningLogProject",
            "icon_class": "bi-cpu-fill",
            "static_image_1": "portfolio/images/projects/Figure_3_ml2.png",
            "static_image_2": "portfolio/images/projects/Figure_4_ml2.png",
            "static_image_3": "portfolio/images/projects/Figure_1_ml3.png",
            "static_image_4": "portfolio/images/projects/Figure_2_ml3.png"
        },
        {
            "title": "SkillSwamp",
            "summary": "Where students trade talents and grow together! 🐸✨",
            "business_problem": "Let's be real: college is expensive, but we're all experts at something! SkillSwamp was born from the idea that a student who's a pro at Python should be able to 'trade' that knowledge for some guitar lessons or help with a marketing project. No money, just pure talent exchange.",
            "tools_used": "Django, Python, Bootstrap, SQLite",
            "key_features": "- Personalized Profile: Show off what you know and what you want to learn.\n- Skill Matching: Our algorithm finds the perfect swap partner for you.\n- Direct Messaging: Chat with your future mentor or student right on the platform.\n- Community Feed: See what the swamp is buzzing about!",
            "role": "I built this from the ground up! From the initial 'what if' to the final 'it works!', I handled the backend logic, the database design, and made sure the UI felt friendly and welcoming.",
            "biggest_challenge": "Building a fair exchange system. How do you measure a 'unit' of skill? We decided to keep it informal and trust-based, which actually made the community much tighter!",
            "what_you_learned": "Community-driven tech is the best tech. I learned a ton about user experience and how to build features that people actually want to use every day.",
            "github_link": "https://github.com/lenatao15/campus_skillswamp",
            "icon_class": "bi-people-fill",
            "static_image_1": "portfolio/images/projects/skillswamp1.PNG",
            "static_image_2": "portfolio/images/projects/skillswamp2.PNG",
            "static_image_3": "portfolio/images/projects/skillswamp3.PNG",
            "static_image_4": "portfolio/images/projects/skillswamp4.PNG"
        }
    ]

    for proj in projects_data:
        Project.objects.create(**proj)

    print("Database populated successfully with required projects!")

if __name__ == '__main__':
    populate()
