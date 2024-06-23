import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load Lottie animations
def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

# Function to save form data locally
def save_form_data(name, email, message):
    data = {
        "name": name,
        "email": email,
        "message": message
    }
    with open("form_submissions.json", "a") as f:
        json.dump(data, f)
        f.write("\n")
    return True

# Function to load form submissions
def load_form_submissions():
    submissions = []
    try:
        with open("form_submissions.json", "r") as f:
            for line in f:
                submissions.append(json.loads(line))
    except FileNotFoundError:
        pass
    return submissions

# Set page config
st.set_page_config(page_title="Hazrat Alkozai - Resume", page_icon=":briefcase:", layout="wide")

# Custom CSS for styling
def custom_css():
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {
            margin-top: 120px;
        }
        .section {
            padding: 40px 0;
            margin-top: 300px;
        }
        .nav-trigger {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 200px;
            z-index: 500;
        }
        .nav-container {
            position: fixed;
            top: -100px;
            left: 0;
            right: 0;
            height: 60px;
            background-color: rgba(0, 0, 0, 0);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            transition: top 0.3s ease-in-out;
        }
        .nav-trigger:hover + .nav-container, .nav-container:hover {
            top: 60px;
            height: 60px;
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
        }
        .nav-button {
            margin: 0 15px;
            padding: 10px 15px;
            background-color: transparent;
            color: #90EE90 !important;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
            text-decoration: none !important;
        }
        .nav-button:hover {
            background-color: rgba(255, 255, 255, 0.1);
            color: #FF6B6B !important;
        }

    </style>
    """, unsafe_allow_html=True)

# Content sections
def who_am_i():
    st.markdown('<div id="who-am-i">', unsafe_allow_html=True)

    # Navigation trigger and container
    st.markdown("""
    <div class="nav-trigger"></div>
    <div class="nav-container">
        <div class="nav-buttons">
            <a href="#who-am-i" class="nav-button">Who Am I</a>
            <a href="#experience" class="nav-button">Experience</a>
            <a href="#skills" class="nav-button">Skills</a>
            <a href="#certifications" class="nav-button">Certifications</a>
            <a href="#projects" class="nav-button">Projects</a>
            <a href="#references" class="nav-button">References</a>
            <a href="#contact-me" class="nav-button">Contact Me</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.header("Hazrat Alkozai")
    st.subheader("IT Professional | Cybersecurity Enthusiast")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("""
        As an aspiring cybersecurity enthusiast completing an Associate's degree in Cybersecurity (August 2024), 
        I offer a robust skill set enhanced by Security+, CCNA, and Google cybersecurity certificates. My expertise
         encompasses critical security tools including Wireshark, Nmap, Burpsuite, Active Directory, Entra ID, and 
         Splunk. complemented by experience in Python, Bash, and PowerShell scripting. 
         With a proven track record of supporting multiple 
         client accounts simultaneously, I have developed strong incident response and prioritization skills. 
         My comprehensive understanding of compliance frameworks such as NIST, ISO 27001, HIPAA,MITRE ATT&CK, and PCI DSS 
         ensures alignment with industry standards. Leveraging hands-on experience in threat hunting 
         and system hardening, coupled with leadership in a coding club, I am well-equipped to contribute effectively
          to a SOC team. My commitment to continuous learning and adapting to emerging threats positions me to make
           an immediate impact in safeguarding an organization's digital assets.
        """)
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""
        I've also recently started a YouTube channel called Xen, where I create videos to stay up-to-date with the latest trends 
        in cybersecurity and share my knowledge with the community. Check it out to see my latest insights and tutorials!
        """)

        st.markdown("""
        <a href="https://www.youtube.com/channel/UClmIaoPCeXW0kGMdFJgOZWQ" target="_blank">
            <button style="
                background-color: #FF0000;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            ">
                Visit My YouTube Channel
            </button>
        </a>
        """, unsafe_allow_html=True)

    with col2:
        lottie_first = load_lottiefile("lot/main.json")
        st_lottie(lottie_first)


    lottie_scroll = "lot/scroll.json"
    lottie_json = load_lottiefile(lottie_scroll)
    if lottie_json:
        st_lottie(lottie_json, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

def experience():
    st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
    st.header("Professional Experience")

    st.subheader("Service Desk Analyst | Bell TechLogix")
    st.write("January 2023 – April 2024")
    ecol1, ecol2 = st.columns([2, 1])
    with ecol1:
        st.write("""
        - Responded to 600+ monthly service tickets spanning inquiries to critical outages.
        - Routed and escalated intricate tickets to appropriate tiers with detailed documentation.
        - Maintained customer satisfaction and QA score above 92 percent through enhanced communications.
        - Performed hands-on troubleshooting remotely for 9 different client accounts to assist with desktop, server, security, network and application issues.
        - Safeguarded protected resources by cross-checking multi-factor identification, approving credential issuance per cybersecurity guidelines.
        - Managed user accounts including password resets, account unlocks, onboardings, and offboardings through Active Directory and Azure Entra ID.
        - Utilized Office 365 admin center and Microsoft Exchange to manage distribution groups, shared mailboxes, and teams groups.
        - Conducted regular security audits of user lists to ensure compliance with cybersecurity protocols.
        - Implemented and maintained security measures to protect against potential threats and vulnerabilities.
        """)

        st.subheader("Desktop Support Technician | American Rescue Rooters Heating and Cooling")
        st.write("June 2022 – November 2022")
        st.write("""
        - Provided Tier 1 and Tier 2 technical support.
        - Installed and configured new PC hardware and software on desktops and peripherals such as printers, external drives, and other related hardware.
        - Documented calls and created tickets utilizing ConnectNow ticketing utility.
        - Proficiently troubleshot and resolved problems on desktop computers, laptop computers and applications or software.
        - Conducted security assessments on newly installed hardware and software to ensure compliance with company security policies.
        - Implemented and maintained endpoint security solutions to protect against malware and other cyber threats.
        """)
    with ecol2:
        lottie_scnd = load_lottiefile("lot/second.json")
        st_lottie(lottie_scnd, height=500, width=300, )

    st.subheader("Help Desk Analyst | Alkozai Transit LLC")
    st.write("June 2021 – June 2022")
    st.write("""
    - Provided Tier 1 and Tier 2 Technical Assistance.
    - Maintained documentation and SOPs, ensuring they were up-to-date with the latest security practices.
    - Documented calls, created tickets, and provided ticket numbers for reference using ServiceNow.
    - Troubleshot and repaired hardware and network issues, ensuring secure configurations were maintained.
    - Performed specific hardware and software maintenance, such as upgrades, virus scans, and system migrations.
    - Installed, configured, and updated end-user desktop and laptop software, ensuring all security patches were applied.
    - Implemented and maintained security measures to protect against potential cyber threats during software installations and updates.
    """)

    st.subheader("Cashier | Sheetz")
    st.write("June 2020 – June 2021")
    st.write("""
    - Greeted customers entering and leaving the establishment.
    - Used POS hardware and software associated with running transactions or returns.
    - Answered customers' questions and provided information on procedures or policies.
    - Complied with all cash handling procedures, safety, and loss prevention policies.
    - Maintained awareness of potential security risks in the retail environment.
    - Followed strict data protection protocols when handling customer information during transactions.
    """)

    lottie_scroll2 = load_lottiefile("lot/scroll.json")
    st_lottie(lottie_scroll2, height=300)

    st.markdown('</div>', unsafe_allow_html=True)

def skills():
    st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
    st.header("Skills")

    # Technical Skills
    st.subheader("Technical Skills")
    technical_skills = [
        "Security Information and Event Management (SIEM)",
        "Log Analysis and Correlation",
        "Intrusion Detection/Prevention Systems (IDS/IPS)",
        "Firewall Configuration and Management",
        "Network Protocol Analysis (e.g., TCP/IP)",
        "Vulnerability Assessment",
        "Endpoint Detection and Response (EDR)",
        "Windows and Linux Operating Systems",
        "Active Directory Basics",
        "Entra ID",
        "ITIL",
        "ITSM",
        "SQL",
        "Tier 3 Troubleshooting",
        "Identity and Access Management (IAM)",
        "Scripting (Python, PowerShell, Bash)",
        "Network Security Monitoring",
        "Incident Response Procedures",
        "Threat Intelligence Platforms",
        "Basic Digital Forensics",
        "Security Frameworks (e.g., NIST, MITRE ATT&CK)",
        "Cloud Security Fundamentals (AWS, Azure, GCP)",
        "Network Traffic Analysis (e.g., Wireshark)",
        "Security Automation and Orchestration Basics"
    ]

    col1, col2 = st.columns(2)

    for i, skill in enumerate(technical_skills):
        if i % 2 == 0:
            col1.write(f"- {skill}")
        else:
            col2.write(f"- {skill}")

    # Soft Skills
    st.subheader("Soft Skills")
    soft_skills = [
        "Analytical Thinking", "Problem-Solving", "Attention to Detail", "Continuous Learning",
        "Effective Communication", "Teamwork & Collaboration", "Adaptability", "Time Management",
        "Ethical Behavior", "Stress Management", "Critical Thinking", "Decision Making under Pressure",
        "Documentation & Reporting", "Presentation Skills", "Risk Assessment", "Incident Response Coordination"
    ]

    col1, col2 = st.columns(2)

    for i, skill in enumerate(soft_skills):
        if i % 2 == 0:
            col1.write(f"- {skill}")
        else:
            col2.write(f"- {skill}")

    col1, col2 = st.columns(2)

    with col1:
        lottie_3 = load_lottiefile("lot/skill.json")
        st_lottie(lottie_3, height=300, width=500)

    with col2:
        lottie_4 = load_lottiefile("lot/comp.json")
        st_lottie(lottie_4, height=300, width=500)

    lottie_5 = load_lottiefile("lot/scroll.json")
    st_lottie(lottie_5, height=300)

    st.markdown('</div>', unsafe_allow_html=True)

def certifications():
    st.markdown('<div id="certifications" class="section">', unsafe_allow_html=True)
    lottie_6 = load_lottiefile("lot/trp.json")
    st_lottie(lottie_6, height=300)
    st.header("Certifications and Awards")
    cert_list = [
        ("Connect and Protect: Networks and Network Security", "Google", "February 2024", "CKXU6R3HDL82"),
        ("Tools of the Trade: Linux and SQL", "Google", "February 2024", "FRCREY2XC9NQ"),
        ("CCNA 200-301", "Cisco", "February 2024", "CSCO14536882"),
        ("Certificate of Appreciation", "Bell TechLogix", "January 2024", "BTL"),
        ("Bell Ringer", "Bell TechLogix", "September 2023", "BTL"),
        ("Play It Safe: Manage Security Risks", "Google", "September 2023", "JMK9D82XJ5F9"),
        ("Foundations of Cybersecurity", "Google", "August 2023", "584QTHP6NAMB"),
        ("CompTIA Sec+", "CompTIA", "July 2023", "COMP001022188345")
    ]

    for cert, issuer, date, creds in cert_list:
        st.subheader(cert)
        st.write(f"Issued by: {issuer}")
        st.write(f"Date: {date}")
        st.write(f"Credentials: {creds}")
        st.write("---")
    st.markdown('</div>', unsafe_allow_html=True)
    lottie_7 = load_lottiefile("lot/scroll.json")
    st_lottie(lottie_7, height=300)

def projects():
    st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
    lottie_8 = load_lottiefile("lot/prjct.json")
    st_lottie(lottie_8, height=300)
    st.header("Projects")


    st.subheader("Resume Portfolio Website")
    st.write("Streamlit, Python | June 2024")
    st.write("""
    - Designed and developed an interactive resume portfolio website using Streamlit and Python.
    - Implemented various Streamlit features to create a user-friendly interface showcasing skills, experience, and projects.
    - Utilized version control (Git) and deployed the application for public access.
    - Demonstrated proficiency in web development, Python programming, and data presentation.
    """)

    st.subheader("OpenVPN-based Virtual Private Network")
    st.write("OpenVPN, Cloud Services, Network Security | Jan 2023")
    st.write("""
    - Set up a custom OpenVPN server on a PhoenixNap cloud instance for secure networking testing purposes.
    - Configured the OpenVPN server-side application with basic encryption protocols and certificate-based authentication.
    - Developed a tailored configuration using AES encryption and point-to-point topology for personal VPN use.
    - Installed and configured the OpenVPN client app on personal devices, successfully establishing an encrypted tunnel.
    - Conducted connection testing to confirm secure traffic routing, enabling controlled experimentation and evaluation.
    """)

    st.subheader("Local Isolated Network")
    st.write("Network Design, Vulnerability Assessment, Linux, Windows server | January 2024")
    st.write("""
    - Set up a customized virtual environment using VirtualBox and VMWare for controlled security research, employing tools
    such as Pen VAS, Nessus, Metasploitable boxes, Metasploit, and NVD for vulnerability assessments, scanning, exploit
    testing, and CVE tracking.
    - Maintained an inventory of technologies, scan results, remediation efforts, and security improvements, coordinated
    responsible disclosure when necessary, and continuously monitored industry best practices to ensure the highest ethical
    standards in vulnerability evaluation.
    """)

    st.subheader("Custom Windows Operating System Images")
    st.write("Windows Server, NTLite, VAPT | June 2023")
    st.write("""
    - Leveraged advanced NTLite software capabilities to deeply customize and optimize Windows operating system images for
    enhanced performance, security, and functionality testing across virtualized environments.
    - Carefully validated infrastructure impacts of component addition or removal by building hardened or vulnerable images
    and thoroughly evaluating post-deployment. Conducted fine-grained configuration of drivers, services, features, and OOBE
    flows to match deployment requirements, then assessed images within isolated VMs for testing and educational purposes.
    """)

    st.subheader("Python Automation Tool")
    st.write("Python, Tkinter | December 2023")
    st.write("""
    - Developed a custom Python-based GUI productivity tool with Tkinter, featuring an intuitive interface, automated triggers,
    and client-specific functions, resulting in significant time savings and efficiency gains for multiple client accounts.
    """)

    st.subheader("Cybersecurity YouTube Channel - Xen")
    st.write("Content Creation, Cybersecurity Trends | Ongoing")
    st.write("""
    - Created and maintain a YouTube channel called "Xen" focused on cybersecurity topics and trends.
    - Regularly produce and publish videos discussing the latest developments in cybersecurity, tools, techniques, and best practices.
    - Engage with the cybersecurity community, sharing insights and staying up-to-date with industry trends.
    """)

    st.subheader("Coding Club Leadership")
    st.write("Python, Project Management | Ongoing")
    st.write("""
    - Lead a coding club, organizing regular meetings and workshops to enhance programming skills.
    - Implement various projects in Python and other languages, focusing on practical applications in cybersecurity.
    - Foster a collaborative learning environment, encouraging knowledge sharing and problem-solving among club members.
    """)
    lottie_9 = load_lottiefile("lot/scroll.json")
    st_lottie(lottie_9, height=300)
    st.markdown('</div>', unsafe_allow_html=True)
def references():
    st.markdown('<div id="references" class="section">', unsafe_allow_html=True)
    lottie_11 = load_lottiefile("lot/ref.json")
    st_lottie(lottie_11, height=300)
    st.header("References")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Michael Conner")
        st.write("**Title:** Team Manager")
        st.write("**Company:** Bell TechLogix")
        st.write("**Phone:** (580) 318-5366")
        st.write("**Email:** mconner@belltechlogix.com")

    with col2:
        st.subheader("Mark Heller")
        st.write("**Title:** Associate Operations Manager")
        st.write("**Company:** Bell TechLogix")
        st.write("**Phone:** (850) 207-1274")
        st.write("**Email:** mheller@belltechlogix.com")


    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Additional references available upon request.")
    lottie_10 = load_lottiefile("lot/scroll.json")
    st_lottie(lottie_10, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

def download_resume():
    st.markdown('<div id="download-resume" class="section">', unsafe_allow_html=True)

    # Center the button using columns
    col1, col2, col3 = st.columns([4, 3, 2])

    with col2:
        # Path to your resume file
        resume_path = "resume/resume.pdf"

        # Read file as bytes
        with open(resume_path, "rb") as file:
            pdf_bytes = file.read()

        # Create download button
        st.download_button(
            label="Download Resume",
            data=pdf_bytes,
            file_name="Hazrat_Alkozai_Resume.pdf",
            mime="application/pdf"
        )

    st.markdown('</div>', unsafe_allow_html=True)

def contact_me():
    st.markdown('<div id="contact-me" class="section">', unsafe_allow_html=True)
    lottie_12 = load_lottiefile("lot/ctct.json")
    st_lottie(lottie_12, height=300)
    st.header("Contact Me")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Location:** Woodbridge, Virginia")
        st.write("**Phone:** 571-552-7086")
        st.write("**Email:** hazratalkozai2020@gmail.com")

    with col2:
        st.write("**LinkedIn:** [linkedin.com/in/hazratalkozai/](https://linkedin.com/in/hazratalkozai/)")
        st.write("**GitHub:** [github.com/Stamper221](https://github.com/Stamper221)")

    # Contact form
    st.subheader("Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name and email and message:
                if save_form_data(name, email, message):
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("There was an error saving your message. Please try again later.")
            else:
                st.warning("Please fill out all fields before submitting.")
    st.markdown('</div>', unsafe_allow_html=True)



def admin_login():
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "shai" and password == "Stamper$321":
            st.session_state.admin_logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Unauthorized access. Invalid username or password.")

def admin_page():
    st.title("Admin Page - Form Submissions")
    submissions = load_form_submissions()
    for submission in submissions:
        st.write(f"Name: {submission['name']}")
        st.write(f"Email: {submission['email']}")
        st.write(f"Message: {submission['message']}")
        st.write("---")

# Main content
def main():
    custom_css()

    # Admin button
    admin_col = st.columns([1000, 100])[0]  # This will push the button to the right
    with admin_col:
        if st.button("Admin", key="admin_button", help="Admin only please, do not click!"):
            st.session_state.admin_button_clicked = True
            st.experimental_rerun()

    # Check if admin login button was clicked
    if st.session_state.get('admin_button_clicked', False):
        if st.session_state.get('admin_logged_in', False):
            admin_page()
        else:
            admin_login()
    else:
        # Content sections
        who_am_i()
        experience()
        skills()
        certifications()
        projects()
        references()
        download_resume()
        contact_me()


if __name__ == "__main__":
    main()
