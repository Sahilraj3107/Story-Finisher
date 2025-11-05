# Story Finisher 📖

An AI-powered story completion tool that uses CrewAI to generate and polish creative stories from simple story start lines.

## Features

- 🤖 AI-powered story generation using Groq LLM
- ✍️ Automatic story editing and refinement
- 📁 Dynamic file naming based on story titles
- 🎨 Multi-agent collaboration (Writer + Editor)

## Prerequisites

- Python 3.8+
- Groq API Key ([Get it here](https://console.groq.com/keys))

## Installation

### 1. Install UV (Package Manager)

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Or using pip:**
```bash
pip install uv
```

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd Story-Finisher
```

### 3. Create Virtual Environment
```bash
uv venv
```

**Activate the virtual environment:**

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
uv pip install -r requirements.txt
```

**Or manually install:**
```bash
uv pip install crewai python-dotenv
```

### 5. Setup Environment Variables

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Project Structure
```
Story-Finisher/
│
├── config/
│   ├── agents.yml          # Agent configurations
│   └── tasks.yml           # Task definitions
│
├── output/                 # Generated stories saved here
│
├── crew.py                 # CrewAI setup
├── main.py                 # Main execution file
├── .env                    # Environment variables (create this)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Configuration Files

### `config/agents.yml`

Defines two AI agents:

**Writer Agent:**
- **Role:** Creates original stories from story start lines
- **Goal:** Write complete, engaging narratives
- **Backstory:** Experienced storyteller who builds rich worlds and complex characters

**Editor Agent:**
- **Role:** Refines and polishes the writer's story
- **Goal:** Deliver only the final clean version (no editing notes)
- **Backstory:** Professional editor who silently improves stories without showing the editing process

---

### `config/tasks.yml`

Defines the workflow tasks:

**Writer Task:**
- Creates the initial story based on the input story line
- Focuses on: plot, characters, settings, emotional resonance, and satisfying conclusions
- Outputs: A complete draft story with a title

**Editor Task:**
- Takes the writer's story as input (using `context`)
- Reviews for: grammar, plot holes, character development, pacing, and clarity
- Outputs: The final polished story with "Title: <story_title>" at the end
- **Note:** Does NOT output editing notes or change logs
```

## Usage

Run the story generator:
```bash
python main.py
```

### Example Story Start Lines

Edit the `story_line` variable in `main.py`:
```python
# Broken Love
story_line = "She kept his last voicemail saved for five years, but today she finally pressed delete..."

# Mystery
story_line = "The last message on her phone was from someone who had been dead for three years..."

# Fantasy
story_line = "On his 16th birthday, the mirror didn't show his reflection—it showed someone else's life..."

# Sci-Fi
story_line = "The algorithm was supposed to predict crimes, not create criminals..."

# Dystopian
story_line = "In a city where emotions are sold in bottles, she was the only one who refused to buy..."
```

## Output

Generated stories are automatically saved in the `output/` folder with the story title as the filename:
```
output/The_Last_Voicemail.txt
output/Reflections_of_Tomorrow.txt
```

## Troubleshooting

### API Key Issues
- Make sure your `.env` file exists and contains your Groq API key
- Verify the API key is valid at [Groq Console](https://console.groq.com/keys)

### Import Errors
```bash
# Reinstall dependencies
uv pip install --force-reinstall crewai python-dotenv
```

### Permission Errors (Windows)
Run PowerShell as Administrator when installing UV

## Generate Requirements File

If you need to regenerate `requirements.txt`:
```bash
# Install pipreqs
pip install pipreqs

# Generate requirements (excluding virtual environment)
pipreqs . --force --ignore .venv
```

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License

## Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Groq](https://groq.com/) - LLM API provider

---

**Happy Story Writing! 📚✨**