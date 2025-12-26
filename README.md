🕉️ Bhagavad Gita AI: Philosophical Wisdom Engine
This project is a specialized AI-powered chatbot designed to provide thoughtful, concise, and authentic guidance based on the teachings of the Bhagavad Gita. Unlike generic chatbots, this engine is "grounded" in specific philosophical context to ensure responses remain true to the original scriptures.

<img width="1080" height="555" alt="image" src="https://github.com/user-attachments/assets/9c44d00e-3157-49d3-98a4-4616de35bbdf" />

🚀 The Vision
In an era of information overload, this tool serves as a "Digital Guru." It bridges the gap between ancient wisdom and modern problems by using Generative AI to interpret and apply Gita principles to user-specific questions.

🛠️ Technical Deep-Dive
1. Grounded Generation (Prompt Engineering)
The core logic in codeB.py uses a sophisticated System Prompt that acts as a guardrail. It instructs the LLM to:

* Strictly adhere to the teachings of the Bhagavad Gita.

* Include relevant Chapter and Verse numbers.

* Translate complex Sanskrit concepts into simple, modern language.

* Provide a guiding principle if a direct answer isn't available, preventing "hallucinations."

2. Modern Frontend Architecture

* The UI is built with Streamlit, featuring a custom CSS injection to create a high-contrast, immersive user experience:

* Dynamic Backgrounds: Uses Base64 encoding to serve high-quality imagery without external hosting dependencies.

* Vibrant UI: Custom-styled floating cards, gold-toned headers, and high-readability text containers.

* State Management: Utilizes st.session_state to maintain the conversation flow between user inputs.

3. Production-Ready Backend
* Logging: A custom logging_setup.py tracks every query and system event in server.log, essential for monitoring AI behavior in a production environment.

* Security: Decoupled API management via openai_helper.py to keep sensitive credentials organized.

📁 Repository Structure
```bash

├── backend/
│   ├── codeB.py           # Logic for GPT-3.5 integration & System Prompting
│   ├── openai_helper.py   # API Configuration
│   └── logging_setup.py   # Custom server-side logging utility
├── frontend/
│   ├── main_page.py       # Streamlit UI with custom CSS styling
│   └── images/            # Asset folder for UI backgrounds
├── server.log             # Auto-generated logs for query tracking
└── README.md
```



  

⚙️ How to Run
Clone & Install:
```bash
Bash
```
```bash
git clone https://github.com/your-username/gita-ai-guide.git
pip install streamlit openai
```

Setup API Key:

```bash
Add your OpenAI key to backend/openai_helper.py.
```

Launch:

```bash
Bash
```
```bash
streamlit run frontend/main_page.py
```
📈 Impact & Use Case :

This project demonstrates how AI can be fine-tuned for Domain-Specific Expertise. By constraining the LLM's "knowledge world" to the Gita, the tool becomes a reliable source for spiritual and philosophical research rather than a general-purpose chat bot.
