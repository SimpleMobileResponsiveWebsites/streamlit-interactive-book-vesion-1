import streamlit as st

# Function to display a single page
def display_page(page_number, book_pages):
    st.title(f"Page {page_number + 1}")
    st.write(book_pages[page_number])

# Main application
def main():
    st.sidebar.title("Book Navigation")

    # Sample book content split into manageable strings
    book_pages = [
        """ 
        ### Burst Softare Methodology Written By Nathan Rossow: 
        
        Fast Prototyping For Python Streamlit Web Applications
        
        To create and deploy applications, we are going to use github.com pycharm and streamlit cloud.
            
        ### First Step
        Create a GitHub Account: Ensure you have a GitHub account. If you have a Github.com account, please sign in now.
        If not, sign up and create a github account
        Login to GitHub: Go to GitHub and log in.
        Create a new repository for your streamlit web application.
        Next, enter a name for the repository, choose the gitignore for python and choose next.
            
        ### Second Step
        Create a streamlit.io account.
        Login to streamlit.io.
        When in your streamlit.io account, choose the "Cloud" menu option
        Link your Github.com account to your streamlit cloud account.
            
        ### Third Step:
        Download and install Pycharm Professional
        Link your Pycharm Professional softare with your github account.
        
        ### Fourth Step:
        Open VCSToPDF
        Enter the app version.  The app version is the file name for your application.
        Use a # as a deliminter for each:
        # idea
        # feature
        # function
        # requirement
        # graphical user interface idea
    
        ### Fifth Step:  
        
            
        ### Step 6:  
         
            
        ### Step 7:  
        

        ### Step 8:  
        Download and install Pycharm Professional

        ### Step 9: 

        Open Pycharm Professional 
            
        ### Eighth Step:  
        Using AI,  necessary code for your streamlit web application using the python programming language.
        Run code Using pycharm professional
            
        ### Ninth Step:
        Test the streamlit web application using your local computer and pycharm professional.
            
        ### Tenth Step:
        Repeat steps 8 and 9 until the application is fully working, robust and without error; as to remove any error.
            
        ### Eleventh Step:
        Copy the production ready code base, and create a file in the repository on github.com for the application you will soon deploy on streamlit.io, using streamlit cloud and give it a specificname.py.
        Ensure you name your application as specific or precise as possible to ensure your naming convention follows the usability and functionality of the web application.
            
        ### Twelfth Step:
        Create a requirements.txt file in the repository.  
        Ensure you have the core dependencies in your requirements.txt file and the version of the package or core dependency is up to date with the python version you are deploying your code base with.
            
        ### Thirteenth Step:
        Sign into streamlit.io.
        Choose "Cloud" from the menu if you are not already in the cloud deployment area where you can click "create app"
        Choose "Create App"
            
        ### Fourteenth Step:
        Choose "Deploy a public app from Github"
            
        ### Fifteenth Step:
        Enter the repository link:
        Here is an example:  
        https://github.com/SimpleMobileResponsiveWebsites/general-contracting-apps
        Enter the Branch:
        Use Main if the branch is main.  Otherwise choose precisely or according to your repository tree.
        Choose the Main File Path:
        Here is an example of the application file we created on the Eleventh Step:
        flooringappv1.py
        Enter an App URL:
        Here is an example:
        Flooringappv1
        In the advanced settings, choose *python 3.10 or higher.
        Click the "Deploy" Button
            
        ### Sixteenth Step:
        Your application will appear within 1-2 minutes
        Test your application end to end
        Test your application a few more times.
        Make 100% sure every feature and function works as you have in your design requirements in the initial build out of the application for production and public distribution.
        Streamlit Cloud is an open source data science platform; *share your application with others.  *Create a feedback loop where you get feedback quickl
        Look at chapter 2 in Streamlt Applicaiton Deployment Regression Testing and Software Regression Testing Documentation to avoid recursive error recognition, track bugs, fix bugs, eliminate bugs, and bake quality in at every iteration.
        Lastly, chapter 2, allows to track each iteration, document each iteration of the application, with the application name, python interpreter, code base, regression testing notes, additional code snippets and the pycharm terminal if necessary  *Also, you can compile each iteration into precise documentation, allowing you to code iterations much faster without github, but also using AI, as AI can read text and pickup your project in seconds.

""", """
        ### Use generative AI coding tools to write the code

        **Use the link below to open up a directory of generative AI tools:**

        [Open The AI Coding Tools Directory](https://aicodingtoolsdirectoryv1.streamlit.app/)
        """,
        """
        ### VCSToPDF Tool for Documentation

        **Use the link below to open the VCSToPDF tool:**

        [Open VCSToPDF Tool](https://vcstopdf1v3.streamlit.app/)
        """,
        """
        ### Using ChatGPT or Other AI Tools to Write Code for Your Application

        AI tools like ChatGPT can assist in writing, debugging, and optimizing code. 
        Here are a few tips on how to leverage these tools effectively:

        1. **Define Clear Objectives:** Clearly state what you want the AI to do. Provide detailed prompts.
        2. **Iterative Development:** Use AI to generate code snippets, then iteratively refine and customize them.
        3. **Learn from Suggestions:** Review the AI-generated code to understand the logic and apply it to similar tasks.

        **Start using ChatGPT for coding assistance here:**
        [Explore ChatGPT](https://chat.openai.com/)
        """,
        """
        ### Using Claude.ai for AI-Powered Coding

        Claude.ai is another powerful AI tool for assisting with your coding needs. 
        Here are some ways to utilize Claude.ai effectively:

        1. **Natural Language Coding:** Provide conversational instructions to generate code snippets.
        2. **Debugging and Testing:** Use Claude.ai to identify and fix issues in your code.
        3. **Documentation Support:** Ask Claude.ai to help create clear and concise documentation for your projects.

        **Start using Claude.ai for your projects here:**
        [Explore Claude.ai](https://claude.ai/)
        """,
        """
        ### Using Meta.ai for Advanced AI Solutions

        Meta.ai offers cutting-edge AI tools for diverse applications, including coding. 
        Here are some benefits of using Meta.ai:

        1. **Scalable AI Models:** Leverage Meta.ai's infrastructure for handling complex coding and data analysis tasks.
        2. **Integration Capabilities:** Easily integrate Meta.ai tools into your existing workflows.
        3. **Comprehensive Support:** Access detailed guides and support to make the most of their tools.

        **Start exploring Meta.ai for your development needs here:**
        [Explore Meta.ai](https://meta.ai/)
        """,
        """
        ### Using Google Gemini for AI-Driven Insights

        Google Gemini combines advanced AI technologies to assist developers in creating innovative applications. 
        Here are key features of Google Gemini:

        1. **Cross-Modal Capabilities:** Work with text, images, and other data seamlessly.
        2. **Integrated Ecosystem:** Leverage the power of Google's AI ecosystem for your projects.
        3. **Efficient Problem-Solving:** Use Gemini to analyze data and generate actionable insights quickly.

        **Discover how Google Gemini can empower your applications here:**
        [Explore Google Gemini](https://ai.google/gemini/)
        """,
        """
        ### Burst Software Methodology

        #### Writing the App

        - Use generational AI to write the code using VCSToPDF.
        - Open up Claude.ai.
        - Visit [ChatGPT](https://chat.openai.com/).
        - Access VCSToPDF: [VCSToPDF](https://vcstopdf1v3.streamlit.app/).
        - Enter the Python application name.
        - Include regression testing notes.

        In the code area, use delimiters for each idea, feature, function, requirement, and graphical user interface functionality.

        #### Testing the App

        - Test the app as quickly as possible.
        - Fast iterations are important in rapid prototyping.
        - Complete end-to-end testing of the application before releasing the product.

        #### Documenting the App for Version Control and Local Storage

        1. Document the end-to-end testing so others can validate and verify what tests have been completed.
        2. Use VCSToPDF to:
           - Document the app version.
           - Include regression testing notes.
           - Capture terminal outputs.
           - Archive code bases.
        """,
        """
        ### Creating and Managing Project Repositories

        #### New Project Repository Setup

        When starting a new project, follow these best practices for repository creation and management:

        1. **Creating a New Repository for Fresh Projects**
        - Initialize a new Git repository with `git init`
        - Create a `.gitignore` file tailored to your project's technology stack
        - Set up a clean `requirements.txt` with only essential dependencies
        - Use virtual environments to isolate project dependencies
        
        Example workflow:
        ```bash
        # Create project directory
        mkdir new-project
        cd new-project

        # Initialize Git
        git init

        # Create virtual environment
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

        # Generate requirements.txt
        pip freeze > requirements.txt
        ```

        2. **Refactoring and Transpiling Existing Codebases**
        - Create a new repository for the refactored project
        - Use tools like `2to3` for Python version migrations
        - Leverage AI tools for code analysis and transformation
        - Maintain version control and document changes carefully

        3. **Best Practices**
        - Always use semantic versioning
        - Include comprehensive README documentation
        - Set up continuous integration (CI) workflows
        - Regularly update dependencies
        - Use branch protection rules in shared repositories
        """,
        """
        ### DevOps and Deployment Strategies for Modern Applications

        #### Continuous Integration and Continuous Deployment (CI/CD)

        **Key CI/CD Principles:**
        1. **Automated Testing**
        - Implement comprehensive unit, integration, and end-to-end tests
        - Use tools like GitHub Actions, Jenkins, or GitLab CI
        - Automate test runs on every code push

        **Deployment Workflows:**
        ```yaml
        # Example GitHub Actions workflow
        name: Python application
        on: [push, pull_request]

        jobs:
          build:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v2
            - name: Set up Python
              uses: actions/setup-python@v2
              with:
                python-version: 3.9
            - name: Install dependencies
              run: |
                python -m pip install --upgrade pip
                pip install -r requirements.txt
            - name: Run tests
              run: |
                pytest tests/
        ```

        #### Container Deployment Strategies

        **Docker Containerization**
        - Create lightweight, portable application containers
        - Use multi-stage builds for optimized images
        - Implement container orchestration with Kubernetes

        Example Dockerfile:
        ```dockerfile
        # Use an official Python runtime as a parent image
        FROM python:3.9-slim

        # Set the working directory in the container
        WORKDIR /app

        # Copy the current directory contents into the container
        COPY . /app

        # Install any needed packages specified in requirements.txt
        RUN pip install --no-cache-dir -r requirements.txt

        # Make port 8000 available to the world outside this container
        EXPOSE 8000

        # Define environment variable
        ENV NAME World

        # Run the application
        CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
        ```

        #### Cloud Deployment Platforms

        **Key Platforms:**
        - **AWS Elastic Beanstalk:** Simple web application deployment
        - **Google Cloud Run:** Serverless container deployment
        - **Heroku:** Quick deployment for small to medium projects
        - **DigitalOcean App Platform:** Simplified cloud deployment

        #### Monitoring and Observability

        **Essential Monitoring Tools:**
        - Prometheus for metrics collection
        - Grafana for visualization
        - ELK Stack (Elasticsearch, Logstash, Kibana) for log management
        - Sentry for error tracking and performance monitoring

        **Best Practices:**
        - Implement comprehensive logging
        - Set up real-time alerts
        - Monitor application performance metrics
        - Use distributed tracing for complex microservices
        """,
        """
        ### Advanced Repository Management Techniques

        #### Creating New Repositories for Different Project Scenarios

        1. **Fresh Project Repository Initialization**
        
        **Workflow for New Projects:**
        ```bash
        # Create a new project directory
        mkdir my-new-project
        cd my-new-project

        # Initialize Git repository
        git init

        # Create a comprehensive .gitignore
        curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

        # Set up virtual environment
        python3 -m venv venv
        source venv/bin/activate

        # Create a structured project layout
        mkdir -p src tests docs
        touch README.md requirements.txt setup.py
        ```

        2. **Managing Requirements for Different Projects**

        **Creating Specialized Requirements Files:**
        ```bash
        # Development requirements
        pip freeze > requirements-dev.txt

        # Production requirements
        pip freeze > requirements-prod.txt

        # Create a base requirements file
        echo "# Base requirements
        requests==2.26.0
        numpy==1.21.2
        pandas==1.3.3" > requirements.txt
        ```

        3. **Refactoring and Transpiling Existing Codebases**

        **Strategies for Code Migration:**
        - Use `2to3` for Python 2 to Python 3 migration
        - Leverage AI-powered refactoring tools
        ```bash
        # Migrate Python 2 code to Python 3
        2to3 -w old_project/
        ```

        **AI-Assisted Refactoring Workflow:**
        1. Use Claude.ai or ChatGPT to analyze code structure
        2. Identify potential improvements and migration paths
        3. Generate refactoring suggestions
        4. Apply changes incrementally
        5. Validate with comprehensive test suites

        #### Best Practices for Repository Management

        - **Version Control:**
          - Use meaningful commit messages
          - Implement branching strategies (GitFlow, trunk-based development)
          - Use semantic versioning (MAJOR.MINOR.PATCH)

        - **Documentation:**
          - Maintain clear README files
          - Use inline code comments
          - Generate API documentation automatically
          - Create CHANGELOG.md for tracking changes

        - **Dependency Management:**
          - Use virtual environments
          - Regularly update and audit dependencies
          - Use tools like Dependabot for automatic updates
          - Pin dependency versions for reproducibility

        **Pro Tip:** Always test thoroughly after refactoring or migrating code bases to ensure functionality remains intact.
        """, """
        ### Using Generative AI To Read App Version, Interpreter, Terminal Inputs And Code Bases For Fast Prototypying 

        #### Using Generative AI To Read:
          - App Version
          - Managing Requirements for Different Projects
          - Refactoring and Transpiling Existing Codebases
        
        """, """
        ### Streamlit | Streamlit Cloud | A Faster Way To Build Apps

        ### Write about the impact of streamlit after learning 12 programming languages:
          - How different programming languages impact different tech stacks
          - What different programming languages can create
          - What you learn when your coding the same project in different programming languages, a pattern emerges
        
        """, """
        ### Write about software testing, software testing documentation, compiling the:

        #### softare testing fundamentals:
          - App version 
          - Interpreter
          - Regression testing notes
          - Terminal inputs
          - Code base
          - end to end testing

        
        """, """
        ### Repository | Branch Name | File Name | App URL - Name Of Application | Python Version - Advanced Settings

        ### Softare testing fundamentals:
          - Repository 
          - Branch Name 
          - File Name
          - App URL - Name Of Application
          - Python Version - Advanced Settings


        
        """, """
        ### Deploy An Application On Streamlit Cloud

        ### Streamlit Python Web Application Deployment Fundamentals:
         - write about deploying applications on streamlit cloud for free
         - write about testing applications using steamlit cloud for free using vcstopdf designed by Nathan Rossow at Burst Software



        
        """, """
        ### Deploy A Public App From Github.com to Streamlit Cloud using a github repository

        #### talk about everything that comes along with deployong an open source software application using a public github repository:
         - explain what a open source github repository is
         - explain what an public application is
         - explain what it means to deploy a public, open source application using a github repository



        
        """, """
        ### Creating A Requirements.txt File | Github.com

        #### talk about the fundamentals of what a requirements.txt file is
         -  talk about creating the requirements.txt file
         - explain what an public application is
         -  talk about creating the requirements.txt file



        
        """, """
        ### Creating A New Repository | Github.com

        ### Talk about creating a new repository
         -  talk about creating the requirements.txt file
         - explain what an public application is
         -  talk about creating the requirements.txt file



        
        """, """
        ### Create An App using Streamlit Cloud And Github.com

        ### write about creating any application using streamlit cloud, streamlit framework github.com and generative AI methods, and burst software
         -  creating an application using streamlit cloud
         - explain the streamlit framework
         -  talk about generative ai methods
         - talk about vcstopdf designed by burst software



        
        """, """
        ### Create A New File | Github.com

        ###  talk about how to create a new file within a repository on github.com
         - explain the steps to creating a new file in a repository using github
         - explain how to save the file when programming in the python language




        
        """, """
        ### Create A Codebase and Give It A Name 

        ###   talk about writing code
         -  talk about testing code
         -  talk about documenting code base regression testing
         -   talk about the codebase readability by using the .pdf based vcs that allows AI to read the codebase, app version, interpreter, regression testing notes and terminal inputs 




        
        """,   
    ]

    # Number of pages in the book
    total_pages = len(book_pages)

    # Table of Contents (TOC)
    st.sidebar.write("**Table of Contents:**")
    for i, content in enumerate(book_pages):
        if st.sidebar.button(f"Page {i + 1}"):
            st.session_state["page_number"] = i

    # Initialize page_number in session state
    if "page_number" not in st.session_state:
        st.session_state["page_number"] = 0

    # Display the selected page
    display_page(st.session_state["page_number"], book_pages)

if __name__ == "__main__":
    main()
